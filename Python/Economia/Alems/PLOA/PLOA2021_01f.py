# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:05:01 2020

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
#################

# PEGAR O DEFLATOR MENSAL
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
df_ipca = df_ipca.loc[:,['deflator']]
df_ipca.reset_index(inplace=True)

# Rodar antes o arquivo junta_siconfi_01c.py
pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
df = processa_arquivos_zip(arquivo='2020b4.zip',
                                           caminho=pasta,
                                           pasta=False)
df['year'] = df['mês'].dt.year
cond1 = df['year'] == 2020
cond2 = df['Conta'].str.contains('impostos, taxas', case=False)
cond2 = df['Conta'] == 'Impostos, Taxas e Contribuições de Melhoria'
cond3 = df['UF'] == 'MS'
cond = cond1 & cond2 & cond3
filtro = df.loc[cond,['mês','Valor']]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2020 = filtro['Valor_d'].sum()



pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
df = processa_arquivos_zip(arquivo='2019b4.zip',
                                           caminho=pasta,
                                           pasta=False)
df['year'] = df['mês'].dt.year
cond1 = df['year'] == 2019
cond2 = df['Conta'].str.contains('impostos, taxas', case=False)
cond2 = df['Conta'] == 'Impostos, Taxas e Contribuições de Melhoria'
cond3 = df['UF'] == 'MS'
cond = cond1 & cond2 & cond3
filtro = df.loc[cond,['mês','Valor']]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2019 = filtro['Valor_d'].sum()

print(df['UF'].unique())

ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
 'SE', 'PB', 'MA', 'CE', 'AL', 'RJ', 'PI', 'AC', 'RS', 'DF', 'RR', 'MG', 'RN']

print(len(ufs))


print(soma_2020/soma_2019)

df_somas = pd.Data

df_somas = pd.DataFrame(columns=['UF','soma_2019', 'soma_2020'])

####################################################################
##################### MONTAR O LOOPING #############################
####################################################################

def variacao_receita():
    
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
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
        df = processa_arquivos_zip(arquivo='2019b4.zip',
                                                   caminho=pasta,
                                                   pasta=False)
        df['year'] = df['mês'].dt.year
        cond1 = df['year'] == 2019
        cond2 = df['Conta'].str.contains('impostos, taxas', case=False)
        cond2 = df['Conta'] == 'Impostos, Taxas e Contribuições de Melhoria'
        cond3 = df['UF'] == uf
        cond = cond1 & cond2 & cond3
        filtro = df.loc[cond,['mês','Valor']]
        filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
        filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
        soma_2019 = filtro['Valor_d'].sum()
        
        ###### 2020
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
        df = processa_arquivos_zip(arquivo='2020b4.zip',
                                                   caminho=pasta,
                                                   pasta=False)
        df['year'] = df['mês'].dt.year
        cond1 = df['year'] == 2020
        cond2 = df['Conta'].str.contains('impostos, taxas', case=False)
        cond2 = df['Conta'] == 'Impostos, Taxas e Contribuições de Melhoria'
        cond3 = df['UF'] == uf
        cond = cond1 & cond2 & cond3
        filtro = df.loc[cond,['mês','Valor']]
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


df_somas = variacao_receita()

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    df_somas.to_excel(writer, sheet_name='VariaçãoReceitas', index=False)














