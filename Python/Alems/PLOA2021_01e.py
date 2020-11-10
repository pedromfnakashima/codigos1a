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
df = processa_arquivos_zip(arquivo='2020b4.zip',
                                           caminho=pasta,
                                           pasta=False)
range_max = 7
multiplicador = 2

for num_per in list(range(1,range_max)):
    cond = df['periodo'] == num_per
    df.loc[cond, 'mes_final_periodo'] = num_per * multiplicador
df.rename(columns={'exercicio':'year','mes_final_periodo':'month'}, inplace=True)
df['day'] = 1
df['data_inicio_periodo'] = pd.to_datetime(df[['year', 'month', 'day']])
df.rename(columns={'year':'exercicio'}, inplace=True)
df.drop(['month','day'],axis=1,inplace=True)
cond = df['Coluna'] == '<MR>'
df.loc[cond, 'mês'] = df['data_inicio_periodo']
for num in list(range(1,12)):
    str1 = f'<MR-{num}>'
    cond = df['Coluna'] == str1
    df.loc[cond, 'mês'] = df['data_inicio_periodo'] - pd.DateOffset(months=num)
del df['data_inicio_periodo']









# ------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
df = processa_arquivos_zip(arquivo='2020q1.zip',
                                           caminho=pasta,
                                           pasta=False)

cond = df['Coluna'].str.contains('MR', case=True)
soma = cond.sum()
print(soma)


pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                                           caminho=pasta,
                                           pasta=False)

cond = df['Coluna'].str.contains('MR', case=True)
soma = cond.sum()
print(soma)


cond1 = df['exercicio'] >= 2016
cond2 = df['Conta'].str.contains('DESPESA BRUTA COM PESSOAL', case=False)
cond3 = df['UF'] == 'MS'
cond4 = df['PODER'].str.contains('Executivo', case=False)
cond = cond1 & cond2 & cond3 & cond4
filtro = df.loc[cond, :]






pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                                           caminho=pasta,
                                           pasta=False)


range_max = 4
multiplicador = 4

for num_per in list(range(1,range_max)):
    cond = df['periodo'] == num_per
    df.loc[cond, 'mes_final_periodo'] = num_per * multiplicador

df.rename(columns={'exercicio':'year','mes_final_periodo':'month'}, inplace=True)
df['day'] = 1
df['data_inicio_periodo'] = pd.to_datetime(df[['year', 'month', 'day']])
df.rename(columns={'year':'exercicio'}, inplace=True)
df.drop(['month','day'],axis=1,inplace=True)

cond = df['Coluna'] == '<MR>'
df.loc[cond, 'mês'] = df['data_inicio_periodo']

for num in list(range(1,12)):
    str1 = f'<MR-{num}>'
    cond = df['Coluna'] == str1
    df.loc[cond, 'mês'] = df['data_inicio_periodo'] - pd.DateOffset(months=num)

del df['data_inicio_periodo']






