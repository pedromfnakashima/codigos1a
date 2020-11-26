# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:20:24 2020

@author: pedro
"""

globals().clear()
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')



##########################################################################################################
'''
2. 
Orçamentos com educação, saúde, pessoal, ano a ano
'''
##########################################################################################################

#############
# PLOA 2021 #
#############

import tabula
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = tabula.read_pdf(pasta / 'cadernoPLOA_2021.pdf', pages=[21])[0]

#

df1 = df.loc[2:21, ['Unnamed: 0','Unnamed: 1'] ]
df1.rename(columns={'Unnamed: 0':'Função', 'Unnamed: 1':'Valor'}, inplace=True)
df2 = df.loc[22:27, ['10 - Fiscal   20 - Seguridade','Unnamed: 0'] ]
df2.rename(columns={'10 - Fiscal   20 - Seguridade':'Função', 'Unnamed: 0':'Valor'}, inplace=True)
df1 = df1.append(df2)
df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2021
df1['Submissão'] = 2020
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = df1.copy()

############
# LOA 2020 #
############

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = tabula.read_pdf(pasta / 'LOA 2020.pdf', pages=[10])[1]

df1 = df.loc[2:27, ['Unnamed: 0','Unnamed: 1'] ]
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
df = tabula.read_pdf(pasta / 'LOA 2019.pdf', pages=[7])[0]

df1 = df.loc[2:27, ['Unnamed: 0','Unnamed: 1'] ]
df1.rename(columns={'Unnamed: 0':'Função', 'Unnamed: 1':'Valor'}, inplace=True)
df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2019
df1['Submissão'] = 2018
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)

############
# LOA 2018 #
############

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = tabula.read_pdf(pasta / 'LOA 2018.pdf', pages=[7])[0]

df['Função'] = df['Unnamed: 1'].str.extract('([A-Z].+)', expand=True)
df['Valor'] = df['Unnamed: 5']

df1 = df.loc[2:27, ['Função','Valor'] ]

df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2018
df1['Submissão'] = 2017
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)

############
# LOA 2017 #
############
import pandas as pd

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_csv(pasta / 'LOA 2017-DespesaPorFunção.csv', delimiter=';')

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
df1 = pd.read_csv(pasta / 'LOA 2016-DespesaPorFunção.csv', delimiter=';')

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
    desp_funções.to_excel(writer, sheet_name='Desp_Funções', index=False)










#####################

desp_função = desp_funções.copy()

cond = desp_função['Função'] == 'EDUCAÇÃO'
desp_função = desp_função.loc[cond, :]
desp_função.drop(['ano'], axis=1, inplace=True)
desp_função.set_index('Competência', inplace=True)
desp_função.sort_index(axis=0, inplace=True)

desp_função.index.freq = 'AS'

atual = desp_função.loc[desp_função.index.max(), 'índice']
desp_função['deflator'] = atual / desp_função['índice']
desp_função['Valor_Deflacionado'] = desp_função['Valor'] * desp_função['deflator']

desp_função['Valor_Deflacionado'].plot()











#####################

def serie_loa_atualizada(serie):
    
    desp_função = desp_funções.copy()
    
    cond = desp_função['Função'] == serie
    desp_função = desp_função.loc[cond, :]
    desp_função.drop(['ano'], axis=1, inplace=True)
    desp_função.set_index('Competência', inplace=True)
    desp_função.sort_index(axis=0, inplace=True)
    
    desp_função.index.freq = 'AS'
    
    atual = desp_função.loc[desp_função.index.max(), 'índice']
    desp_função['deflator'] = atual / desp_função['índice']
    desp_função['Valor_Deflacionado'] = desp_função['Valor'] * desp_função['deflator']
    
    return desp_função

df_educ = serie_loa_atualizada('EDUCAÇÃO')
df_jud = serie_loa_atualizada('JUDICIÁRIA')



df_jud['Valor_Deflacionado'].plot()






'''

'''




'''

'''






'''

'''








































