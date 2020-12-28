# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 08:51:08 2020

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

##########################################################################################################
##########################################################################################################
##########################################################################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Ciência da dados para empresas e negócios (Udemy)' /'Bases de dados'
employee_df = pd.read_csv(pasta / 'Human_Resources.csv')

print(employee_df.shape)
print(employee_df.head())
print(employee_df.info())
print(employee_df.describe())

# Fazendo o encode
employee_df['Attrition'] = employee_df['Attrition'].apply(lambda x: 1 if x=='Yes' else 0)
employee_df['OverTime'] = employee_df['OverTime'].apply(lambda x: 1 if x=='Yes' else 0)
employee_df['Over18'] = employee_df['Over18'].apply(lambda x: 1 if x=='Y' else 0)


# Mapa de calor do seaborn
# Para descobrir se existem valores nuloes na base de dados
sns.heatmap(employee_df.isnull())
sns.heatmap(employee_df.isnull(), cbar=False)

# Gráficos para os atributos
employee_df.hist(bins=30,figsize=(20,20),color='r')

employee_df.drop(['EmployeeCount','StandardHours','Over18','EmployeeNumber'],axis=1,inplace=True)

left_df = employee_df[employee_df['Attrition'] ==1]
stayed_df = employee_df[employee_df['Attrition'] ==0]

print('Total = ', len(employee_df))
print('Número de funcionários que saíram da empresa = ', len(left_df))
print('Porcentagem de funcionários que saíram da empresa = ', (len(left_df)/len(employee_df))*100)
print('Número de funcionários que ficaram da empresa = ', len(stayed_df))
print('Porcentagem de funcionários que ficaram da empresa = ', (len(stayed_df)/len(employee_df))*100)

print(left_df.describe())
print(stayed_df.describe())

# Matriz de correlações
correlations = employee_df.corr()
# Gráfico de calor das correlações
f, ax = plt.subplots(figsize=(20,20))
sns.heatmap(correlations, annot=True)

#
plt.figure(figsize=[25,12])
sns.countplot(x='Age',data=employee_df)

# Cor dependendo se a pessoa sai ou não da empresa
plt.figure(figsize=[25,12])
sns.countplot(x='Age', hue='Attrition',data=employee_df)

#
'''
Explicação:
411 -> 4 linhas, 1 coluna, id = 1
412 -> 4 linhas, 1 coluna, id = 2
413 -> 4 linhas, 1 coluna, id = 3
414 -> 4 linhas, 1 coluna, id = 4
'''
plt.figure(figsize=[20,20])
plt.subplot(411)
sns.countplot(x='JobRole',hue='Attrition',data=employee_df)

plt.subplot(412)
sns.countplot(x='MaritalStatus',hue='Attrition',data=employee_df)

plt.subplot(413)
sns.countplot(x='JobInvolvement',hue='Attrition',data=employee_df)

plt.subplot(414)
sns.countplot(x='JobLevel',hue='Attrition',data=employee_df)

# KDE (Kernel Density Estimate)
plt.figure(figsize=(12,7))
sns.kdeplot(left_df['DistanceFromHome'],label='Funcionários que saíram da empresa',color='r',shade=True)
sns.kdeplot(stayed_df['DistanceFromHome'],label='Funcionários que ficaram na empresa',color='b',shade=True)

#
plt.figure(figsize=(12,7))
sns.kdeplot(left_df['TotalWorkingYears'],label='Funcionários que saíram da empresa',color='r',shade=True)
sns.kdeplot(stayed_df['TotalWorkingYears'],label='Funcionários que ficaram na empresa',color='b',shade=True)

# Boxplot
plt.figure(figsize=(15,10))
sns.boxplot(x='MonthlyIncome',y='Gender',data=employee_df)

#
plt.figure(figsize=(15,10))
sns.boxplot(x='MonthlyIncome',y='JobRole',data=employee_df)

# Pré-processamento e bases de treinamento/teste
print(employee_df.head())

'''
Transformar atributos categóricos em números
Encode
Para atributos que não têm ordem de importância,
devemos usar dummies
'''
X_cat = employee_df[['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus']]

from sklearn.preprocessing import OneHotEncoder

onehotencoder = OneHotEncoder()
X_cat = onehotencoder.fit_transform(X_cat).toarray()
X_cat = pd.DataFrame(X_cat)

print(employee_df['BusinessTravel'].unique())

'''
vars_cat = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus']
vars_cat_set = set(vars_cat)
vars_tot = list(employee_df.columns)
vars_tot_set = set(vars_tot)
vars_num_set = vars_tot_set.difference(vars_cat_set)
vars_num = list(vars_num_set)
X_numerical = employee_df[vars_num]
'''
X_numerical = employee_df[['Age', 'DailyRate', 'DistanceFromHome',	'Education', 'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement',	'JobLevel',	'JobSatisfaction',	'MonthlyIncome',	'MonthlyRate',	'NumCompaniesWorked',	'OverTime',	'PercentSalaryHike', 'PerformanceRating',	'RelationshipSatisfaction',	'StockOptionLevel',	'TotalWorkingYears'	,'TrainingTimesLastYear'	, 'WorkLifeBalance',	'YearsAtCompany'	,'YearsInCurrentRole', 'YearsSinceLastPromotion',	'YearsWithCurrManager']]

X_all = pd.concat([X_cat,X_numerical],axis=1)
print(X_all.shape)

# Normalizando:

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X = scaler.fit_transform(X_all)

y = employee_df['Attrition']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

print(X_train.shape)
print(y_train.shape)

print(X_test.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression()

logistic.fit(X_train, y_train)

y_pred = logistic.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True)

# Cálculo do Precision - manual
'''
TP/(TP+FP)
Quando prevê que é positivo, ou seja,
que o funcionário sairá da empresa, ele
está certo em 79% das vezes
'''
print(19/(19+5))

# Cálculo do Recall - manual
'''
FN: pessoas que, na base de dados tem indicação
de que elas vão sair da empresa (ou saíram
da empresa), porém elas foram classificadas
como se elas não fossem sair da empresa.
TP/(TP+FN)
O modelo indica corretamente 32% das pessoas
que vão sair da empresa
'''
print(19/(19+39))

# Executando os mesmos cálculos utilizando
# o sklearn

from sklearn.metrics import precision_score, recall_score, f1_score, classification_report

print(precision_score(y_test, y_pred))

print(recall_score(y_test, y_pred))

print(f1_score(y_test, y_pred, average='macro'))

print(classification_report(y_test, y_pred))

######################################
############ RANDON FOREST ###########
######################################

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier()

forest.fit(X_train, y_train)

y_pred = forest.predict(X_test)

print(accuracy_score(y_test, y_pred))

cm = confusion_matrix(y_pred, y_test)
print(cm)

sns.heatmap(cm,annot=True)

print(classification_report(y_test,y_pred))

######################################
############ REDES NEURAIS ###########
######################################

import tensorflow as tf

rede_neural = tf.keras.models.Sequential()

# adicionando primeira camada
rede_neural.add(tf.keras.layers.Dense(units=25, activation='relu', input_shape=(50,)))

print(X_train.shape)

'''
Número de neurônios=
(Número de entradas (50) + Número de saídas (1) )/ 2 = 25,5
Arrendondando -> 25 (units=25)
A única saída é a probabilidade
'''

# adicionando segunda camada oculta
rede_neural.add(tf.keras.layers.Dense(units=25, activation='relu'))

# adicionando terceira camada oculta
rede_neural.add(tf.keras.layers.Dense(units=25, activation='relu'))

# defindo a camada de saída
rede_neural.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

'''
sigmoide gera números entre 0 e 1
como a única saída é a probabilidade,
units = 1
'''

print(rede_neural.summary())

rede_neural.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])

rede_neural.fit(X_train, y_train, epochs=200)

y_pred = rede_neural.predict(X_test)
print(y_pred)

y_pred = (y_pred >= 0.5)

cm = confusion_matrix(y_test,y_pred)

print(cm)

sns.heatmap(cm, annot=True)

print(classification_report(y_test,y_pred))

#########################################
######### SALVAR O CLASSIFICADOR ########
#########################################
pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Ciência da dados para empresas e negócios (Udemy)'
os.chdir(pasta)

import pickle

with open('variaveis_modelo.pkl','wb') as f:
    pickle.dump([scaler,onehotencoder,logistic], f)

with open('variaveis_modelo.pkl','rb') as f:
    min_max, encoder, model = pickle.load(f)

print(min_max, encoder, model)

X_novo = employee_df.iloc[0:1]

X_cat_novo = X_novo[['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus']]

X_cat_novo = encoder.transform(X_cat_novo).toarray()

X_cat_novo = pd.DataFrame(X_cat_novo)

X_numerical_novo = X_novo[['Age', 'DailyRate', 'DistanceFromHome',	'Education', 'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement',	'JobLevel',	'JobSatisfaction',	'MonthlyIncome',	'MonthlyRate',	'NumCompaniesWorked',	'OverTime',	'PercentSalaryHike', 'PerformanceRating',	'RelationshipSatisfaction',	'StockOptionLevel',	'TotalWorkingYears'	,'TrainingTimesLastYear'	, 'WorkLifeBalance',	'YearsAtCompany'	,'YearsInCurrentRole', 'YearsSinceLastPromotion',	'YearsWithCurrManager']]

X_all_novo = pd.concat([X_cat_novo,X_numerical_novo],axis=1)

X_novo = min_max.transform(X_all_novo)

model.predict(X_novo)

print(model.predict(X_novo))

print(model.predict_proba(X_novo))

print(model.classes_)











