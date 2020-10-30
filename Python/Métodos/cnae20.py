# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:44:12 2020

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
caminho_wd = caminho_base / 'Dados' / 'cnae e ncm'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())



import pandas as pd
cnae20 = pd.read_excel('CNAE20_Subclasses_EstruturaDetalhada.xlsx', sheet_name='Est. Detalhada CNAE 2.0 - subcl')

print(cnae20.columns)

cnae20 = cnae20.drop(['Unnamed: 0'], axis=1)

cnae20 = cnae20.rename(columns={'2.2 Estrutura detalhada da CNAE 2.0: seções, divisões, grupos, classes e subclasses':'seção',
                                'Unnamed: 2':'divisão',
                                'Unnamed: 3':'grupo',
                                'Unnamed: 4':'classe',
                                'Unnamed: 5':'subclasse',
                                'Unnamed: 6':'descrição'})

cnae20 = cnae20.iloc[4:,]
cnae20.index = range(len(cnae20))

cond1 = ~ cnae20['seção'].str.contains('continuação', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('2.2', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('2.0', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('Seção', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('conclusão', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

print(cnae20.dtypes)
cnae20['seção'].fillna(method='ffill', inplace=True)
cnae20['divisão'].fillna(method='ffill', inplace=True)
cnae20['grupo'].fillna(method='ffill', inplace=True)
cnae20['classe'].fillna(method='ffill', inplace=True)
cnae20['subclasse'].fillna(method='ffill', inplace=True)


cnae20['subclasse'] = cnae20['subclasse'].str.replace('-','').str.replace('/','')
cnae20['classe'] = cnae20['classe'].str.replace('.','').str.replace('-','')
cnae20['grupo'] = cnae20['grupo'].str.replace('.','')

cnae20 = cnae20.iloc[:-2]
