# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:49:44 2020

@author: pedro-salj

http://www.sefaz.ms.gov.br/loa-leis-orcamentarias-anuais/

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
caminho_wd = caminho_base / 'Dados' / 'LOA, LDO - MS' 
os.chdir(caminho_wd)
##########################################################################################################
##########################################################################################################
##########################################################################################################
import numpy as np
import pandas as pd


#pip install tabula-py

import tabula

df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[2])[0]

df1 = df.copy()

print(df2.dtypes)

lista = ['TESOURO', 'OUTRAS FONTES', 'TOTAL']

df1[lista] = df1[lista].apply(lambda col: col.str.replace('.',''))

df1[lista] = df1[lista].apply(lambda col: col.astype('float64'))

print(df2.dtypes)


df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[7])


'''
DESPESAS CORRENTES
pág. 7
Pessoal, Juros, Investimentos
10 - Fiscal 20 - Seguridade
'''
import tabula

df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[7])


'''
DESPESA POR FUNÇÃO
pág. 10

'''
import tabula

df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[10])

'''
DESPESA COM PESSOAL E JUROS
INVESTIMENTOS
pág. 12

'''
import tabula

df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[12])

'''
APLICAÇÃO DO ICMS NA SAÚDE: pág. 13
APLICAÇÃO DO ICMS NA EDUCAÇÃO: pág. 14

'''
import tabula

df = tabula.read_pdf(caminho_wd / 'LOA 2020.pdf', pages=[12])






































