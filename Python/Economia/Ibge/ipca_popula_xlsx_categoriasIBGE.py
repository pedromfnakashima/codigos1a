# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:47:57 2020

@author: pedro

Pega categorias e popula o arquivo
D:\Códigos, Dados, Documentação e Cheat Sheets\Dados\Ibge\Ipca\
    categoriasIBGE.xlsx

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

import pandas as pd
##########################################################################################################
############################# Gerador de datas #####################################################
##########################################################################################################

def g_li_datas_ibge(início, final):
    if início == final:
        str_dt_ibge = início.replace('-','')
        li_meses = [str_dt_ibge]
    else:
        import numpy as np
        from datetime import datetime
        import pandas as pd
        ano_início = int(início.split('-')[0])
        mês_início = int(início.split('-')[1])
        ano_final = int(final.split('-')[0])
        mês_final = int(final.split('-')[1])
        data1 = datetime(ano_início, mês_início, 1)
        data2 = datetime(ano_final, mês_final, 1) + pd.DateOffset(months=1)
        np_meses = np.arange(data1,data2, 1, dtype='datetime64[M]').astype(str)
        li_meses = [s.replace('-','') for s in np_meses]
    return li_meses

li_meses = g_li_datas_ibge('2020-01', '2020-01')

##########################################################################################################
########################### Gera correspondências código-descrição #####################################################
##########################################################################################################

##################################### TABELA 7060 #####################################
'''
Tabelas só com os pesos:


2938 (200607 - 201112):
1419 (201201 - 201912):
7060 (202001 -): https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/66/p/202002/c315/all/d/v66%204
'''
# mês = '202001'
# tabela = '7060'

def g_dic_categorias(tabela, mês, variável):
    
    import requests
    
    # variável = 'peso'
    # mês = '202001'
    # tabela = '7060'
    
    if variável == 'peso':
        url = f'https://apisidra.ibge.gov.br/values/t/{tabela}/n1/all/v/66/p/{mês}/c315/all/d/v66%204'
    elif variável == 'variação':
        url = f'https://apisidra.ibge.gov.br/values/t/{tabela}/n1/all/v/63/p/{mês}/c315/all/d/v66%204'
    
    r = requests.get(url)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
        
    df = df.groupby(['D4N']).head(1)
    df = df.loc[:,['D4N']]
    
    for index_linha, linha in df.iterrows():
        try: # Roda o seguinte código
            df.loc[index_linha,'código'] = linha['D4N'].split(".")[0]    
            df.loc[index_linha,'descrição'] = linha['D4N'].split(".")[1]
        except IndexError:  # Executa esse código quando há a exceção
            import re
            is_match = bool(re.match('^índice', df.loc[index_linha,'D4N'], re.IGNORECASE))
            if is_match == True:
                df.loc[index_linha,'descrição'] = 'Índice geral'
                df.loc[index_linha,'código'] = '0'
            else:
                df.loc[index_linha,'descrição'] = ''
        else:  # se não há exceção, roda esse código
            pass
        finally: # sempre roda esse código
            pass
    
    df.drop([0],axis=0,inplace=True)
    
    df['tabela'] = tabela
    df['início'] = pd.to_datetime(mês, format='%Y%m')
    
    cond1 = df['código'] == '0'
    cond = cond1
    df.loc[cond1,'categoria'] = 'Geral'
    
    cond1 = df['código'].str.len() == 1
    cond2 = df['código'] != '0'
    cond = cond1 & cond2
    df.loc[cond,'categoria'] = 'Grupo'
    
    cond1 = df['código'].str.len() == 2
    df.loc[cond1,'categoria'] = 'Subgrupo'
    
    cond1 = df['código'].str.len() == 4
    df.loc[cond1,'categoria'] = 'Item'
    
    cond1 = df['código'].str.len() == 7
    df.loc[cond1,'categoria'] = 'Subitem'
    
    # Coloca em dicionário
    li_categorias = ['Grupo','Subgrupo','Item','Subitem']
    
    dic_categorias = {}
    
    for categoria in li_categorias:
        
        # categoria = 'Subgrupo'
        
        cond1 = df['categoria'] == categoria
        df_categoria = df.loc[cond1,:]
        
        df_categoria = df_categoria.groupby(['código']).head(1)
        
        dic_categorias[categoria] = df_categoria
        
        dic_categorias[categoria] = dic_categorias[categoria].loc[:,['tabela','início','código','descrição']]
        
        #dic_categorias[categoria].set_index(['tabela','código'],inplace=True)
    
    return dic_categorias

# Adiciona dicionários ao dicionário dic_dics
dic_dics = {}
dic_dics['2938'] = g_dic_categorias('2938', '200607', 'peso')
dic_dics['1419'] = g_dic_categorias('1419', '201201', 'peso')
dic_dics['7060'] = g_dic_categorias('7060', '202001', 'peso')

# Grupo
df_Grupo = dic_dics['2938']['Grupo'].copy()
df_Grupo = df_Grupo.append(dic_dics['1419']['Grupo'])
df_Grupo = df_Grupo.append(dic_dics['7060']['Grupo'])
df_Grupo.sort_values(['código','início'],ascending=[True,False],inplace=True)
df_Grupo = df_Grupo.groupby(['código']).head(1)

# Subgrupo
df_Subgrupo = dic_dics['2938']['Subgrupo'].copy()
df_Subgrupo = df_Subgrupo.append(dic_dics['1419']['Subgrupo'])
df_Subgrupo = df_Subgrupo.append(dic_dics['7060']['Subgrupo'])
df_Subgrupo.sort_values(['código','início'],ascending=[True,False],inplace=True)
df_Subgrupo = df_Subgrupo.groupby(['código']).head(1)

# Item
df_Item = dic_dics['2938']['Item'].copy()
df_Item = df_Item.append(dic_dics['1419']['Item'])
df_Item = df_Item.append(dic_dics['7060']['Item'])
df_Item.sort_values(['código','início'],ascending=[True,False],inplace=True)
df_Item = df_Item.groupby(['código']).head(1)

# Subitem
df_Subitem = dic_dics['2938']['Subitem'].copy()
df_Subitem = df_Subitem.append(dic_dics['1419']['Subitem'])
df_Subitem = df_Subitem.append(dic_dics['7060']['Subitem'])
df_Subitem.sort_values(['código','início'],ascending=[True,False],inplace=True)
df_Subitem = df_Subitem.groupby(['código']).head(1)

###################################################################################################
############################# POPULA ARQUIVO categoriasIBGE.xlsx (NOVO) ######################################
###################################################################################################

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = "categoriasIBGE.xlsx"

with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
    df_Grupo.to_excel(writer, sheet_name='Grupo', index=False)

with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
    df_Subgrupo.to_excel(writer, sheet_name='Subgrupo', index=False)

with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
    df_Item.to_excel(writer, sheet_name='Item', index=False)
    
with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
    df_Subitem.to_excel(writer, sheet_name='Subitem', index=False)



###################################################################################################
############################# POPULA ARQUIVO categoriasIBGE.xlsx (VELHO-DESATIVADO) ######################################
###################################################################################################
li_dics_nums = ['2938','1419','7060']

li_categorias = ['Grupo','Subgrupo','Item','Subitem']

for dic_i_num in li_dics_nums:
    # print(dic_i_num)

    # dic_i_num = li_dics[0]
    dic_i = dic_dics[dic_i_num]
    
    for categoria_i in li_categorias:
        # categoria_i = li_categorias[0]
        
        sheet_name = 't' + dic_i_num + '_' + categoria_i
        
        
        # pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
        pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
        arq_nome = "categoriasIBGE.xlsx"
        with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
            dic_i[categoria_i].to_excel(writer, sheet_name=sheet_name, index=True)
















