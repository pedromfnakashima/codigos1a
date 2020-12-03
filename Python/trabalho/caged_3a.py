# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:28:09 2020

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
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################
arq_nome = 'CAGEDMOV200701.csv'

arq_nome = 'CAGEDMOV201912.csv'

arq_nome = 'CAGEDMOV202001.csv'

import pandas as pd

pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',')

import glob
import pandas as pd
from pathlib import Path

os.chdir(pasta)

vetor1 = []

for arq_num, arq_nome in enumerate(glob.glob('*.csv')):
    print(arq_nome)
    
    df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',')
    
    colunas = df.columns
    
    vl_bool = 'classe.1' in colunas
    
    vetor1.append(vl_bool)
    
    
    
    
colunas = df.columns

print('competência' in colunas)


vl_bool = 'classe.1' in colunas


vetor1 = []

vetor1.append(vl_bool)












