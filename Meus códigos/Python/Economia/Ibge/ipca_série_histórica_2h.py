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

# dicCatIBGE = g_dic_contribuição(df, cod_D1C='1', categoria='Grupo')
# dfv = dicCatIBGE['Variação'].copy()


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

# índices = g_índices(dfv, base='2006-12-01')
# índices = g_índices(dfv, base='2012-01-01')
# índices = g_índices(dfv, base='2019-12-01')

# dfi = g_índices(dfv, base='2006-12-01')

def g_v12m(dfi):

    dfi_L12 = dfi.shift(periods=12)
    
    dfv_12m = ((dfi / dfi_L12) - 1) * 100
    
    return dfv_12m

# dfv_12m = g_v12m(dfi)

def g_vano(dfi):
    
    dfi_dez = dfi.copy()
    
    import numpy as np
    cond1 = dfi_dez.index.month != 12
    dfi_dez.loc[cond1,:] = np.nan
    
    dfi_dez = dfi_dez.shift(periods=1)
    
    dfi_dez.fillna(method='ffill',inplace=True)
    
    dfv_ano = ((dfi / dfi_dez) - 1) * 100
    
    return dfv_ano

# dfv_ano = g_vano(dfi)

###############################################################################
###############################################################################

dicCatIBGE = g_dic_contribuição(df, cod_D1C='1', categoria='Grupo')
dfv = dicCatIBGE['Variação'].copy()

dfi = g_índices(dfv, base='2006-12-01')
dfv_12m = g_v12m(dfi)
dfv_ano = g_vano(dfi)

###############################################################################
###############################################################################

def transpõeEordena(df, ordenaPor='último'):
    
    df_cp = df.copy()
    df_cp['dt_ano_mes'] = [str(dt.year) + str(dt.month).zfill(2) for dt in df_cp.index]
    último = df_cp.iloc[-1,-1]
    df_cp.sort_index(ascending=False, inplace=True)
    df_cp.set_index('dt_ano_mes',inplace=True)
    df_longo = df_cp.T
    # Ordena pela coluna do último mês
    if ordenaPor == 'último':
        df_longo.sort_values(by=[último],ascending=[False],inplace=True)
    else:
        df_longo.sort_values(by=[ordenaPor],ascending=[False],inplace=True)
    return df_longo

dfv_T = transpõeEordena(dfv, ordenaPor='último')

dfv_T = transpõeEordena(dfv, ordenaPor='202011')

dfv_12m_T = transpõeEordena(dfv_12m, ordenaPor='202011')




















