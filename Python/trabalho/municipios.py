# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:33:38 2020

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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

import pandas as pd

###############################################
####### códigos dos estados ################
###############################################

caminho_caged = caminho_base / 'Dados' / 'trabalho'
df_estados = pd.read_excel(caminho_caged / 'Layout Novo Caged Movimentação.xlsx', sheet_name='uf')  
df_estados = df_estados.rename(columns = {'Código': 'uf_cod_ibge', 'Descrição': 'uf_nome', 'Sigla':'uf_sigla'})
print(df_estados.columns)
df_estados = df_estados[['uf_cod_ibge', 'uf_sigla']]

df_estados.to_excel('estados.xlsx', sheet_name='estados', engine='xlsxwriter', index=False)  


###############################################
####### códigos dos municipios ################
###############################################

caminho_mun = caminho_base / 'Dados'
caminho_caged = caminho_base / 'Dados' / 'trabalho'
caminho_tse = caminho_base / 'Dados' / 'TSE'

df_municipios = pd.read_excel(caminho_mun / 'codigos_municipios.xlsx', sheet_name='municipios')  
df_municipios = df_municipios.rename(columns = {'Código Município Completo': 'mun_cod_ibge', 'Nome_Município': 'mun_nome', 'UF':'uf_cod_ibge', 'Capital':'capital'})
print(df_municipios.dtypes)
print(df_municipios['mun_cod_ibge'].nunique())

df_uf_codigos = pd.read_excel(caminho_caged / 'Layout Novo Caged Movimentação.xlsx', sheet_name='uf') 
print(df_uf_codigos.columns)
df_uf_codigos = df_uf_codigos.rename(columns = {'Código': 'uf_cod_ibge', 'Sigla': 'uf_sigla'})
df_uf_codigos = df_uf_codigos.drop(['Descrição'], axis=1)
print(df_uf_codigos.dtypes)

df_municipios_tse = pd.read_excel(caminho_mun / 'conversao_ibge_tse.xlsx', sheet_name='municipios')  
print(df_municipios_tse.dtypes)
print(df_municipios_tse['mun_cod_ibge'].nunique())

df_municipios = pd.merge(df_municipios, df_municipios_tse, how='left', on='mun_cod_ibge')
df_municipios = pd.merge(df_municipios, df_uf_codigos, how='left', on='uf_cod_ibge')

df_municipios['mun_nome'] = df_municipios['uf_sigla'] + '-' + df_municipios['mun_nome']
print(df_municipios.columns)

df_municipios = df_municipios[['mun_cod_ibge', 'mun_cod_tse', 'mun_nome', 'capital']]

df_municipios.to_excel('municipios.xlsx', sheet_name='municipios', engine='xlsxwriter', index=False)  