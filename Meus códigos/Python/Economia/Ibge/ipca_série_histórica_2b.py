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
##########################################################################################################
##################################### Importa dados #####################################
##########################################################################################################

def junta_arqs(arqs_csv, pasta):
    for index_arq, arq_nome in enumerate(arqs_csv):
        
        # arq_nome = "t7060.csv"
        print(arq_nome)
    
        df = pd.read_csv(pasta / arq_nome,
                                      delimiter = '|',
                                      decimal=',',
                                      dtype='str',
                                      parse_dates=['dt'])
        if index_arq == 0:
            df2 = df.copy()
        else:
            df2 = df2.append(df)
    
    return df2

arqs_csv = ['t2938.csv','t1419.csv','t7060.csv']
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'

df = junta_arqs(arqs_csv=arqs_csv, pasta=pasta)

# li_datas = pd.DatetimeIndex(df['dt'].unique())
# df_datas = pd.DataFrame({'dt':li_datas})
# df_datas.set_index('dt',inplace=True)
# del li_datas

##########################################################################################################
################################# Importa categorias IBGE ######################################
##########################################################################################################

def g_dic_categorias(arq_nome, pasta):
    
    dic_categorias = {}
    
    li_categorias = ['Grupo','Subgrupo','Item','Subitem']
    
    for plan_nome in li_categorias:
        
        # plan_nome = 'Grupo'
        df_cat_i = pd.read_excel(pasta / arq_nome, sheet_name=plan_nome, skiprows=0,dtype={'código':'str'},parse_dates=['início'])
        
        dic_categorias[plan_nome] = df_cat_i
    
    return dic_categorias

arq_nome = 'categoriasIBGE.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'

dic_categorias = g_dic_categorias(arq_nome=arq_nome, pasta=pasta)


# print(df.dtypes)

cod_D1C = '1' # Território: Brasil
categoria = 'Grupo'

arq_nome = 'categoriasIBGE.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
df_categoria_i = pd.read_excel(pasta / arq_nome, sheet_name=categoria, skiprows=0)

# for index_linha, linha in df_categoria_i.iterrows():
#     print(linha['código'])

dicionário1 = {}
li_variação_peso = ['Variação', 'Peso']

# vp = 'Variação'
# vp = 'peso'

for vp in li_variação_peso:
    
    cond1 = df['D2N'].str.contains(vp,case=False)
    cond2 = df['tipoCatIBGE'] == categoria
    cond3 = df['D1C'] == cod_D1C
    cond = cond1 & cond2 & cond3
    filtro1 = df.copy().loc[cond,:]
    
    # print(df_categoria_i.dtypes)
    
    for index_linha, linha in df_categoria_i.iterrows():
        CódIBGE_cat_i = linha['código']
        DescIBGE_cat_i = linha['descrição']
        CódDescIBGE_cat_i = str(CódIBGE_cat_i) + '. ' + DescIBGE_cat_i
        # print(index_linha, CódDescIBGE_cat_i)
        
        # index_linha = 0
        # CódIBGE_cat_i ='1. Alimentação e bebidas'
        cond1 = filtro1['códIBGE'] == str(CódIBGE_cat_i)
        filtro2 = filtro1.loc[cond1,['dt','V']]
        filtro2.set_index('dt',inplace=True)
        filtro2.rename(mapper={'V':CódDescIBGE_cat_i},axis=1,inplace=True)
        

        
        if index_linha == 0:
            df_todos = filtro2.copy()
        else:
            df_todos = df_todos.merge(filtro2,how='left',left_index=True,right_index=True)
        
        # Converte para numérico
        df_todos = df_todos.apply(pd.to_numeric)
    
    dicionário1[vp] = df_todos

dicionário1['Contribuição'] = (dicionário1['Variação'] * dicionário1['Peso']) / 100










