# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:04:46 2020

@author: pedro-salj

A CULPA POR SOMAS ERRADAS É DE CÓDIGOS CNAE SUBCLASSE QUE NÃO EXISTEM!!!!
EXEMPLO: 8630505

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
os.chdir(caminho_wd)
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

pasta = caminho_base / 'Dados' / 'cnae e ncm'
arq_nome = 'cnae_corresp.csv'
cnae_corresp_longo = pd.read_csv(pasta / arq_nome,
                              delimiter = '|',
                              decimal=',',
                              dtype='str')


##########################################################################################################
arq_nome = 'CAGEDMOV202010.csv'
pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
dtype = {'cnae_subclasse_cod':'str','cnae_classe_cod':'str', 'competência':'str'}
df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',',
                 dtype=dtype)

df.rename(mapper={'cnae_seção_cod':'cnae_seção_cod_orig'},axis=1,inplace=True)

cond1 = df['cnae_subclasse_cod'] == '8630505'
df.loc[cond1, 'cnae_subclasse_cod'] = '8630504'

df = df.merge(cnae_corresp_longo,how='left',left_on='cnae_subclasse_cod',right_on='cnae_subclasse_cod')

cond1 = df['cnae_classe_cod'].isnull()
filtro = df.loc[cond1,:]

df_agregado = df.groupby(['cnae_seção_cod'])['saldomovimentação'].sum().to_frame()

print(df_agregado['saldomovimentação'].sum())




