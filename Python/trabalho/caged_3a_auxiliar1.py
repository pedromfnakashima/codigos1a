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


##########################################################################################################
##########################################################################################################
##########################################################################################################

import glob
import re

for arq_nome in glob.glob('*.csv'):
    print(arq_nome)
    
    #arq_nome = 'CAGEDMOV200701.csv'
    #arq_nome = 'CAGEDMOV202009.csv'
    
    dtype = {'cbo_ocupação_cod':'str','cnae_subclasse_cod':'str','cnae_classe_cod':'str'}
    pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
    df = pd.read_csv(pasta / arq_nome,
                                  delimiter = ';',
                                  decimal=',',
                                  dtype=dtype)
    df['len'] = df['cnae_subclasse_cod'].str.len()
    #print(df['len'].value_counts())
    
    cond1 = df['len'] == 6
    print(f'Linhas com subclasses de 6 dígitos: {cond1.sum()}')
    #df.loc[cond1, 'cnae_subclasse_cod'] = '0' + df['len']
    
    #print(df['len'].value_counts())
    
    #df.to_csv(arq_nome, sep=';', decimal=',', index=False)

##########################################################################################################
##########################################################################################################
##########################################################################################################
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
os.chdir(caminho_wd)

import glob
import re

for arq_nome in glob.glob('*.txt'):
    print(arq_nome)
    
    #arq_nome = 'CAGEDMOV200701.csv'
    #arq_nome = 'CAGEDMOV202009.csv'
    
    #dtype = {'cbo_ocupação_cod':'str','cnae_subclasse_cod':'str','cnae_classe_cod':'str'}
    pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
    df = pd.read_csv(pasta / arq_nome,
                                  delimiter = ';',
                                  decimal=',',
                                  dtype={'subclasse':'str'})
    df['len'] = df['subclasse'].str.len()
    #print(df['len'].value_counts())
    
    cond1 = df['len'] == 6
    print(f'Linhas com subclasses de 6 dígitos: {cond1.sum()}')
    #df.loc[cond1, 'cnae_subclasse_cod'] = '0' + df['len']
    
    #print(df['len'].value_counts())
    
    #df.to_csv(arq_nome, sep=';', decimal=',', index=False)






