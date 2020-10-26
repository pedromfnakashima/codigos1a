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

plt.legend()
plt.show()

####################################################

def gera_scatter(df_input, col_x, col_y, col_cor):
    
    x, y = df_input[col_x], df_input[col_y]
    
    classes_cor = set(df_input[col_cor])
    
    fig1, (ax1) = plt.subplots(nrows=1, ncols=1)
    
    for name in classes_cor:
        index = df_input[col_cor] == name
        ax1.scatter(x[index], y[index], marker='o', label=name)
    
    plt.legend()
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

plt.legend()
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

class Dados:
    dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}
    
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

dados = Dados()

dados.Action

plt.show()


print(Dados.dic_cores)



fig1, (ax1) = plt.subplots(nrows=1, ncols=1)

dic = {}

dic.update('Action': ax1.scatter(x['Action'], y['Action'], marker='o', color=serie_cores['azul'], s=50, alpha=0.5))

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
dic_cores = {'azul' :'#0000ff',
         'vermelho' : '#cc0000',
         'verde' : '#003300',
         'rosa' : '#ff00ff',
         'laranja' : '#ff6600',
         'marrom' : '#663300',
         'roxo' : '#6600cc'}
serie_cores = pd.Series(dic_cores)

dic_cat = {'Action': {'marker':'x', 'cor':serie_cores['azul'], 's':50, 'alpha':0.5},
           'Adventure': {'marker':'x', 'cor':serie_cores['vermelho'], 's':50, 'alpha':0.5},
           'Comedy': {'marker':'x', 'cor':serie_cores['verde'], 's':50, 'alpha':0.5},
           'Drama': {'marker':'x', 'cor':serie_cores['rosa'], 's':50, 'alpha':0.5},
           'Horror': {'marker':'x', 'cor':serie_cores['laranja'], 's':50, 'alpha':0.5},
           'Romance': {'marker':'x', 'cor':serie_cores['marrom'], 's':50, 'alpha':0.5},
           'Thriller': {'marker':'x', 'cor':serie_cores['roxo'], 's':50, 'alpha':0.5}
    }


x, y = movies['CriticRating'], movies['AudienceRating']
dic_cat = {}
for key in dic_cat.keys():
    print(dic_cat[key]['s'])
    dic_cat.update({key: ax1.scatter(x[key], y[key], marker=dic_cat[key]['marker'], color=dic_cat[key]['cor'], s=dic_cat[key]['s'], alpha=dic_cat[key]['alpha'])})


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





























