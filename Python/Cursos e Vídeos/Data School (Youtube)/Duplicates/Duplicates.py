# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:56:21 2020

@author: pedro-salj

https://www.youtube.com/watch?v=ht5buXUMqkQ
"""


globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório"""
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)
# --------------------------------------------------------------
import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')

print(users.shape) # 943 x 4

# Marca duplicados
'''
Marca como verdadeiro se anteriormente já apareceu
uma ocorrência do valor de uma coluna.
'''
print(users.zip_code.duplicated())

# Conta zip_code duplicados
print(users.zip_code.duplicated().sum()) # 148

'''
Marca se uma linha inteira já apareceu anteriormente
acima
'''
# Conta linhas inteiras duplicadas
print(users.duplicated().sum()) # 7

# Lista as 7 linhas duplicadas
print(users.loc[users.duplicated(), :])

'''
Marca as duplicadas como verdadeiro, com exceção
da PRIMEIRA
'''
# Lista as 7 linhas duplicadas; keep ='first' é o padrão
print(users.loc[users.duplicated(keep='first'), :])

'''
Marca as duplicadas como verdadeiro, com exceção
da ÚLTIMA
'''
print(users.loc[users.duplicated(keep='last'), :])

'''
Marca todas as duplicadas como verdadeiro
'''
print(users.loc[users.duplicated(keep=False), :])

'''
Deleta as duplicadas
'''

users_sem_dup = users.drop_duplicates(keep='first')
print(users_sem_dup.shape)

users_sem_dup = users.drop_duplicates(keep='last')
print(users_sem_dup.shape)

users_sem_dup = users.drop_duplicates(keep=False)
print(users_sem_dup.shape)

'''
Considera apenas algumas colunas quando identificar
os duplicados
'''

print(users.duplicated(subset=['age','zip_code']).sum())

users_sem_dup = users.drop_duplicates(subset=['age','zip_code'])
print(users_sem_dup.shape)







