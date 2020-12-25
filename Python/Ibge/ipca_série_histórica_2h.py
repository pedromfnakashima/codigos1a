# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:05:26 2020

@author: pedro

ROTEIRO

1. Escolha do ano base (flexível, por parâmetro)
2. Cálculo do índice para cada categoria
3. Cálculo  da inflação em 12 meses
4. Cálculo da inflação no ano

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
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)

#import numpy as np
import pandas as pd

#######################################################################################
#######################################################################################
#######################################################################################
# Rodar antes ou o código ipca_série_histórica_2c.py (ibge) ou o código ipca_série_histórica_2h.py (bacen)

dfv = dicCatIBGE['Variação'].copy()


def g_índices(dfv, base):
    
    dfi = dfv.copy()
    
    posi_dt = dfi.index.get_loc(base) # Posição (número) da data-base
    rng_L1 = range(posi_dt - 1, -1, -1) # range de Linhas p/ antes da data-base
    num_linhas = dfi.shape[0] # número de linhas no df
    rng_L2 = range(posi_dt+1, num_linhas) # range de Linhas p/ depois da data-base
    num_colunas = dfi.shape[1] # número de colunas no df
    rng_C = range(num_colunas) # range de Colunas p/ o loomping pelas colunas
    
    # Looping pelas Colunas
    for C in rng_C:
        # Define o índice da data-base como 100
        dfi.iloc[posi_dt, C] = 100
        # Preenche depois da data-base
        for L in rng_L2:
            dfi.iloc[L, C] = dfi.iloc[L-1, C] * (1 + dfv.iloc[L, C]/100)
        # Preenche antes da data-base
        for L in rng_L1:
            dfi.iloc[L, C] = dfi.iloc[L+1, C] / (1 + (dfv.iloc[L+1, C])/100)
    
    return dfi

índices = g_índices(dfv, base='2006-12-01')
índices = g_índices(dfv, base='2012-01-01')
índices = g_índices(dfv, base='2019-12-01')

dfi = g_índices(dfv, base='2006-12-01')
dfi_L12 = dfi.shift(periods=12)

dfv_12m = ((dfi / dfi_L12) - 1) * 100





# Supondo que 200612 seja o mês escolhido para ser o índice = 100


# dfi = dfv.copy()

# base = '2006-12-01'

# posi_dt = dfi.index.get_loc(base)
# rng_L1 = range(posi_dt - 1, -1, -1)
# # lista1 = list(rng_L1)

# num_linhas = dfi.shape[0]
# rng_L2 = range(posi_dt+1, num_linhas)
# # lista2 = list(rng_L2)

# num_colunas = dfi.shape[1]
# rng_C = range(num_colunas)
# # lista3 = list(rng_C)


# print(list(range(num_colunas)))
# print(dfi.iloc[0,8])
# print(dfi.iloc[posi_dt, col_i])

# for C in rng_C:
#     print(C)
#     dfi.iloc[posi_dt, C] = 100
#     for L in rng_L2:
#         # print(i)
#         # i_1 = i - 1
#         # iloc
#         # print(i_1)
#         # print(dfi.iloc[i-1, col_i])
#         dfi.iloc[L, C] = dfi.iloc[L-1, C] * (1 + dfv.iloc[L, C]/100)
    
#     for L in rng_L1:
#         # print(i)
#         dfi.iloc[L, C] = dfi.iloc[L+1, C] / (1 + (dfv.iloc[L+1, C])/100)


