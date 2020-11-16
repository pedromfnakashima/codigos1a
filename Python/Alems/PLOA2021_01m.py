# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:31:40 2020

@author: pedro
"""

########################### IPCA #########################################
def g_deflator(base = 'último'):
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
    df_ipca.index.freq = 'MS'
    
    if base == 'último':
        base_escolhida = df_ipca.loc[df_ipca.index.max(), 'Índice']
    else:
        base = '2020-08-01'
        cond = df_ipca.index == base
        filtro = df_ipca.loc[cond, :]
        filtro.reset_index(inplace=True)
        base_escolhida = filtro.loc[0,'Índice']
    
    df_ipca['deflator'] = base_escolhida / df_ipca['Índice']
    df_ipca = df_ipca['deflator']
    return df_ipca

df_ipca = g_deflator()
df_ipca = g_deflator(base='2020-08-01')

##########################################################################

def deflaciona_dic(dic, base = 'último'):
    
    df_ipca = g_deflator(base=base)
    
    dic_series_mensais = dic.copy()
    
    for key in dic_series_mensais.keys():
        print(key)

        
        dic_series_mensais[key] = dic_series_mensais[key].mul(df_ipca, axis=0)
        
        dic_series_mensais[key].dropna(axis=0, thresh=1, inplace=True)
        
    return dic_series_mensais


dic_series_mensais = g_series_mensais() # arquivo PLOA2021_01l.py

dicionario_deflacionado = deflaciona_dic(dic=dic_series_mensais, base='2020-08-01')

dicionario_deflacionado = deflaciona_dic(dic=dic_series_mensais)













