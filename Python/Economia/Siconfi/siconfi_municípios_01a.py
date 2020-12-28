# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:36:36 2020

@author: pedro

No próximo arquivo (siconfi_municípios_01b.py), será transformado o código abaixo em função
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
caminho_wd = caminho_base / 'codigos_versionados' / 'Python' / 'Siconfi' # pasta onde tem os scripts (para importar as funções)
os.chdir(caminho_wd)

#import numpy as np
import pandas as pd

############################
############################
############################

# As funções abaixo têm que estar em arquivos no mesmo diretório (e também ser wd)
from f_processa_arquivos_zip import processa_arquivos_zip
from f_g_li_datas import g_li_datas

# Municípios de MS
arq_nome = 'municípios_e_ufs.xlsx'
pasta = caminho_base / 'Dados'
df_municípios = pd.read_excel(pasta / arq_nome, sheet_name='municípios_ms', skiprows=0)
df_municípios = df_municípios.loc[:,['mun_cod7_ibge','mun_nome_curto']]

li_períodos = g_li_datas('2019b1', '2020b2', extensão='.zip')

# dicionário_completo = {}

for index_per, str_per in enumerate(li_períodos):
    # print(str_per, index_per)
    
    # index_per = 0
    # str_per = '2020b1.zip'
    
    # index_per = 1
    # str_per = '2020b2.zip'
    
    pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Municípios' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
    df = processa_arquivos_zip(arquivo=str_per,
                               caminho=pasta,
                               pasta=False)
    
    dicionário_i = {}
    
    for index_linha, linha in df_municípios.iterrows():
        # print(linha['mun_cod7_ibge'], linha['mun_nome_curto'])
        
        mun_cód = linha['mun_cod7_ibge']
        # mun_cód = 5002704 # Campo Grande
        
        cond1 = df['Cod.IBGE'] == mun_cód
        cond2 = df['MR'] == 0
        cond = cond1 & cond2
        filtro = df.loc[cond, :]
        
        li_variáveis = filtro['Conta'].unique()
        
        for index_var, str_variável in enumerate(li_variáveis):
            # print(str_variável, index_var)
            
            # index_var = 0
            # str_variável = 'IPTU'
            
            cond1 = df['Cod.IBGE'] == mun_cód
            cond2 = df['Conta'] == str_variável
            cond3 = ~ df['mês'].isnull()
            cond = cond1 & cond2 & cond3
            filtro = df.loc[cond, ['mês','MR','Valor']]
            
            filtro.rename(mapper={'Valor':str_variável},axis=1,inplace=True)
            
            if index_var == 0:
                df_completo = filtro.copy()
            else:
                df_completo = df_completo.merge(filtro,how='left',left_on=['mês','MR'],right_on=['mês','MR'])
            
        dicionário_i[linha['mun_nome_curto']] = df_completo
    
    if index_per == 0:
        dicionário_completo = dicionário_i.copy()
    else:
        for key in dicionário_i.keys():
            # print(key)
            dicionário_completo[key] = dicionário_completo[key].append(dicionário_i[key])
    

for key in dicionário_completo.keys():
    
    dicionário_completo[key].sort_values(['mês','MR'],ascending=[True,True],inplace=True)
    
    dicionário_completo[key] = dicionário_completo[key].groupby(['mês']).tail(1)
    
    dicionário_completo[key].fillna(0,inplace=True)
    
    dicionário_completo[key].set_index('mês',inplace=True)










