# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:51:24 2020

@author: pedro
"""

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
caminho_wd = caminho_base / 'Dados' / 'alems'
os.chdir(caminho_wd)

#pip install tabula-py

import tabula
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-até2014', skiprows=0, dtype={'capital': np.bool})

print(df.dtypes)

print(df['Órgão'].isna().sum())

#cond = df['Órgão'].isna()
#df_filtro = df.loc[cond,:]

df['Órgão'] = df['Órgão'].str.replace('Assembléia', 'Assembleia')


cond = df['Órgão'].str.contains('Assembléia')
df_filtro = df.loc[cond,:]



print(df['Órgão'].value_counts().head(20))

contagem = df['Órgão'].value_counts()


cond = df.applymap(np.isreal)


df.applymap(np.isreal)

######################################
######################################
######################################

import tabula
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-até2014', skiprows=0, na_values=['-'])

df.dropna(thresh=4, inplace=True)

print(df.dtypes)

df2 = df.copy()
print(df2['TESOURO'].apply(type))

stats = df2['TESOURO'].apply(type)
print(stats.value_counts())

cond = df['TESOURO'].apply(lambda x: type(x).__name__) == 'str'
'''
Referência da linha acima:
    https://pbpython.com/currency-cleanup.html
'''
print(cond.sum())

cond = df['TESOURO'].apply(lambda x: type(x).__name__) == 'str'
filtro = df.loc[cond,:]

cond = df['OUTRAS FONTES'].apply(lambda x: type(x).__name__) == 'str'
filtro = df.loc[cond,:]

cond = df['TOTAL'].apply(lambda x: type(x).__name__) == 'str'
filtro = df.loc[cond,:]

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-até2014', skiprows=0, dtype={'TESOURO': np.float64})

# Série com o orçamento da alems

import tabula
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-até2014', skiprows=0, na_values=['-'])

df['Órgão'] = df['Órgão'].str.replace('Assembléia', 'Assembleia')

cond = df['Órgão'] == 'Assembleia Legislativa'
filtro = df.loc[cond,:]
filtro.set_index('LOA', inplace=True)

filtro.sort_values(by=['LOA'], inplace=True)

filtro['TOTAL'].plot()

with pd.ExcelWriter(pasta / 'arq.xlsx', mode='a', engine="openpyxl") as writer:  
    df.to_excel(writer, sheet_name='Planilha 2', index=False)


######################################
######################################
######################################

import tabula
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-2015-', skiprows=0, na_values=['-'])


cond = df['FISCAL'].apply(lambda x: type(x).__name__) == 'str'
filtro = df.loc[cond,:]







