# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:36:51 2020

@author: Pedro
"""
globals().clear()

# https://www.statsmodels.org/devel/datasets/statsmodels.datasets.get_rdataset.html#statsmodels.datasets.get_rdataset
# https://vincentarelbundock.github.io/Rdatasets/articles/data.html

from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('Logado de casa')
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('Logado da salj-alems')
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

import pandas as pd


ebola = pd.read_csv(caminho / 'Cursos e Livros' / 'Pandas for everyone' / 'data' / 'country_timeseries.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".")

print(ebola.iloc[:5,:5])
print(ebola.info())

ebola['date_dt'] = pd.to_datetime(ebola['Date'])

print(ebola.info())


print(ebola.loc[1,'date_dt'].year)
print(ebola.loc[1,'date_dt'].month)

ebola['ano'] = ebola['date_dt'].dt.year
ebola['mes'] = ebola['date_dt'].dt.month

print(ebola.info())

print(ebola.iloc[-5:,:5])

print(ebola['date_dt'].min())

ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()

print(ebola[['Date','Day','outbreak_d']].head())
print(ebola[['Date','Day','outbreak_d']].tail())

print(ebola.info())

### 11.7 Datetime Methods

banks = pd.read_csv(caminho / 'Cursos e Livros' / 'Pandas for everyone' / 'data' / 'banklist.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".",
                       parse_dates = [5,6])

print(banks.head())
print(banks.info())

banks['closing_quarter'], banks['closing_year'] = \
    (banks['Closing Date'].dt.quarter,
     banks['Closing Date'].dt.year)

# Quantos bancos fecharam em cada ano

closing_year = banks.groupby(['closing_year']).size()

# Quantos bancos fecharam em cada trimestre do ano

closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()

print(closing_year_q.index)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()

fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()


# 11.8 Getting Stock Data

import pandas_datareader as pdr

tesla = pdr.get_data_yahoo('TSLA')

print(tesla.info())

tesla = pd.read_csv(caminho / 'Cursos e Livros' / 'Pandas for everyone' / 'data' / 'tesla_stock_yahoo.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".",
                       parse_dates = [0])


# 11.9 Subsetting Data Based on Dates

print(tesla.loc[(tesla.Date.dt.year == 2010) & \
                (tesla.Date.dt.month == 6)])

print(tesla.tail())

# 11.9.1 The DatetimeIndex Object

tesla.index = tesla['Date']

print(tesla.index)

print(tesla['2015'].iloc[:5,:5])

print(tesla['2010-06'].iloc[:,:5])

tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()

tesla.index = tesla['ref_date']

print(tesla.iloc[:5,:5])

print(tesla['0 day':'5 day'].iloc[:5,:5])

# 11.10 Date Ranges

ebola = pd.read_csv(caminho / 'Cursos e Livros' / 'Pandas for everyone' / 'data' / 'country_timeseries.csv',
                       encoding = 'latin',
                       delimiter = ',',
                       decimal = ".",
                       parse_dates = [0])

print(ebola.iloc[:5,:5])

print(ebola.iloc[-5:,:5])

head_range = pd.date_range(start='2014-12-31', end='2015-01-05')

print(head_range)

ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']

ebola_5 = ebola_5.reindex(head_range)

print(pd.date_range('2017-01-01', '2017-01-07', freq='B'))

print(pd.date_range('2017-01-01', '2017-01-07', freq='2B'))

# Primeira quinta de cada mês
print(pd.date_range('2017-01-01', '2017-12-31', freq='WOM-1THU'))

# Terceira sexta de cada mês
print(pd.date_range('2017-01-01', '2017-12-31', freq='WOM-3FRI'))

# 11.11 Shifting Values

import matplotlib.pyplot as plt
ebola.index = ebola['Date']

#pág 230; posição 9163

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
plt.plot()



fig, ax1 = plt.subplots()
ax1 = ebola.plot(ax=ax1)





fig, ax = plt.subplots()
ax = ebola.plot(ax=ax)
ax.legend(fontsize=7,
          loc='upper left',
          borderaxespad=0.5)
plt.show()
















