# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:49:45 2020

@author: pedro

http://www.sefaz.ms.gov.br/loa-leis-orcamentarias-anuais/


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

######################################

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_excel(pasta / 'LOAs - Séries.xlsx', sheet_name='Desp_Tot_Orgão', skiprows=0, na_values=['-'])

'''
1. Evolução do orçamento de cada poder, em valores atuais.
'''

import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_excel(pasta / 'LOAs - Séries.xlsx', sheet_name='Desp_Tot_Orgão', skiprows=0, na_values=['-'])
df1['Submissão'] = df1['Competência'] - 1


orgao = 'Assembleia Legislativa'

cond = df1['Órgão'] == orgao
filtro = df1.loc[cond,:]

filtro.drop(['Poder', 'Órgão'], axis=1, inplace=True)

filtro = filtro.merge(df_ipca, how='left', left_on='Submissão', right_on='ano')

atual = filtro.loc[filtro.index.max(), 'Índice']
filtro['deflator'] = atual / filtro['Índice']

filtro['TOTAL_atualizado'] = filtro['TOTAL'] * filtro['deflator']

filtro.drop(['ano', 'mês'], axis=1, inplace=True)

##########################################################################################################



def orc_orgao(orgao, competencia):
        
    import pandas as pd
    
    pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
    df1 = pd.read_excel(pasta / 'LOAs - Séries.xlsx', sheet_name='Desp_Tot_Orgão', skiprows=0, na_values=['-'])
    #df1['Submissão'] = df1['Competência'] - 1
    
    #orgao = 'Assembleia Legislativa'
    #orgao = 'PODER EXECUTIVO'
    #orgao = 'DEFENSORIA PÚBLICA'
    #competencia = 2016
    
    if orgao == 'PODER EXECUTIVO' or orgao == 'PODER JUDICIÁRIO' or orgao == 'MINISTÉRIO PÚBLICO':
        cond1 = df1['Competência'] >= competencia
        cond2 = df1['Poder'] == orgao
        cond3 = ~ df1['Órgão'].str.contains('defensoria', case=False)
        filtro = df1.loc[cond1 & cond2 & cond3,:]
        filtro = filtro.groupby(['Competência'])['TOTAL'].sum().to_frame()
        filtro.reset_index(inplace=True)
        
        
    elif orgao == 'DEFENSORIA PÚBLICA':
        cond1 = df1['Competência'] >= competencia
        cond2 = df1['Órgão'].str.contains('defensoria', case=False)
        filtro = df1.loc[cond1 & cond2,:]
        filtro = filtro.groupby(['Competência'])['TOTAL'].sum().to_frame()
        filtro.reset_index(inplace=True)

    elif orgao == 'TRIBUNAL DE CONTAS':
        cond1 = df1['Competência'] >= competencia
        cond2 = df1['Órgão'].str.contains('tribunal de contas', case=False)
        filtro = df1.loc[cond1 & cond2,:]
        filtro = filtro.groupby(['Competência'])['TOTAL'].sum().to_frame()
        filtro.reset_index(inplace=True)
    else:
        cond1 = df1['Competência'] >= competencia
        cond2 = df1['Órgão'] == orgao
        filtro = df1.loc[cond1 & cond2,:]
        filtro.drop(['Poder', 'Órgão'], axis=1, inplace=True)

        
    filtro['Submissão'] = filtro['Competência'] - 1
    filtro = filtro.merge(df_ipca, how='left', left_on='Submissão', right_on='ano')
    atual = filtro.loc[filtro.index.max(), 'Índice']
    filtro['deflator'] = atual / filtro['Índice']
    filtro['TOTAL_atualizado'] = filtro['TOTAL'] * filtro['deflator']
    filtro['TOTAL_atualizado_milhões'] = filtro['TOTAL_atualizado'] / 1_000_000
    filtro['TOTAL_atualizado_bilhões'] = filtro['TOTAL_atualizado'] / 1_000_000_000
    filtro.drop(['ano', 'mês'], axis=1, inplace=True)
    
       
    return filtro
        

df_alems = orc_orgao('Assembleia Legislativa', 2016)
df_execut = orc_orgao('PODER EXECUTIVO', 2016)
df_jud = orc_orgao('PODER JUDICIÁRIO', 2016)
df_mpe = orc_orgao('MINISTÉRIO PÚBLICO', 2016)
df_dp = orc_orgao('DEFENSORIA PÚBLICA', 2016)
df_tce = orc_orgao('TRIBUNAL DE CONTAS', 2016)








df_alems.set_index('Competência', inplace=True)
df_alems['TOTAL_atualizado_milhões'].plot()

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

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
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

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
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

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
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

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
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

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_csv(pasta / 'LOA 2016-DespesaPorFunção.csv', delimiter=';')

df1['Valor'] = df1['Valor'].str.replace('.','').str.replace(',','.')
df1['Competência'] = 2016
df1['Submissão'] = 2015
df1['Valor'] = pd.to_numeric(df1['Valor'])

desp_funções = desp_funções.append(df1)

desp_funções = desp_funções.merge(df_ipca, how='left', left_on='Submissão', right_on='ano')

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
































