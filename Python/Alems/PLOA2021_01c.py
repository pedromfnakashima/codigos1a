# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:11:35 2020

@author: pedro
"""

globals().clear()
import os
import pandas as pd
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')


def desp_loa_funções():
        
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
    # Deflator
    atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
    df_ipca['Deflator'] = atual / df_ipca['Índice']
    ##########################################################################

    pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
    df_desp_funções = pd.read_excel(pasta / 'LOAs - Séries.xlsx', sheet_name='Desp_Funções', skiprows=0)
    
    ##########################################################################
    # SAÚDE
    cond1 = df_desp_funções['Função'] == 'SAÚDE'
    filtro = df_desp_funções.loc[cond1, ['Competência', 'Submissão', 'Valor']]
    filtro.rename(columns={'Valor':'Saúde'}, inplace=True)
    ##########################################################################
    df_todos = filtro.copy()
    ##########################################################################
    # EDUCAÇÃO
    cond1 = df_desp_funções['Função'] == 'EDUCAÇÃO'
    filtro = df_desp_funções.loc[cond1, ['Competência', 'Valor']]
    filtro.rename(columns={'Valor':'Educação'}, inplace=True)
    df_todos = df_todos.merge(filtro, how='left', left_on='Competência', right_on='Competência')
    ##########################################################################
    # SEGURANÇA PÚBLICA
    cond1 = df_desp_funções['Função'] == 'SEGURANÇA PUBLICA'
    filtro = df_desp_funções.loc[cond1, ['Competência', 'Valor']]
    filtro.rename(columns={'Valor':'Segurança'}, inplace=True)
    df_todos = df_todos.merge(filtro, how='left', left_on='Competência', right_on='Competência')
    ##########################################################################
    # TRABALHO
    cond1 = df_desp_funções['Função'] == 'TRABALHO'
    filtro = df_desp_funções.loc[cond1, ['Competência', 'Valor']]
    filtro.rename(columns={'Valor':'Trabalho'}, inplace=True)
    df_todos = df_todos.merge(filtro, how='left', left_on='Competência', right_on='Competência')
    ##########################################################################
    # HABITAÇÃO
    cond1 = df_desp_funções['Função'] == 'HABITAÇÃO'
    filtro = df_desp_funções.loc[cond1, ['Competência', 'Valor']]
    filtro.rename(columns={'Valor':'Habitação'}, inplace=True)
    df_todos = df_todos.merge(filtro, how='left', left_on='Competência', right_on='Competência')
    ##########################################################################
    df_todos = df_todos.merge(df_ipca, how='left', left_on='Submissão', right_on='ano')
    df_todos.drop(['ano'], axis=1, inplace=True)
    df_todos['Saúde_d'] = df_todos['Saúde'] * df_todos['Deflator']
    df_todos['Educação_d'] = df_todos['Educação'] * df_todos['Deflator']
    df_todos['Segurança_d'] = df_todos['Segurança'] * df_todos['Deflator']
    df_todos['Trabalho_d'] = df_todos['Trabalho'] * df_todos['Deflator']
    df_todos['Habitação_d'] = df_todos['Habitação'] * df_todos['Deflator']
    ##########################################################################
    df_todos.drop(['Índice','Deflator','Submissão','Saúde','Educação','Segurança','Trabalho','Habitação'], axis=1, inplace=True)
    df_todos.set_index('Competência', inplace=True)
    ##########################################################################
    return df_todos

df_loa_desp_funções = desp_loa_funções()
df_loa_desp_funções_M = df_loa_desp_funções / 1_000_000
df_loa_desp_funções_B = df_loa_desp_funções / 1_000_000_000


pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    df_loa_desp_funções_M.to_excel(writer, sheet_name='loa_desp_funç_M', index=True)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    df_loa_desp_funções_B.to_excel(writer, sheet_name='loa_desp_funç_B', index=True)









df_loa_desp_funções_B['Educação_d'].plot()



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


