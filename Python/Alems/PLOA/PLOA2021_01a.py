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
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
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
    ########################### IPCA #########################################
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
    df_ipca.index.freq = 'MS'
    df_ipca['mês'] = df_ipca.index.month
    df_ipca['ano'] = df_ipca.index.year
    cond = df_ipca['mês'] == 10
    df_ipca = df_ipca.loc[cond,:]
    df_ipca.drop(['mês'], axis=1, inplace=True)
    ##########################################################################
    
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
    filtro.drop(['ano'], axis=1, inplace=True)
    
       
    return filtro
        

def evolucao_orcamento(competencia):
        
    df_alems = orc_orgao('Assembleia Legislativa', competencia)
    df_alems.rename(columns={'TOTAL_atualizado':'Alems'}, inplace=True)
    
    df_execut = orc_orgao('PODER EXECUTIVO', competencia)
    df_execut.rename(columns={'TOTAL_atualizado':'Executivo'}, inplace=True)
    
    df_jud = orc_orgao('PODER JUDICIÁRIO', competencia)
    df_jud.rename(columns={'TOTAL_atualizado':'Judiciário'}, inplace=True)
    
    df_mpe = orc_orgao('MINISTÉRIO PÚBLICO', competencia)
    df_mpe.rename(columns={'TOTAL_atualizado':'MPE'}, inplace=True)
    
    df_dp = orc_orgao('DEFENSORIA PÚBLICA', competencia)
    df_dp.rename(columns={'TOTAL_atualizado':'Defensoria'}, inplace=True)
    
    df_tce = orc_orgao('TRIBUNAL DE CONTAS', competencia)
    df_tce.rename(columns={'TOTAL_atualizado':'TCE'}, inplace=True)
    
    df_todos = df_alems.loc[:,['Competência', 'Alems']]
    df_todos = df_todos.merge(df_execut.loc[:,['Competência', 'Executivo']], how='left', left_on='Competência', right_on='Competência')
    df_todos = df_todos.merge(df_jud.loc[:,['Competência', 'Judiciário']], how='left', left_on='Competência', right_on='Competência')
    df_todos = df_todos.merge(df_mpe.loc[:,['Competência', 'MPE']], how='left', left_on='Competência', right_on='Competência')
    df_todos = df_todos.merge(df_dp.loc[:,['Competência', 'Defensoria']], how='left', left_on='Competência', right_on='Competência')
    df_todos = df_todos.merge(df_tce.loc[:,['Competência', 'TCE']], how='left', left_on='Competência', right_on='Competência')
    
    df_todos.set_index('Competência', inplace=True)
    return df_todos

df_poderes = evolucao_orcamento(2016)
df_poderes_M = df_poderes / 1_000_000
df_poderes_B = df_poderes / 1_000_000_000


pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    df_poderes_M.to_excel(writer, sheet_name='orcPoderesMilhoes', index=True)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    df_poderes_B.to_excel(writer, sheet_name='orcPoderesBilhoes', index=True)














from matplotlib import pyplot as plt
import numpy as np

fig1, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=False)

ax1.plot(df_poderes_M['MPE'], label='Ministério Público')
ax1.plot(df_poderes_M['Alems'], label='Assembleia Legislativa')
ax1.plot(df_poderes_M['TCE'], label='Tribunal de Contas')
ax1.plot(df_poderes_M['Defensoria'], label='Defensoria')

ax2.plot(df_poderes_B['Judiciário'], label='Poder Judiciário')
ax3.plot(df_poderes_B['Executivo'], label='Poder Executivo')

# Configuração de ax1
ax1.set_xticks(np.arange(2016,2022,1))
ax1.set_title('Alems, MPE, Defensoria e TCE', fontsize=18)
ax1.set_ylabel('Milhões de Reais')
ax1.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax1.grid(True)

# Configuração de ax2
ax2.set_xticks(np.arange(2016,2022,1))
ax2.set_title('Poder Judiciário', fontsize=18)
ax2.set_ylabel('Bilhões de Reais')
ax2.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax2.grid(True)

# Configuração de ax3
ax3.set_xticks(np.arange(2016,2022,1))
ax3.set_title('Poder Executivo', fontsize=18)
ax3.set_ylabel('Bilhões de Reais')
ax3.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax3.grid(True)


# Configurações gerais
#fig1.tight_layout()
cm = 1/2.54  # centimetros para polegadas
fig1.set_size_inches(20*cm, 40*cm)
fig1.show()

#pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
#fig1.savefig(pasta / 'figura.png')




print(np.arange(2014,2022,1))














