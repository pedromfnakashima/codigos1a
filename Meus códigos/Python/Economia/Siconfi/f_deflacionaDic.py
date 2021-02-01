# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 19:46:25 2020

@author: pedro
"""

import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')


import pandas as pd
from datetime import datetime


# -------

def deflaciona_dic(dic, base='último', exclusões=False, download=False):
    
    # base = 'último'
    # base='202008'
    # download=False
    # exclusões=['MR']
    # dic = dic_muns.copy()
    
    # -------

    if download == True:
        import requests
        url = f'https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/2266/p/all/d/v2266%2013'
        r = requests.get(url)
        j = r.json()
        df = pd.DataFrame.from_dict(j)
        df['dt'] = pd.to_datetime(df['D3C'], format='%Y%m', errors='coerce')
        df['V'] = pd.to_numeric(df['V'], errors='coerce')
        cond1 = ~ df['dt'].isnull()
        df = df.loc[cond1,['dt','V']]
        df.set_index('dt',inplace=True)
        df.index.freq = 'MS'
        df.rename(mapper={'V':'índice'},axis=1,inplace=True)
    
        pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
        arq_nome = "ipca_índice.csv"
        df.to_csv(pasta / arq_nome, sep='|', decimal=',', index=True)
    else:
        pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
        arq_nome = "ipca_índice.csv"
        df = pd.read_csv(pasta / arq_nome,delimiter = '|',decimal=',',parse_dates=['dt'],index_col=['dt'])
    
    # base_escolhida para deflacionar
    if base == 'último':
        base_escolhida = df.loc[df.index.max(), 'índice']
    else:
        base_ano = int(base[0:4])
        base_mês = int(base[-2:])
        base_dt = datetime(base_ano, base_mês, 1)
        base_escolhida = df.loc[base_dt, 'índice']
    
    df['deflator'] = base_escolhida / df['índice']
    
    s_deflator = df['deflator']
    
    diccp = dic.copy()
    
    # Looping pelos DFs do dic
    for key in diccp.keys():
        # print(key)
    
        # key = 'Campo Grande'
        
        dfi = diccp[key].copy()
        
        if exclusões != False:
            dfi_colunas_def = set(dfi.columns) - set(exclusões)
        else:
            dfi_colunas_def = set(dfi.columns)
        
        for str_coluna in dfi_colunas_def:
            # print(str_coluna)
        
            # str_coluna = 'RECEITAS CORRENTES (I)'
            
            coluna_deflacionada = dfi[str_coluna] * s_deflator
            coluna_deflacionada = coluna_deflacionada[~ coluna_deflacionada.isnull()]
            
            dfi[str_coluna] = coluna_deflacionada
        
        diccp[key] = dfi.copy()
    
    return diccp

# dic_deflacionado = deflaciona_dic(dic_muns, base='último', exclusões=['MR'], download=False)

# dic_deflacionado = deflaciona_dic(dic_muns, base='202008', exclusões=['MR'], download=False)


