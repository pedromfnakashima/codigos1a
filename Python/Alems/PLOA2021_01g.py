# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 07:35:04 2020

@author: pedro-salj
"""
globals().clear()
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')


import tabula
import numpy as np
import pandas as pd

#############
# PLOA 2021 #
#############

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = tabula.read_pdf(pasta / 'cadernoPLOA_2021.pdf', pages=[18])[0]

#

df1 = df.loc[3:6, ['Unnamed: 0','Unnamed: 1'] ]
df1.rename(columns={'Unnamed: 0':'Função', 'Unnamed: 1':'Valor'}, inplace=True)

df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2021
df1['Submissão'] = 2020
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = df1.copy()

############
# LOA 2020 #
############

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = tabula.read_pdf(pasta / 'LOA 2020.pdf', pages=[7])[1]

df1 = df.loc[2:5, ['Unnamed: 0','Unnamed: 1'] ]

df1.rename(columns={'Unnamed: 0':'Função', 'Unnamed: 1':'Valor'}, inplace=True)
df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2020
df1['Submissão'] = 2019
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)

############
# LOA 2019 #
############

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = tabula.read_pdf(pasta / 'LOA 2019.pdf', pages=[4])[0]

df1 = df.loc[3:6, ['Unnamed: 1','Unnamed: 2'] ]
df1.rename(columns={'Unnamed: 1':'Função', 'Unnamed: 2':'Valor'}, inplace=True)
df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2019
df1['Submissão'] = 2018
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)

############
# LOA 2018 #
############

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_excel(pasta / 'LOA 2018-DespesasCorrentes.xlsx', sheet_name='Planilha1', skiprows=0)

df1['Competência'] = 2018
df1['Submissão'] = 2017

desp_funções = desp_funções.append(df1)

############
# LOA 2017 #
############
import pandas as pd

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_csv(pasta / 'LOA 2017-DespesasCorrentes.csv', delimiter=';')

df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2017
df1['Submissão'] = 2016
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)

############
# LOA 2016 #
############
import pandas as pd

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_csv(pasta / 'LOA 2016-DespesasCorrentes.csv', delimiter=';')

df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2016
df1['Submissão'] = 2015
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)
desp_funções.sort_values(['Competência', 'Função'], inplace=True)

############################################
######### EXPORTA PARA EXCEL ###############
############################################

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'LOAs - Séries.xlsx', mode='a', engine="openpyxl") as writer:  
    desp_funções.to_excel(writer, sheet_name='Desp_Correntes', index=False)

####################################################
######### DEFLACIONA E GERA GRÁFICOS ###############
####################################################

########################### IPCA #########################################
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
df_ipca['mês'] = df_ipca.index.month
df_ipca['ano'] = df_ipca.index.year
cond = df_ipca['mês'] == 10
df_ipca = df_ipca.loc[cond,:]
df_ipca.drop(['mês'], axis=1, inplace=True)
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
##########################################################################

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs - Séries.xlsx', sheet_name='Desp_Correntes', skiprows=0)

df = df.merge(df_ipca, how='left', left_on='Submissão', right_on='ano')

df['Valor_d'] = df['Valor'] * df['deflator']

# DESPESAS CORRENTES

cond = df['Função'].str.contains('correntes', case=False)
cond = df['Função'] == 'Despesas Correntes'
filtro = df.loc[cond, ['Competência','Função','Valor_d']]
filtro = df.loc[cond, ['Competência', 'Valor_d']]
filtro.rename(columns={'Valor_d':'Despesas Correntes'}, inplace=True)

despesas_correntes = filtro.copy()

# JUROS E ENCARGOS DA DÍVIDA

cond = df['Função'].str.contains('correntes', case=False)
cond = df['Função'] == 'Juros e Encargos da Dívida'
filtro = df.loc[cond, ['Competência','Função','Valor_d']]
filtro = df.loc[cond, ['Competência', 'Valor_d']]
filtro.rename(columns={'Valor_d':'Juros e Encargos da Dívida'}, inplace=True)

despesas_correntes = despesas_correntes.merge(filtro, how='left', left_on='Competência', right_on='Competência')

# JUROS E ENCARGOS DA DÍVIDA

cond = df['Função'].str.contains('correntes', case=False)
cond = df['Função'] == 'Pessoal e Encargos Sociais'
filtro = df.loc[cond, ['Competência','Função','Valor_d']]
filtro = df.loc[cond, ['Competência', 'Valor_d']]
filtro.rename(columns={'Valor_d':'Pessoal e Encargos Sociais'}, inplace=True)

despesas_correntes = despesas_correntes.merge(filtro, how='left', left_on='Competência', right_on='Competência')

despesas_correntes.set_index('Competência', inplace=True)

despesas_correntes_M = despesas_correntes / 1_000_000
despesas_correntes_B = despesas_correntes / 1_000_000_000













































