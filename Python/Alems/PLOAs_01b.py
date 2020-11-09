# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:42:07 2020

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

######################################

import tabula
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-até2014', skiprows=0, na_values=['-'])
df['Órgão'] = df['Órgão'].str.replace('Assembléia', 'Assembleia')
df.dropna(thresh=4, inplace=True)

with pd.ExcelWriter(pasta / 'LOAs.xlsx', mode='a', engine="openpyxl") as writer:  
    df.to_excel(writer, sheet_name='Desp-Órgão-até2014', index=False)

# ---------------------------------------------------------------------------------------------------------
pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-2015-', skiprows=0, na_values=['-'])
df['Órgão'] = df['Órgão'].str.replace('Assembléia', 'Assembleia')
df.dropna(thresh=4, inplace=True)

with pd.ExcelWriter(pasta / 'LOAs.xlsx', mode='a', engine="openpyxl") as writer:  
    df.to_excel(writer, sheet_name='Desp-Órgão-2015-', index=False)

######################################
'''
Despesa por órgão
'''
pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df1 = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-até2014', skiprows=0, na_values=['-'])
df1 = df1[['LOA', 'Poder', 'Órgão', 'TOTAL']]

pasta = caminho_wd = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
df2 = pd.read_excel(pasta / 'LOAs.xlsx', sheet_name='Desp-Órgão-2015-', skiprows=0, na_values=['-'])
df2 = df2[['LOA', 'Poder', 'Órgão', 'TOTAL']]

df2 = df2.append(df1)

df2 = df2.sort_values(by=['LOA', 'Poder', 'Órgão'], ascending=[True, True, True])

with pd.ExcelWriter(pasta / 'LOAs - Séries.xlsx', mode='a', engine="openpyxl") as writer:  
    df2.to_excel(writer, sheet_name='Desp_Tot_Orgão', index=False)

######################################

cond = df2['Órgão'] == 'Assembleia Legislativa'
filtro = df2.loc[cond,:]
filtro.set_index('LOA', inplace=True)


filtro['TOTAL'].plot()

'''
Como deflacionar? Qual índice escolher?
'''















