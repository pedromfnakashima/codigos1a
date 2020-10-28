# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:48:03 2020

@author: pedro

IMPORTANTE!
NÃO uso o dataset do curso,
mas do curso R Programming A-Z,
também da Udemy
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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'R Programming A-Z (Udemy)'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

#############################
#############################
#############################
globals().clear()
import pandas as pd
movies = pd.read_csv('P2-Movie-Ratings.csv')

print(movies.columns)

movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

movies['CriticRating'].plot.hist()

movies['CriticRating'].plot.hist(edgecolor='k')

movies['CriticRating'].plot.hist(edgecolor='k').autoscale(enable=True, axis='both', tight=True)

movies['CriticRating'].plot.hist(bins=20, edgecolor='k').autoscale(enable=True, axis='both', tight=True)

movies['CriticRating'].plot.hist(bins=50, edgecolor='k').autoscale(enable=True, axis='both', tight=True)

movies['CriticRating'].plot.hist(grid=True)

movies[['CriticRating', 'AudienceRating', 'BudgetMillions']].plot.bar()

movies[['CriticRating', 'AudienceRating', 'BudgetMillions']].plot.bar(stacked=True)

movies[['CriticRating', 'AudienceRating', 'BudgetMillions']].plot.barh(stacked=True)

movies.plot.line(y='CriticRating')

movies.plot.line(y='CriticRating', figsize=(10,4))

movies.plot.line(y='CriticRating', figsize=(10,4), lw=4)

movies.plot.line(y=['CriticRating', 'AudienceRating'], figsize=(10,4), lw=4)

movies.plot.area(y=['CriticRating', 'AudienceRating'])

movies.plot.area(y=['CriticRating', 'AudienceRating'], alpha=0.4)

movies.plot.area(y=['CriticRating', 'AudienceRating'], alpha=0.4, stacked=False)

# Scatter plots - não funciona bem

movies.plot.scatter(x='CriticRating', y='AudienceRating')

movies.plot.scatter(x='CriticRating', y='AudienceRating', c='Genre')

movies.plot.scatter(x='CriticRating', y='AudienceRating', c='AudienceRating')


movies.plot.scatter(x='CriticRating', y='AudienceRating', c='Genre', cmap='coolwarm')

movies.plot.scatter(x='CriticRating', y='AudienceRating', s=movies['Genre'])
movies.plot.scatter(x='CriticRating', y='AudienceRating', s=movies['Genre']*50)
movies.plot.scatter(x='CriticRating', y='AudienceRating', s=movies['Genre']*50, alpha=0.3)

# Scatter plots - pyplot
# https://stackoverflow.com/questions/28033046/matplotlib-scatter-color-by-categorical-factors
# https://medium.com/@contactsunny/label-encoder-vs-one-hot-encoder-in-machine-learning-3fc273365621

#############################
##### CONFIGURAÇÃO GERAL ####
#############################
"""
Funcionando

ATENÇÃO!!!!
TEM QUE RODAR TUDO DE UMA VEZ!!!!!!!!!!! Pelo menos:
    fig1, (ax1) = plt.subplots(nrows=1, ncols=1)
    e
    ax1.scatter(x[index], y[index], marker='o', label=name)

"""
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'R Programming A-Z (Udemy)'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

#############################
#############################
#############################

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

x, y = movies['CriticRating'], movies['AudienceRating']
classes_cor = set(movies['Genre'])

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

for name in classes_cor:
    index = movies['Genre'] == name
    ax1.scatter(x[index], y[index], marker='o', label=name)

ax1.legend()
plt.show()

####################################################

def gera_scatter(df_input, col_x, col_y, col_cor):
    
    x, y = df_input[col_x], df_input[col_y]
    
    classes_cor = set(df_input[col_cor])
    
    fig1, (ax1) = plt.subplots(nrows=1, ncols=1)
    
    for name in classes_cor:
        index = df_input[col_cor] == name
        ax1.scatter(x[index], y[index], marker='o', label=name)
    
    ax1.legend()
    plt.show()
    
    return fig1

gera_scatter(df_input=movies,
             col_x='CriticRating',
             col_y='AudienceRating',
             col_cor='Genre')

####################################################

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer
lab_encoder = LabelEncoder()
movies['GeneroCod'] = lab_encoder.fit_transform(movies['Genre'])

x, y = movies['CriticRating'], movies['AudienceRating']
classes_cor_set = set(movies['Genre'])

cor_corresp = movies.groupby('Genre').first().loc[:, 'GeneroCod'].reset_index()

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

ax1.scatter(x, y, marker='o')

ax1.legend()
plt.show()

####################################################
# Funcionando

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer
lab_encoder = LabelEncoder()
movies['GeneroCod'] = lab_encoder.fit_transform(movies['Genre'])

x, y = movies['CriticRating'], movies['AudienceRating']
cor = movies['GeneroCod']
classes_cor_set = set(movies['Genre'])

cor_corresp = movies.groupby('Genre').first().loc[:, 'GeneroCod']

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

#ax1.scatter(x, y, marker='o', c='b')
turquesa = '#afeeee'
azul = '#3352FF'
vermelho = '#FF3333'
ax1.scatter(x, y, marker='o', color=vermelho)

plt.legend()
plt.show()

""" FUNCIONANDO!!! """
####################################################
# 
# https://stackoverflow.com/questions/29973952/how-to-draw-legend-for-scatter-plot-indicating-size

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer
lab_encoder = LabelEncoder()
movies['GeneroCod'] = lab_encoder.fit_transform(movies['Genre'])

movies.set_index('Genre', inplace=True)

# 7 cores
azul = '#0000ff'
vermelho = '#cc0000'
verde = '#003300'
rosa = '#ff00ff'
laranja = '#ff6600'
marrom = '#663300'
roxo = '#6600cc'
dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}
serie_cores = pd.Series(dic_cores)

x, y = movies['CriticRating'], movies['AudienceRating']

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

Action = ax1.scatter(x['Action'], y['Action'], marker='o', color=serie_cores['azul'], s=50, alpha=0.5)
Adventure = ax1.scatter(x['Adventure'], y['Adventure'], marker='o', color=serie_cores['vermelho'], s=50, alpha=0.5)
Comedy = ax1.scatter(x['Comedy'], y['Comedy'], marker='o', color=serie_cores['verde'], s=50, alpha=0.5)
Drama = ax1.scatter(x['Drama'], y['Drama'], marker='o', color=serie_cores['rosa'], s=50, alpha=0.5)
Horror = ax1.scatter(x['Horror'], y['Horror'], marker='o', color=serie_cores['laranja'], s=50, alpha=0.5)
Romance = ax1.scatter(x['Romance'], y['Romance'], marker='o', color=serie_cores['marrom'], s=50, alpha=0.5)
Thriller = ax1.scatter(x['Thriller'], y['Thriller'], marker='o', color=serie_cores['roxo'], s=50, alpha=0.5)

ax1.legend( (Action, Adventure, Comedy, Drama, Horror, Romance, Thriller),
           ('Action', 'Adventure', 'Comedy', 'Drama', 'Horror', 'Romance', 'Thriller'),
           loc = 'lower left',
           ncol=1,
           fontsize=8
    )

plt.show()
####################################################

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.set_index('Genre', inplace=True)

# 7 cores
dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}
serie_cores = pd.Series(dic_cores)


x, y = movies['CriticRating'], movies['AudienceRating']

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

ax1.scatter(x['Action'], y['Action'], marker='o', color=serie_cores['azul'], s=50, alpha=0.5, label='Action')
ax1.scatter(x['Adventure'], y['Adventure'], marker='o', color=serie_cores['vermelho'], s=50, alpha=0.5, label='Adventure')
ax1.scatter(x['Comedy'], y['Comedy'], marker='o', color=serie_cores['verde'], s=50, alpha=0.5, label='Comedy')
ax1.scatter(x['Drama'], y['Drama'], marker='o', color=serie_cores['rosa'], s=50, alpha=0.5, label='Drama')
ax1.scatter(x['Horror'], y['Horror'], marker='o', color=serie_cores['laranja'], s=50, alpha=0.5, label='Horror')
ax1.scatter(x['Romance'], y['Romance'], marker='o', color=serie_cores['marrom'], s=50, alpha=0.5, label='Romance')
ax1.scatter(x['Thriller'], y['Thriller'], marker='o', color=serie_cores['roxo'], s=50, alpha=0.5, label='Thriller')

ax1.legend(loc = 'lower left',
           ncol=1,
           fontsize=8
    )

plt.show()

####################################################

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.set_index('Genre', inplace=True)

# 7 cores
dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}
serie_cores = pd.Series(dic_cores)


x, y = movies['CriticRating'], movies['AudienceRating']

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

ax1.scatter(x['Action'], y['Action'], marker='o', color=serie_cores['azul'], s=50, alpha=0.5, label='Action')
ax1.scatter(x['Adventure'], y['Adventure'], marker='o', color=serie_cores['vermelho'], s=50, alpha=0.5, label='Adventure')
ax1.scatter(x['Comedy'], y['Comedy'], marker='o', color=serie_cores['verde'], s=50, alpha=0.5, label='Comedy')
ax1.scatter(x['Drama'], y['Drama'], marker='o', color=serie_cores['rosa'], s=50, alpha=0.5, label='Drama')
ax1.scatter(x['Horror'], y['Horror'], marker='o', color=serie_cores['laranja'], s=50, alpha=0.5, label='Horror')
ax1.scatter(x['Romance'], y['Romance'], marker='o', color=serie_cores['marrom'], s=50, alpha=0.5, label='Romance')
ax1.scatter(x['Thriller'], y['Thriller'], marker='o', color=serie_cores['roxo'], s=50, alpha=0.5, label='Thriller')

ax1.legend(loc = 'lower left',
           ncol=1,
           fontsize=8
    )

plt.show()
####################################################

import pandas as pd
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.set_index('Genre', inplace=True)

# 7 cores
dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}
serie_cores = pd.Series(dic_cores)
cores = np.random.choice(serie_cores, 7, replace=False)

x, y = movies['CriticRating'], movies['AudienceRating']

fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

qtd_categorias = len(movies.groupby('Genre').first())


indices = list(movies.groupby('Genre').first().index)
for indice, nome in enumerate(indices):
    ax1.scatter(x[nome], y[nome], marker='o', color=cores[indice], s=50, alpha=0.5, label=nome)

ax1.legend(loc = 'lower left',
           ncol=1,
           fontsize=8
    )

plt.show()

####################################################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'R Programming A-Z (Udemy)'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

movies = pd.read_csv('P2-Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}

# Funcionando


def gera_grafico(df_input, var_x, var_y, var_cor, dic_cores):
    
    df_copia = df_input.copy()
    
    df_copia.set_index(var_cor, inplace=True)
    

    serie_cores = pd.Series(dic_cores)
    
    qtd_categorias = len(df_copia.groupby(var_cor).first())
    
    cores = np.random.choice(serie_cores, qtd_categorias, replace=False)
    
    x, y = df_copia[var_x], df_copia[var_y]
    
    fig1, (ax1) = plt.subplots(nrows=1, ncols=1)
    
    indices = list(df_copia.groupby(var_cor).first().index)
    for indice, nome in enumerate(indices):
        ax1.scatter(x[nome], y[nome], marker='o', color=cores[indice], s=50, alpha=0.5, label=nome)
    
    ax1.legend(loc = (1.03,-0.1),
               ncol=1,
               fontsize=8,
               title=var_cor
        )
    
    ax1.set_xlabel(var_x)
    ax1.set_ylabel(var_y)
    
    plt.show()

gera_grafico(movies, var_x='CriticRating', var_y='AudienceRating', var_cor='Genre', dic_cores=dic_cores )

#################

movies['BudgetMillions'].plot.hist(bins=50, edgecolor='k').autoscale(enable=True, axis='both', tight=True)

cond1 = movies['BudgetMillions'] >=0
cond2 = movies['BudgetMillions'] <=99
movies.loc[cond1 & cond2, 'Faixas'] = 'Até 99'

cond1 = movies['BudgetMillions'] > 100
cond2 = movies['BudgetMillions'] <=200
movies.loc[cond1 & cond2, 'Faixas'] = 'De 100 a 200'

cond1 = movies['BudgetMillions'] > 200
movies.loc[cond1, 'Faixas'] = 'Acima de 200'

del cond1, cond2

###

import seaborn as sns

sns.scatterplot(data=movies, x="CriticRating", y="AudienceRating")

sns.scatterplot(data=movies, x="CriticRating", y="AudienceRating", hue="Genre")

sns.scatterplot(data=movies, x="CriticRating", y="AudienceRating", hue="Genre", size="BudgetMillions")











