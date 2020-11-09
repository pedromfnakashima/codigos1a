# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 07:21:00 2020

@author: pedro-salj
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
import pandas as pd

print(dir(tabula))

df = tabula.read_pdf("cadernoPloa.pdf", pages=22)[0]
df.columns = df.loc[0,:]
df.drop(0, axis=0, inplace=True)

for (columnName, columnData) in df.loc[:, df.columns != 'Sub Categoria'].iteritems():
   print('Colunm Name : ', columnName)
   df[columnName] = df[columnName].str.replace('.','').str.replace(',','.').str.replace('(','-').str.replace(')','')
   df[columnName] = df[columnName].astype(float)
del columnName, columnData
df.set_index('Sub Categoria', inplace=True)
df = df.T


















