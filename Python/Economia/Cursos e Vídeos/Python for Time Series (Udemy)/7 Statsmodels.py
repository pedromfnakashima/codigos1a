# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:13:25 2020

@author: pedro-salj
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
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

#############################
########## FILTRO HP ########
#############################

import numpy as np
import pandas as pd
df = pd.read_csv('macrodata.csv', index_col=0, parse_dates=True)

df['realgdp'].plot(figsize=(12,5))

""" Filtro HP """

from statsmodels.tsa.filters.hp_filter import hpfilter

# Resultado é uma tupla
gdp_cycle, gdp_trend = hpfilter(df['realgdp'], lamb=1600)

print(type(gdp_trend))

gdp_trend.plot()

df['trend'] = gdp_trend

print(df.head())

df[['trend', 'realgdp']].plot(figsize=(12,5))

df[['trend', 'realgdp']]['2005-01-01':].plot(figsize=(12,5))


#####################################
########## ETS DECOMPOSITION ########
#####################################
""" Error Trend Sazonality """

import numpy as np
import pandas as pd
airline = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)

print(airline)

airline = airline.dropna() # precisa pra ets

airline.plot()

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')

print(result.trend.head(10))

result.plot()

result.plot();

""" para mudar o tamanho permanentemente """

from pylab import rcParams
rcParams['figure.figsize'] = 12,5
result.plot()

#####################################
########## EWMA #####################
#####################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

airline = pd.read_csv('airline_passengers.csv', index_col='Month')

print(airline.head())
print(airline.index)

airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

print(airline.index)

airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()

airline.plot()
airline.plot(figsize=(10,8))

# EWMA

airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()

airline[['Thousands of Passengers', 'EWMA-12']].plot()

airline[['Thousands of Passengers', 'EWMA-12']].plot(figsize=(10,8))

# HOLT WINTERS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('airline_passengers.csv', index_col='Month', parse_dates=True)
df = df.dropna()

print(df.index)
# freq = None

""" O passo abaixo é fundamental
para se rodar statsmodels """
df.index.freq = 'MS' # MS = Monthly Start

print(df.index)
# freq = MS

print(df.head())

""" Simple Exponential Smoothing """

from statsmodels.tsa.holtwinters import SimpleExpSmoothing

span = 12
alpha = 2/(span+1)

df['EWMA12'] = df['Thousands of Passengers'].ewm(alpha=alpha, adjust=False).mean()

"""
Simple Exponential Smoothing
com Statsmodels
"""
model = SimpleExpSmoothing(df['Thousands of Passengers'])

fitted_model = model.fit(smoothing_level=alpha, optimized=False)

print(fitted_model.fittedvalues.shift(-1))

df['SES12'] = fitted_model.fittedvalues.shift(-1)

print(df.head())

df.plot()

"""
Double Exponential Smoothing
=
Modelo de Holt
"""
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df['DES_add_12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='add').fit().fittedvalues.shift(-1)

print(df.head())

print(df.columns)

df[['Thousands of Passengers', 'SES12', 'DES_add_12']].plot()

df[['Thousands of Passengers', 'SES12', 'DES_add_12']].iloc[:24].plot(figsize=(12,5)) # Primeiros 2 anos (24 meses)

df[['Thousands of Passengers', 'SES12', 'DES_add_12']].iloc[-24:].plot(figsize=(12,5)) # Últimos 2 anos (24 meses)

df['DES_mul_12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='mul').fit().fittedvalues.shift(-1)

print(df.columns)

df[['Thousands of Passengers', 'SES12', 'DES_add_12', 'DES_mul_12']].iloc[-24:].plot(figsize=(12,5)) # Últimos 2 anos (24 meses)
df[['Thousands of Passengers', 'SES12', 'DES_add_12', 'DES_mul_12']].iloc[:24].plot(figsize=(12,5)) # Primeiros 2 anos (24 meses)

"""
Triple Exponential Smoothing
=
Modelo de Holt-Winters
"""

df['TES_mul_12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='mul', seasonal='mul', seasonal_periods=12).fit().fittedvalues

df.plot()

print(df.columns)

df[['Thousands of Passengers', 'DES_mul_12', 'TES_mul_12']].plot(figsize=(12,6)) # Todos os dados
df[['Thousands of Passengers', 'DES_mul_12', 'TES_mul_12']].iloc[:24].plot(figsize=(12,6)) # 2 primeiros anos (começo dos dados) => TES pior que DES
df[['Thousands of Passengers', 'DES_mul_12', 'TES_mul_12']].iloc[-24:].plot(figsize=(12,6)) # 2 últimos anos (final dos dados) => TES melhor que DES

