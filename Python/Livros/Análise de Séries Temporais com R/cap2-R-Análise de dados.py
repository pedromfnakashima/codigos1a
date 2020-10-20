# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 08:14:05 2020

@author: pedro
"""

globals().clear()

from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    print('Logado de casa')
    caminho = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('Logado da salj-alems')
    caminho = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

# https://www.statsmodels.org/devel/datasets/statsmodels.datasets.get_rdataset.html#statsmodels.datasets.get_rdataset
# https://vincentarelbundock.github.io/Rdatasets/articles/data.html

import pandas as pd

df = pd.read_csv(caminho / 'Cursos e Livros' / 'Análise de Séries Temporais com R' / 'cap2-HW' / 'elecequip.csv',
                       encoding = 'latin',
                       delimiter = ';',
                       decimal = ",")

df = df.assign(Date=pd.to_datetime(df[['year', 'month']].assign(day=1)))

df['indice'] = pd.PeriodIndex(df['Date'], freq='M')

df.index = df['Date']



df.drop(['Date','indice','year','month'], axis='columns', inplace=True)

print(df.index)

df['elecequip'].plot(linewidth=0.5);

from statsmodels.tsa.seasonal import seasonal_decompose

decomp = seasonal_decompose(df.elecequip, model='additive')

decomp.plot()








series_monthly = pd.Series([1, 2, 3],
                           pd.DatetimeIndex(['2011-12', '2012-01', '2012-02']))






