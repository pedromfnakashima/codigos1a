# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 07:31:18 2020

@author: pedro-salj
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

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)
import pandas as pd
##########################################################################################################
##########################################################################################################
##########################################################################################################

arq_nome = 'EXP_2020.csv'

pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / arq_nome,
                       encoding = 'latin',
                       delimiter = ';')

df.rename(columns={'CO_ANO':'year','CO_MES':'month'},inplace=True)
df['day'] = 1
df['mês'] = pd.to_datetime(df[['year', 'month', 'day']])
df.drop(['year','month','day'],axis=1,inplace=True)

agregado = df.groupby(['mês','CO_NCM'])['VL_FOB'].sum().to_frame()

agregado.reset_index(inplace=True)

agregado.sort_values(by=['mês','VL_FOB'], ascending=[True,False],inplace=True)


















