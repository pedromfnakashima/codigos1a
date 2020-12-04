# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:42:03 2020

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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / arq_nome,
                 encoding = 'latin',
                 delimiter = ';')
        


pasta = caminho_base / 'Dados'
df_municipios = pd.read_excel(pasta/'municipios.xlsx', sheet_name='municipios', dtype={'mun_cod_ibge7':'str'})
df_municipios['mun_cod_ibge6'] = df_municipios['mun_cod_ibge7'].str.slice(0,6)
df_municipios = df_municipios.loc[:,['mun_cod_ibge7','mun_cod_ibge6','mun_cod_tse','mun_nome','uf_sigla']]

pasta = caminho_base / 'Dados'
with pd.ExcelWriter(pasta / 'municipios.xlsx', mode='a', engine="openpyxl") as writer:  
    df_municipios.to_excel(writer, sheet_name='municipios', index=False)
    
    



