# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:47:48 2020

@author: pedro

Meta: transformar cod5, cod7... em cod
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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'

os.chdir(caminho_wd)
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

import glob
import re

for arq_nome in glob.glob('*.csv'):
    print(arq_nome)
    
    #arq_nome = 'CAGEDMOV200701.csv'
    #arq_nome = 'CAGEDMOV202009.csv'
    
    dtype = {'cbo2002ocupação_cod6':'str','cnae2_subclasse_cod7':'str','cnae2_classe_cod5':'str'}
    pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
    df = pd.read_csv(pasta / arq_nome,
                                  delimiter = ';',
                                  decimal=',',
                                  dtype=dtype)
    
    #print(df.dtypes)
    
    #df['len'] = df['cnae2_subclasse_cod7'].str.len()
    #print(df['len'].value_counts())
    
    colunas_antes = df.columns
    colunas_depois = []
    for coluna in colunas_antes:
        nova_coluna = re.sub(r'\d', "", coluna)
        nova_coluna = re.sub(r'cbo', "cbo_", nova_coluna)
        #print(nova_coluna)
        colunas_depois.append(nova_coluna)
    
    #print(colunas_depois)
    
    df.columns = colunas_depois
    
    df.to_csv(arq_nome, sep=';', decimal=',', index=False)











