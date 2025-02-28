# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:29:50 2020

@author: pedro-salj
"""

#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
os.chdir(caminho_wd)
#import numpy as np
#import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

import requests
import pandas as pd
url = "https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204"
r = requests.get(url)
j = r.json()
df = pd.DataFrame.from_dict(j)

# ---------------------------------------

df['year'] = df['D3C'].str.slice(0,4)
df['month'] = df['D3C'].str.slice(4,6)
df['day'] = '01'
df['dt'] = pd.to_datetime(df[['year', 'month', 'day']],errors='coerce')
df.drop(['year','month','day'],axis=1,inplace=True)

def retorna_código_e_desc(texto):
    import re
    matches = re.search('^\d+', texto)
    é_índice = bool(re.match('índice', texto, re.IGNORECASE))
    posição_início = texto.find('.') + 1 # posição do ponto mais 1
    if matches != None:
        #print(matches.group(0))
        cód = matches.group(0)
        str_texto = texto[posição_início:]
    elif é_índice == True:
        #print('é índice')
        cód = '0'
        str_texto = texto
    else:
        #print('outra coisa')
        cód = ''
        str_texto = ''
    return cód, str_texto

for index_linha, linha in df.iterrows():
    #print(linha[nome_antigo_categoria_Grupo])
    código, descrição = retorna_código_e_desc(linha['D4N'])
    #print(cód1)
    df.loc[index_linha,'código'] = código
    df.loc[index_linha,'descrição'] = descrição

# Classifica as entradas como Geral, Grupo, Subgrupo, Item, Subitem
cond1 = df['código'] == '0'
cond = cond1
df.loc[cond1,'categoria'] = 'Geral'

cond1 = df['código'].str.len() == 1
cond2 = df['código'] != '0'
cond = cond1 & cond2
df.loc[cond,'categoria'] = 'Grupo'

cond1 = df['código'].str.len() == 2
df.loc[cond1,'categoria'] = 'Subgrupo'

cond1 = df['código'].str.len() == 4
df.loc[cond1,'categoria'] = 'Item'

cond1 = df['código'].str.len() == 7
df.loc[cond1,'categoria'] = 'Subitem'

# Tabelas com as descrições e códigos

li_categorias = ['Grupo','Subgrupo','Item','Subitem']

# GRUPOS

dic_categorias = {}

for categoria in li_categorias:
    #categoria = 'Subgrupo'
    
    cond1 = df['categoria'] == categoria
    df_categoria = df.loc[cond1,:]
    
    df_categoria = df_categoria.groupby(['código']).head(1)
    
    dic_categorias[categoria] = df_categoria
    
    dic_categorias[categoria] = dic_categorias[categoria].loc[:,['código','descrição']]


dic_categorias2 = dic_categorias.copy()
dic_categorias2['Grupo']['código2'] = dic_categorias2['Grupo']['código'] + '000000'
dic_categorias2['Subgrupo']['código2'] = dic_categorias2['Subgrupo']['código'] + '00000'
dic_categorias2['Item']['código2'] = dic_categorias2['Item']['código'] + '000'
dic_categorias2['Subitem']['código2'] = dic_categorias2['Subitem']['código']

df_CódLongo = dic_categorias2['Grupo'].copy()
df_CódLongo = df_CódLongo.append(dic_categorias2['Subgrupo'])
df_CódLongo = df_CódLongo.append(dic_categorias2['Item'])
df_CódLongo = df_CódLongo.append(dic_categorias2['Subitem'])

df_CódLongo['código2'] = df_CódLongo['código2'].astype('str')

# DF com correspondências

arq_nome = 'IPCA - Divisão por Categorias.xlsx'
pasta = caminho_base / 'Dados' / 'BD firjan' / 'Inflação'
df = pd.read_excel(pasta / arq_nome, sheet_name='IPCA - Variação', skiprows=0)
print(df.dtypes)
df.rename(mapper={'Unnamed: 0':'CNCA','Unnamed: 1':'DNDS','Unnamed: 2':'Código'},axis=1,inplace=True)

df = df.iloc[4:,0:3]
df.dropna(thresh=2,inplace=True)
df.rename(mapper={'Código':'código2'},axis=1,inplace=True)

df['código2'] = df['código2'].astype('str')

print(df.dtypes)
print(df_CódLongo.dtypes)

df_merge = df.merge(df_CódLongo,how='left',left_on='código2',right_on='código2')

# Criar 4 DFs: Variação, Peso, Contribuição, Índice

















cond1 = df['D4N'] == 'Índice geral'
filtro = df.loc[cond1,:]

##########################################################################################################
##########################################################################################################
##########################################################################################################
