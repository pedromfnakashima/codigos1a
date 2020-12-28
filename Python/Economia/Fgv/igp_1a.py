# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:14:27 2020

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
caminho_wd = caminho_base / 'Dados' / 'Firjan'
os.chdir(caminho_wd)
import numpy as np
import pandas as pd


##########################################################################################################
##########################################################################################################
##########################################################################################################

pasta = caminho_base / 'Dados' / 'Fgv'
arq_nome = 'IGP-DI.csv'

try:  
    df = pd.read_csv(pasta / arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
except UnicodeDecodeError: # ocorre exceção
    df = pd.read_csv(pasta / arq_nome, encoding = 'latin', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
else: # Sem exceções
    pass
finally: # sempre fazer isso
    pass

df['Data'] = df['Data'].astype('datetime64[ns]')

df.set_index('Data',inplace=True)

# --------------------------------------------------------------------

pasta = caminho_base / 'Dados' / 'Fgv'
arq_nome = 'IGP - DI, OG, M, 10.csv'
na_values = [' - ','-']


try:  
    df = pd.read_csv(pasta / arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, na_values=na_values)
except UnicodeDecodeError: # ocorre exceção
    df = pd.read_csv(pasta / arq_nome, encoding = 'latin', header=0, sep=';', decimal=',', quotechar='"', skiprows=0, na_values=na_values)
else: # Sem exceções
    pass
finally: # sempre fazer isso
    pass

df['Data'] = df['Data'].astype('datetime64[ns]')

df.set_index('Data',inplace=True)




































