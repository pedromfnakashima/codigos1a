# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 02:07:52 2020

@author: pedro
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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

##########################################################################################################
################################### TESTES ###############################################################
##########################################################################################################
import pandas as pd

caminho = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(caminho / 'CAGEDMOV202009.csv', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)

caminho = caminho_base / 'Dados' / 'trabalho' / 'rais_vinculos' / 'microdados'
df = pd.read_csv(caminho / 'MS2007.txt', header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}'])
print(df.dtypes)



print(df['saldomovimentação'].sum())


##########################################################################################################
##########################################################################################################
##########################################################################################################
import pandas as pd















