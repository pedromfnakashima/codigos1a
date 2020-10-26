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

from matplotlib import pyplot as plt

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer
lab_encoder = LabelEncoder()

movies['genero'] = lab_encoder.fit_transform(movies['Genre'])

unicos = movies['Genre'].unique()

print(movies['Genre'].unique())


# https://altair-viz.github.io/user_guide/encoding.html
#pip install altair
#pip install vega_datasets
from altair import *
import pandas as pd

df = datasets.load_dataset('iris')
Chart(df).mark_point().encode(x='petalLength',y='sepalLength', color='species')



import altair as alt
from vega_datasets import data
cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    shape='Origin'
)



import matplotlib

print(matplotlib.__version__)

pip install matplotlib

plt.scatter(x=movies['CriticRating'], y=movies['AudienceRating'])

plt.scatter(x=movies['CriticRating'], y=movies['AudienceRating'], c=movies['genero'])

plt.colorbar()

x = movies['CriticRating']
y = movies['AudienceRating']
colors = movies['Genre']
sizes = movies['Genre']

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')

import numpy as np
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar();  # show color scale




















import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
price_data = (cbook.get_sample_data('goog.npz', np_load=True)['price_data'].view(np.recarray))
price_data = price_data[-250:]  # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()










