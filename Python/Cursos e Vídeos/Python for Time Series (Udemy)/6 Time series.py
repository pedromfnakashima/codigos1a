# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:37:30 2020

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
caminho_wd = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python Time Series (Udemy)' / 'Data'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())


#############################
#############################
#############################
globals().clear()

from datetime import datetime

my_year = 2020
my_month = 1
my_day = 2
my_hour = 13
my_min = 30
my_sec = 15

my_date = datetime(my_year, my_month, my_day)
print(my_date)
print(type(my_date))

my_date_time = datetime(my_year, my_month, my_day, my_hour, my_min, my_sec)
print(my_date_time)

print(my_date_time.day)

#############################
##### datetime do numpy #####
#############################

import numpy as np

date = np.array(['2020-03-15', '2020-03-16', '2020-03-17'])
print(type(date))

date = np.array(['2020-03-15', '2020-03-16', '2020-03-17'], dtype='datetime64')
print(date.dtype)

date = np.array(['2020-03-15', '2020-03-16', '2020-03-17'], dtype='datetime64[Y]')
print(date.dtype)

date = np.array(['2020-03-15', '2020-03-16', '2020-03-17'], dtype='datetime64[h]')
print(date.dtype)
print(date)


#############################
##### np.arange #############
#############################
print(np.arange(0,10,2))

print(np.arange('2018-06-01','2018-06-23', 7, dtype='datetime64[D]'))

print(np.arange('1968','1976', dtype='datetime64[Y]'))

#############################
##### pandas ################
#############################

import pandas as pd

print(pd.date_range('2020-01-01', periods=7, freq='D'))

print(pd.date_range('Jan 01, 2018', periods=7, freq='D'))

print(pd.to_datetime(['1/2/2018', 'Jan 03, 2018']))

print(pd.to_datetime(['1/2/2018', '1/3/2018']))

print(pd.to_datetime(['2/1/2018', '3/1/2018']))

print(pd.to_datetime(['2/1/2018', '3/1/2018'], format='%d/%m/%Y'))

print(pd.to_datetime(['2--1--2018', '3--1--2018'], format='%d--%m--%Y'))

data = np.random.randn(3,2)
cols = ['A', 'B']
print(data)


idx = pd.date_range('2020-01-01', periods=3, freq='D')

df = pd.DataFrame(data, index=idx, columns=cols)

print(df)
print(df.index)
print(df.index.max())
print(df.index.argmax())
print(df.index.argmin())

#############################
##### Time Resampling #######
#############################


import pandas as pd


pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
df = pd.read_csv(pasta / 'starbucks.csv', index_col='Date', parse_dates=True)

print(df.head())

print(df.info())

print(df.index)

# daily --> yearly
print(df.resample(rule='A').mean())
print(df.resample(rule='A').std())

def first_day(entry):
    
    # IS THERE AN ENTRY?
    if len(entry) != 0:
        # IF SO, RETURN FIRST ENTRY
        return entry[0]

print(df.resample(rule='A').apply(first_day))

df['Close'].resample('A').mean().plot.bar()

title = 'Monthly Max Closing Price for Starbucks'
df['Close'].resample('M').max().plot.bar(figsize=(16,6), title=title, color='#1f77b4')

#############################
##### Time Shifting #########
#############################

import pandas as pd

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
df = pd.read_csv(pasta / 'starbucks.csv', index_col='Date', parse_dates=True)

print(df.head())
print(df.tail())

print(df.shift(1))

print(df.shift(1, fill_value=0))

print(df.shift(1).tail())

print(df.shift(5))

# df = df.shift(5)

print(df.shift(-1))
print(df.shift(-1).tail())

# -----------------------------------

print(df.shift(periods=1, freq='M'))


#################################
##### Rolling and Expanding #####
#################################

# Rolling ---------------------------------------

import pandas as pd

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
df = pd.read_csv(pasta / 'starbucks.csv', index_col='Date', parse_dates=True)

df['Close'].plot()

df['Close'].plot(figsize=(12,5))

print(df.rolling(window=7).mean().head(10))

df['Close'].plot(figsize=(12,5))
df.rolling(window=7).mean()['Close'].plot()

df['Close'].plot(figsize=(12,5))
df.rolling(window=30).mean()['Close'].plot()

df['Close'].plot(figsize=(12,5))
df.rolling(window=60).mean()['Close'].plot()

df['Close'].plot(figsize=(12,5))
df.rolling(window=15).mean()['Close'].plot()

df['Close: 30 Day Mean'] = df['Close'].rolling(window=30).mean()

print(df.head())

df[['Close', 'Close: 30 Day Mean']].plot(figsize=(12,5))

# Expanding ---------------------------------------

df['Close'].expanding().mean().plot(figsize=(12,5))


########################################
##### Visualizing Time Series Data #####
########################################

import pandas as pd

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
df = pd.read_csv(pasta / 'starbucks.csv', index_col='Date', parse_dates=True)

print(df.index)

#df.index = pd.to_datetime(df.index)

df.plot()

df['Close'].plot()

df['Close'].plot();

df['Volume'].plot()

title = 'TITLE'
ylabel = 'Y LABEL'
xlabel = 'X LABEL'

df['Close'].plot(figsize=(12,6), title=title)

""" Para adicionar labels x e y, precisa atribuir o
gráfico a uma variável, por convenção ax """

ax = df['Close'].plot(figsize=(12,6), title=title)

ax.autoscale(axis='both', tight=True) # sem espaço em branco na vertical e horizontal

ax.set(xlabel=xlabel, ylabel=ylabel)

# ---------------------

ax = df['Close'].plot(figsize=(12,6), title=title)

ax.autoscale(axis='y', tight=True) # sem espaço em branco na vertical

ax.set(xlabel=xlabel, ylabel=ylabel)

# ---------------------

""" Plotando apenas um ano. Forma 1 """

print(df['Close'])
print(df['Close']['2017-01-01':'2017-12-31'])

df['Close'].plot(figsize=(12,4))

df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4))

""" Plotando apenas um ano. Forma 2 """

df['Close'].plot(figsize=(12,4), xlim = ['2017-01-01','2017-12-31'])

""" Usando ylim """

df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4), ylim=[0,70])

df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4), ylim=[40,70])

""" Estilo da linha: ls """

df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4), ylim=[40,70], ls='--')

""" Cor da linha: c """

df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4), ylim=[40,70], ls='--', c='red')


""" Outras configurações """

import pandas as pd

pasta = caminho_base / 'Dados' / 'Cursos e Livros' / 'Python for time series (Udemy)' / 'Data'
df = pd.read_csv(pasta / 'starbucks.csv', index_col='Date', parse_dates=True)

df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60])

df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))

""" tirando o label do eixo x """

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

""" xticks
Agora, as datas estão igualmente espaçadas
Agora, não há mais marcação de cada novo mês
Agora, o espaçamento é por 1 semana"""

from matplotlib import dates

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))

""" formatando as datas"""

from matplotlib import dates

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(dates.DateFormatter('%a-%B-%d'))

""" minor axis """

from matplotlib import dates

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b')) #\n representa uma nova linha

""" grid """

from matplotlib import dates

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b')) #\n representa uma nova linha

ax.yaxis.grid(True)
ax.xaxis.grid(True)










