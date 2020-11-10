# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:32:04 2020

@author: pedro-salj
"""

globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

import pandas as pd
#################

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
rreo_rcl = processa_arquivos_zip(arquivo='2020b4.zip',
                                           caminho=pasta,
                                           pasta=False)


rreo_rcl['início'] = pd.to_datetime('2020/8/1', format='%Y/%m/%d')











data = pd.to_datetime(['2020/8/1'], format='%Y/%m/%d')
data.freq = 'MS'
mes = pd.Timedelta(1, unit ='MS')


# icms
cond1 = rreo_rcl['exercicio'] >= 2016
cond2 = rreo_rcl['Conta'].str.contains('icms', case=False)
cond3 = rreo_rcl['UF'] == 'MS'
cond = cond1 & cond2 & cond3
filtro = rreo_rcl.loc[cond, :]





cond1 = rreo_rcl['exercicio'] >= 2016
cond2 = rreo_rcl['Conta'].str.contains('RECEITA CORRENTE LÍQUIDA AJUSTADA PARA CÁLCULO DOS LIMITES DA DESPESA COM PESSOAL', case=False)
cond3 = rreo_rcl['UF'] == 'MS'
cond = cond1 & cond2 & cond3
filtro = rreo_rcl.loc[cond, :]

#--------------------------------------------------------------------------------------------
cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR>'
filtro.loc[cond1 & cond2,'mês'] = 8

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-1>'
filtro.loc[cond1 & cond2,'mês'] = 7

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-2>'
filtro.loc[cond1 & cond2,'mês'] = 6

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-3>'
filtro.loc[cond1 & cond2,'mês'] = 5

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-4>'
filtro.loc[cond1 & cond2,'mês'] = 4

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-5>'
filtro.loc[cond1 & cond2,'mês'] = 3

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-6>'
filtro.loc[cond1 & cond2,'mês'] = 2

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-7>'
filtro.loc[cond1 & cond2,'mês'] = 1

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-8>'
filtro.loc[cond1 & cond2,'mês'] = 12

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-9>'
filtro.loc[cond1 & cond2,'mês'] = 11

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-10>'
filtro.loc[cond1 & cond2,'mês'] = 10

cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR-11>'
filtro.loc[cond1 & cond2,'mês'] = 9
#--------------------------------------------------------------------------------------------

filtro.rename(columns={'exercicio':'year'}, inplace=True)



cond1 = filtro['bimestre'] == 4
cond2 = filtro['Coluna'] == '<MR>'
filtro.loc[cond1 & cond2,'month'] = 8
filtro['day'] = 1

filtro['data'] = pd.to_datetime(filtro[['year', 'month', 'day']])


cond1 = rreo_rcl['exercicio'] >= 2016
cond2 = rreo_rcl['Coluna'].str.contains('mr', case=False)
cond3 = rreo_rcl['UF'] == 'MS'
cond = cond1 & cond2 & cond3
filtro = rreo_rcl.loc[cond, :]



date = np.array(['2020-08-1', '2020-03-16', '2020-03-17'], dtype='datetime64[Y]')


import numpy as np

data = np.array(['2020-08-1'], dtype='datetime64[Y]')


import pandas as pd

data = pd.to_datetime(['2020/8/1'], format='%Y/%m/%d')
data.freq = 'MS'
mes = pd.Timedelta(1, unit ='MS')

from datetime import date
from dateutil.relativedelta import relativedelta

print(data)

print(data + relativedelta(months=+6))

import monthdelta

print(monthdelta(1))




# https://www.xspdf.com/resolution/53042314.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.tseries.offsets.DateOffset.html
print(data)
print(data + pd.DateOffset(months=1))























