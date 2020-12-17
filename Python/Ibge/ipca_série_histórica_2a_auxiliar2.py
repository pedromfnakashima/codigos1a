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
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################
'''
Períodos e tabelas
2938: julho/2006 até dezembro/2011 (link: https://sidra.ibge.gov.br/Tabela/2938)
1419: janeiro/2012 até dezembro/2019 (link: https://sidra.ibge.gov.br/tabela/1419)
7060: a partir de janeiro/2020 (link: https://sidra.ibge.gov.br/tabela/7060)
'''

# DF com correspondências

arq_nome = 'IPCA - Divisão por CategoriasANTIGO.xlsx'
pasta = caminho_base / 'Dados' / 'BD firjan' / 'Inflação'
df = pd.read_excel(pasta / arq_nome, sheet_name='Classificação', skiprows=0, dtype={'código':'str'})

print(df.dtypes)

df_class_jul2006_dez2011 = df.copy()

cond1 = df_class_jul2006_dez2011['código'] =='1111004'
filtro = df_class_jul2006_dez2011.loc[cond1,:]



# -------------------------------------------------------------------------------------------------------------------

arq_nome = 'IPCA - Divisão por Categorias.xlsx'
pasta = caminho_base / 'Dados' / 'BD firjan' / 'Inflação'
df = pd.read_excel(pasta / arq_nome, sheet_name='Classificação', skiprows=0, dtype={'código':'str'})

print(df.dtypes)


df_class_jan2012_dez2019 = df.copy()

# -------------------------------------------------------------------------------------------------------------------

#####################################################################################################################
################################### CLASSIFICAÇÃO - NOVOS ITENS #####################################################
#####################################################################################################################

############################### Novos itens
import tabula

pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
arq_nome = 'EE069_Atualizacoes_da_estrutura_de_ponderacao_do_IPCA_e_repercussao_nas_suas_classificacoes.pdf'

df = tabula.read_pdf(pasta / arq_nome, pages=[3])[0]
print(df.dtypes)


df.rename(mapper={'Unnamed: 0':'SNIPC','Código':'COICOP','Unnamed: 1':'descrição','Unnamed: 2':'A_I_S_M','Estrutura a partir de jan/2020':'repartir','Unnamed: 3':'IN_SE_AI'},axis=1,inplace=True)
df = df.iloc[2:,:]
df.index = range(len(df))

for index_linha, linha in df.iterrows():
    #print(linha['repartir'].split(' '), index_linha)
    col0 = linha['repartir'].split(' ')[0]
    col1 = linha['repartir'].split(' ')[1]
    col2 = linha['repartir'].split(' ')[2]
    df.loc[index_linha,'C_NC'] = col0
    df.loc[index_linha,'D_SD_ND'] = col1
    df.loc[index_linha,'S_NS'] = col2
    
df.drop(['repartir','COICOP','descrição'],axis=1,inplace=True)
df.rename(mapper={'SNIPC':'código'},axis=1,inplace=True)

df_novosItens = df.copy()



############################### Modificações
import tabula

pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
arq_nome = 'EE069_Atualizacoes_da_estrutura_de_ponderacao_do_IPCA_e_repercussao_nas_suas_classificacoes.pdf'
df = tabula.read_pdf(pasta / arq_nome, pages=[4])[0]
df.rename(mapper={'Unnamed: 0':'código','Código':'COICOP', 'Descrição':'descrição','Unnamed: 1':'atual','Classificação':'novo'},axis=1,inplace=True)
df = df.iloc[1:,:]





#####################################################################################################################
########################################## ESTRUTURA ATUAL ##########################################################
#####################################################################################################################
'''
ROTEIRO
Tabela com colunas: código | descrição
'''

import requests
import pandas as pd
url = "https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204"
r = requests.get(url)
j = r.json()
df = pd.DataFrame.from_dict(j)

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

df = df.loc[:,['código','descrição']]

df = df.groupby(['código']).head(1)

df = df.iloc[2:,:]

df['código'] = df['código'].astype('str')

df_class_jan2020_ = df.copy()

df_class_jan2020_.rename(mapper={'descrição':'descrição_nova'},axis=1,inplace=True)
df_class_jan2020_ = df_class_jan2020_.merge(df_class_jan2012_dez2019,how='left',left_on='código',right_on='código')

# --------------------------------------------


cond1 = df_class_jan2020_['descrição_nova'].str.contains('milho',case=False)
filtro = df_class_jan2020_.loc[cond1,:]

cond1 = df_class_jan2020_['descrição_nova'].str.contains('neurológico',case=False)
filtro = df_class_jan2020_.loc[cond1,:]

cond1 = df_class_jan2020_['descrição_nova'].str.contains('Sobrancelha',case=False)
filtro = df_class_jan2020_.loc[cond1,:]














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
