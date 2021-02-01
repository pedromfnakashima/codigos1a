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
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)

#import numpy as np
import pandas as pd

#################################################################################################
################################# DOWNLOAD DOS ARQUIVOS #########################################
#################################################################################################
'''
Períodos e tabelas
2938: julho/2006 até dezembro/2011 (link: https://sidra.ibge.gov.br/Tabela/2938)
1419: janeiro/2012 até dezembro/2019 (link: https://sidra.ibge.gov.br/tabela/1419)
7060: a partir de janeiro/2020 (link: https://sidra.ibge.gov.br/tabela/7060)
'''
##################################### ----------- #####################################

arqs_csv = ['t2938.csv','t1419.csv','t7060.csv']

arq_nome = "t7060.csv"


##########################################################################################################
##########################################################################################################
##########################################################################################################

def g_li_categorias(): # rodar ipca_série_histórica_2a_auxiliar3.py

    li_categorias = ['Grupo','Subgrupo','Item','Subitem']
    
    # GRUPOS
    arq_nome = 'categorias.xlsx'
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    
    dic_categorias = {}
    
    for categoria in li_categorias:
        #categoria = 'Subgrupo'
    
        plan_nome = '202001_' + categoria
        df_cat = pd.read_excel(pasta / arq_nome, sheet_name=plan_nome, skiprows=0,dtype={'código':'str'})
        dic_categorias[categoria] = df_cat
    return dic_categorias

dic_categorias = g_li_categorias()



# ---------------------------------------
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't7060.csv'
df1 = pd.read_csv(pasta / arq_nome,
                              delimiter = '|',
                              decimal=',',
                              dtype='str')

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't1419.csv'
df2 = pd.read_csv(pasta / arq_nome,
                              delimiter = '|',
                              decimal=',',
                              dtype='str')

df = df1.append(df2)

# Definir nível territorial
cond1 = df['NC'] == '1'
df = df.loc[cond1,:]

# Variável de data
df['V'] = pd.to_numeric(df['V'],errors='coerce')
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

# O FOR ABAIXO É EXTREMAMENTO LENTO PARA DFS GRANDES!!! REFAZER!!!

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

# Filtros
# DF separado por: variação percentual, peso, contribuição

categoria = 'Grupo'

# vp = 'variação'
vp = 'peso'

dicionário1 = {}
li_variação_peso = ['Variação', 'Peso']


for vp in li_variação_peso:
    
    cond1 = df['D2N'].str.contains(vp,case=False)
    cond2 = df['categoria'] == categoria
    cond = cond1 & cond2
    df_cat = df.copy().loc[cond,:]
    
    for index_linha, linha in dic_categorias[categoria].iterrows():
        print(index_linha, linha['código'], linha['descrição'])
    
        # código = '1'
        # nome = 'Alimentação e bebidas'
        # código = '11'
        # nome = 'Alimentação no domicílio'
        código = linha['código']
        
        nome_maior = linha['código'] + '. ' + linha['descrição']
        
        cond1 = df_cat['código'] == código
        df_categoria_i = df_cat.loc[cond1,:]
        
        df_categoria_i.set_index('dt',inplace=True)
        
        df_categoria_i = df_categoria_i.loc[:,['V']]
        
        df_categoria_i.rename(mapper={'V':nome_maior},axis=1,inplace=True)
        
        if index_linha == 0:
            df_categoria_ii = df_categoria_i.copy()
        else:
            df_categoria_ii = df_categoria_ii.merge(df_categoria_i,how='left',left_index=True,right_index=True)
    
    dicionário1[vp] = df_categoria_ii

dicionário1['Contribuição'] = (dicionário1['Variação'] * dicionário1['Peso']) / 100
print(dicionário1['Variação'].dtypes)
print(dicionário1['Peso'].dtypes)

# Tabelas com as descrições e códigos





# DF com correspondências

arq_nome = 'classificação.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df = pd.read_excel(pasta / arq_nome, sheet_name='jan2020_', skiprows=0, dtype={'código':'str'})
print(df.dtypes)







# Criar 4 DFs: Variação, Peso, Contribuição, Índice


D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Ibge\Ipca














cond1 = df['D4N'] == 'Índice geral'
filtro = df.loc[cond1,:]

##########################################################################################################
##########################################################################################################
##########################################################################################################
