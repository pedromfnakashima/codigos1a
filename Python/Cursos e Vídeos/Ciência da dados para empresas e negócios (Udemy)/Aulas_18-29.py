# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:11:59 2020

@author: pedro
"""

#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Ciência da dados para empresas e negócios (Udemy)' /'Bases de dados'
creditcard_df = pd.read_csv(pasta / 'Marketing_data.csv')

print(creditcard_df.shape)
print(creditcard_df.head())
print(creditcard_df.info())
print(creditcard_df.describe())

sns.heatmap(creditcard_df.isnull())

# Lista quantidade de valores nulos por coluna
print(creditcard_df.isnull().sum())

nulos_minimum_payments = creditcard_df.loc[(creditcard_df['MINIMUM_PAYMENTS'].isnull() == True)]

# Imputa a média p/ os valores nulos da coluna
creditcard_df.loc[(creditcard_df['MINIMUM_PAYMENTS'].isnull() == True), 'MINIMUM_PAYMENTS'] = creditcard_df['MINIMUM_PAYMENTS'].mean()
creditcard_df.loc[(creditcard_df['CREDIT_LIMIT'].isnull() == True), 'CREDIT_LIMIT'] = creditcard_df['CREDIT_LIMIT'].mean()

# Valores duplicados
print(creditcard_df.duplicated().sum())

# Apaga identificador do cliente
creditcard_df.drop('CUST_ID',axis=1,inplace=True)

# Aula 21
print(creditcard_df.columns)

print(len(creditcard_df.columns)) # 17

# Distribuição de frequência de cada uma
# das colunas
plt.figure(figsize=(10,50))
for i in range(len(creditcard_df.columns)):
    plt.subplot(17,1,i+1)
    sns.distplot(creditcard_df[creditcard_df.columns[i]], kde=True)
    plt.title(creditcard_df.columns[i])
plt.tight_layout()

# Matriz de correlações
correlations = creditcard_df.corr()
# Mapa de calor da matriz de correlações
f, ax = plt.subplots(figsize=(20,20))
sns.heatmap(correlations, annot=True)

# AULA 23 - OBTENÇÃO DO NÚMERO DE CLUSTERS

print(min(creditcard_df['BALANCE']))
print(max(creditcard_df['BALANCE']))

# Padronizar tudo

scaler = StandardScaler()

creditcard_df_scaled = scaler.fit_transform(creditcard_df)

print(min(creditcard_df_scaled[0]))
print(max(creditcard_df_scaled[0]))

'''
Definição do número de grupos
Elbow method (método do cotovelo)
'''

wcss_1 = []
range_values = range(1,21)

for i in range_values:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(creditcard_df_scaled)
    wcss_1.append(kmeans.inertia_)


plt.plot(wcss_1, 'bx-', color='r')
plt.xlabel('Clusters')
plt.ylabel('WCSS')

'''wcss_1 = pd.DataFrame(wcss_1)
wcss_1['K'] = range(1,21)
wcss_1.rename(columns={0:'WCSS'},inplace=True)

plt.plot(wcss_1['K'], wcss_1['WCSS'], 'bx-')
plt.xlabel('Clusters')
plt.ylabel('WCSS')
plt.xticks(np.arange(1, 21, step=1))
plt.grid()
'''

# AULA 24

kmeans = KMeans(n_clusters=8)
kmeans.fit(creditcard_df_scaled)
labels = kmeans.labels_

print(np.unique(labels,return_counts=True))

# centróides
print(kmeans.cluster_centers_)

cluster_centers = pd.DataFrame(data=kmeans.cluster_centers_,columns=[creditcard_df.columns])

cluster_centers = scaler.inverse_transform(cluster_centers)

cluster_centers = pd.DataFrame(data=cluster_centers,columns=[creditcard_df.columns])

# AULA 25

'''
Adicionar cada um dos grupos a cada um
dos clientes.
'''
creditcard_df_cluster = pd.concat([creditcard_df,pd.DataFrame({'cluster':labels})], axis=1)

for i in creditcard_df.columns:
    plt.figure(figsize=(35,5))
    for j in range(8):
        plt.subplot(1,8,j+1)
        cluster = creditcard_df_cluster[creditcard_df_cluster['cluster'] == j]
        cluster[i].hist(bins=20)
        plt.title('{}\nCluster {}'.format(i,j))
    plt.show

credit_ordered = creditcard_df_cluster.sort_values(by='cluster')

# AULA 26

pca = PCA(n_components=2)

principal_comp = pca.fit_transform(creditcard_df_scaled)

pca_df = pd.DataFrame(data=principal_comp, columns=['pca1','pca2'])

pca_df = pd.concat([pca_df, pd.DataFrame({'cluster':labels})], axis=1)

#
plt.figure(figsize=(10,10))
sns.scatterplot(x='pca1',y='pca2',hue='cluster',data=pca_df)
#
plt.figure(figsize=(10,10))
sns.scatterplot(x='pca1',y='pca2',hue='cluster',data=pca_df, palette=['red','green','blue','pink','yellow','gray','purple','black'])

# AULA 28 - Construção e treinamento de autoencoders

print(creditcard_df_scaled.shape)

'''
REDUÇÃO DE DIMENSIONALIDADE (c/ autoencoders)
17 -> 500 -> 2000 -> 10
-> 2000 -> 500 -> 17
'''

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# 
input_df = Input(shape=(17,))
x = Dense(500, activation='relu')(input_df)
x = Dense(2000, activation='relu')(x)

encoded = Dense(10, activation='relu')(x)

x = Dense(2000, activation='relu')(encoded)
x = Dense(500, activation='relu')(x)

decoded = Dense(17)(x)

# autoencoder
autoencoder = Model(input_df, decoded)

# encoder
encoder = Model(input_df, encoded)

autoencoder.compile(optimizer='Adam', loss='mean_squared_error')

autoencoder.fit(creditcard_df_scaled, creditcard_df_scaled, epochs=50)

print(creditcard_df_scaled.shape)

compact = encoder.predict(creditcard_df_scaled)

print(compact.shape)

# AULA 29 - CONSTRUÇÃO E TREINAMENTO DE AUTOENCODERS 2

wcss_2 = []
range_values = range(1,21)

for i in range_values:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(compact)
    wcss_2.append(kmeans.inertia_)

##
plt.plot(wcss_2, 'bx-')
plt.xlabel('Clusters')
plt.ylabel('WCSS')

##
plt.plot(wcss_1, 'bx-', color='r')
plt.plot(wcss_2, 'bx-', color='g')

##

kmeans = KMeans(n_clusters=4)
kmeans.fit(compact)

labels = kmeans.labels_
print(labels, labels.shape)

df_cluster_at = pd.concat([creditcard_df, pd.DataFrame({'cluster':labels})], axis=1)

##

pca = PCA(n_components=2)
prin_comp = pca.fit_transform(compact)
pca_df = pd.DataFrame(data=prin_comp, columns=['pca1','pca2'])

pca_df = pd.concat([pca_df,pd.DataFrame({'cluster':labels})], axis=1)

##

plt.figure(figsize=(10,10))
sns.scatterplot(x='pca1',y='pca2',hue='cluster',data=pca_df, palette=['red','green','blue','pink'])

##

df_cluster_ordered = df_cluster_at.sort_values(by='cluster')
















