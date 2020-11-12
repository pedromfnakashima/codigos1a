# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:55:19 2020

@author: pedro
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

# PEGAR O DEFLATOR MENSAL
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
df_ipca = df_ipca.loc[:,['deflator']]
df_ipca.reset_index(inplace=True)

uf = 'MS'

##### 2019
pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2019q2.zip',
                           caminho=pasta,
                           pasta=False)

df['year'] = df['mês'].dt.year
cond1 = df['UF'] == uf
cond2 = df['year'] == 2019
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond = cond1 & cond2 & cond3
filtro = df.loc[cond,:]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2019 = filtro['Valor_d'].sum()

##### 2020
pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                           caminho=pasta,
                           pasta=False)

df['year'] = df['mês'].dt.year
cond1 = df['UF'] == uf
cond2 = df['year'] == 2020
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond = cond1 & cond2 & cond3
filtro = df.loc[cond,:]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2020 = filtro['Valor_d'].sum()





####################################################################
##################### MONTAR O LOOPING #############################
####################################################################

def variacao_g_pessoal():
    
    # PEGAR O DEFLATOR MENSAL
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
    df_ipca.index.freq = 'MS'
    atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
    df_ipca['deflator'] = atual / df_ipca['Índice']
    df_ipca = df_ipca.loc[:,['deflator']]
    df_ipca.reset_index(inplace=True)
    
    ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
     'SE', 'PB', 'MA', 'CE', 'AL', 'RJ', 'PI', 'AC', 'RS', 'DF', 'RR', 'MG', 'RN']
    
    df_somas = pd.DataFrame(columns=['UF','soma_2019', 'soma_2020'])
    
    for index, uf in enumerate(ufs):
        #print(index, uf)
        ##### 2019
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
        df = processa_arquivos_zip(arquivo='2019q2.zip',
                                   caminho=pasta,
                                   pasta=False)
        
        df['year'] = df['mês'].dt.year
        cond1 = df['UF'] == uf
        cond2 = df['year'] == 2019
        cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
        cond = cond1 & cond2 & cond3
        filtro = df.loc[cond,:]
        filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
        filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
        soma_2019 = filtro['Valor_d'].sum()
        
        ##### 2020
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
        df = processa_arquivos_zip(arquivo='2020q2.zip',
                                   caminho=pasta,
                                   pasta=False)
        
        df['year'] = df['mês'].dt.year
        cond1 = df['UF'] == uf
        cond2 = df['year'] == 2020
        cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
        cond = cond1 & cond2 & cond3
        filtro = df.loc[cond,:]
        filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
        filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
        soma_2020 = filtro['Valor_d'].sum()
        
        df_somas.loc[index,'UF'] = uf
        df_somas.loc[index,'soma_2019'] = soma_2019
        df_somas.loc[index,'soma_2020'] = soma_2020
        
        
        df_somas['mult'] = df_somas['soma_2020'] / df_somas['soma_2019']
        df_somas.sort_values(by=['mult'], inplace=True)
        df_somas['var_percent'] = ((df_somas['soma_2020'] - df_somas['soma_2019']) / df_somas['soma_2019']) * 100
        
    return df_somas


df_somas = variacao_g_pessoal()