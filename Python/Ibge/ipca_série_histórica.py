# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 07:25:59 2020

@author: pedro-salj

TABELAS
- tabela1737:
IPCA - Série histórica com número-índice, variação mensal e
variações acumuladas em 3 meses, em 6 meses, no ano e em 12 meses (a partir de dezembro/1979)
- tabela3065:
IPCA15 - Série histórica com número-índice, variação mensal e variações
acumuladas em 3 meses, em 6 meses, no ano e em 12 meses (a partir de maio/2000)


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
caminho_wd = caminho_base / 'Dados' / 'Firjan'
os.chdir(caminho_wd)
import numpy as np
import pandas as pd


##########################################################################################################
##########################################################################################################
##########################################################################################################

arq_nome = 'tabela3065.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
df_ipca15 = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# -------------------------------------------------------------------------------
arq_nome = 'tabela1737.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# -------------------------------------------------------------------------------
arq_nome = 'tabela1736.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Inpc'
df_inpc = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# -------------------------------------------------------------------------------
arq_nome = 'tabela6903.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
df_ipp = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)

# -------------------------------------------------------------------------------
arq_nome = 'tabela6903_2.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
df_ipp_grande = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)

#coluna_dt_str = df.iloc[:,0]
#coluna = coluna_dt_str.copy()


def g_col_data(df, colMês, colVar, nomeVar):
    
    # colMês: o número da coluna que tem o mês no formato IBGE
    
    #colMês = 1
    #colVar = 2
    #nomeVar='Índice'
    # -------------------------------------------------------------------------------
    #pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
    #arq_nome = 'tabela3065.xlsx'
    #df = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
    # -------------------------------------------------------------------------------
    #arq_nome = 'tabela1736.xlsx'
    #pasta = caminho_base / 'Dados' / 'Ibge' / 'Inpc'
    #df = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
    # -------------------------------------------------------------------------------
    
    import numpy as np
    import pandas as pd
    
    df_cp = df.copy()
    
    li_colunas = df_cp.columns
    nome_antigo_índice = li_colunas[colVar]
    nome_antigo_mês = li_colunas[colMês]
    
    df_cp.rename(mapper={nome_antigo_índice:nomeVar},axis=1,inplace=True)
    
    coluna = df_cp.iloc[:,colMês]
    cond1 = coluna.isnull()
    coluna.loc[cond1] = ''
    
    
    month = np.zeros(len(coluna))
    year = np.zeros(len(coluna))
    day = np.ones(len(coluna))
    
    #str_mês_pt = 'janeiro'
    #mês_e_ano = np.nan
    
    import re
    li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    for index_mês, str_mês_pt in enumerate(li_meses, start=1):
        #print(index_mês, str_mês_pt)
        for index_mês_e_ano, mês_e_ano in enumerate(coluna):
            #print(index_mês_e_ano, mês_e_ano)
            matched = re.match(str_mês_pt, mês_e_ano)
            is_match = bool(matched)
            #print(is_match)
            if is_match == True:
                month[index_mês_e_ano] = index_mês
    
    index_z1 = -1
    for col_dt, ano in zip(coluna, month):
        index_z1 += 1
        encontrado = re.search(r'\d{4}', col_dt, re.IGNORECASE)
        if encontrado != None:
            ano = encontrado.group(0)
            year[index_z1] = ano
    
    li_zerar = ['Variável','Mês', 'Fonte']
    for index_li_zerar, zerar in enumerate(li_zerar, start=1):
        for index_col, col in enumerate(coluna):
            matched = re.match(zerar, col)
            is_match = bool(matched)
            if is_match == True:
                month[index_col] = 0
                year[index_col] = 0
                day[index_col] = 0
    
    df_cp_data = pd.DataFrame({'year':year,'month':month,'day':day})
    
    df_cp_data['dt'] = pd.to_datetime(df_cp_data[['year', 'month', 'day']],errors='coerce')
    
    
    df_cp[nome_antigo_mês] = df_cp_data['dt']
    df_cp.rename(mapper={nome_antigo_mês:'dt'},axis=1,inplace=True)
    
    
    cond1 = ~ df_cp['dt'].isnull()
    df_cp = df_cp.loc[cond1,:]
    
    df_cp = df_cp.iloc[:, [colMês,colVar]]
    df_cp.set_index('dt',inplace=True)
    
    df_cp[nomeVar] = pd.to_numeric(df_cp[nomeVar], errors='coerce')
    
    return df_cp

#col_dt = g_col_data(coluna_dt_str)

df_ipca15 = g_col_data(df_ipca15, colMês=0, colVar=2, nomeVar='IPCA15')
df_ipca = g_col_data(df_ipca, colMês=0, colVar=1, nomeVar='IPCA')
df_inpc = g_col_data(df_inpc, colMês=1, colVar=2, nomeVar='INPC')
df_ipp = g_col_data(df_ipp, colMês=1, colVar=2, nomeVar='IPP')


df = df_ipca.merge(df_ipca15,how='outer',left_index=True,right_index=True)
df = df.merge(df_inpc,how='outer',left_index=True,right_index=True)
df = df.merge(df_ipp,how='outer',left_index=True,right_index=True)
del df_ipca, df_ipca15, df_inpc, df_ipp

##########################################################################################################
##########################################################################################################
##########################################################################################################

























##########################################################################################################
##########################################################################################################
##########################################################################################################


pasta = caminho_wd = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela', skiprows=0)

print(df_ipca.columns)

#df_ipca.rename(columns={'IPCA - Número-índice (base: dezembro de 1993 = 100) (Número-índice)':'índice'}, inplace=True)
#df_ipca.drop(['Unnamed: 0'], axis=1, inplace=True)
df_ipca.drop(df_ipca.tail(1).index,inplace=True)

df_ipca['year'] = df_ipca['Mês'].str.split(' ').str.get(1).astype('int')
df_ipca['month_str'] = df_ipca['Mês'].str.split(' ').str.get(0)

df_ipca.drop(['Mês'], axis=1, inplace=True)

li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for index, mês in enumerate(li_meses, start=1):
    print(index, mês)
    cond1 = df_ipca['month_str'] == mês
    df_ipca.loc[cond1, 'month'] = index

df_ipca['day'] = 1

df_ipca.drop(['month_str'], axis=1, inplace=True)
'''
Construindo datetime a partir dos componentes.
As colunas devem se chamar: year, month, day
E devem estar no formato numérico
'''
df_ipca['data'] = pd.to_datetime(df_ipca[['year', 'month', 'day']])
df_ipca.set_index('data', inplace=True)
df_ipca.index.freq = 'MS'

df_ipca.drop(['year','month','day'], axis=1, inplace=True)


df_ipca['L1_índice'] = df_ipca['índice'].shift(1)
df_ipca['vm_ipca'] = ((df_ipca['índice'] / df_ipca['L1_índice'])-1)*100


df_ipca['vm_ipca'].plot()


















arq_nome = 'tabela3065.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
df = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
coluna_dt_str = df.iloc[:,0]

month = np.zeros(len(coluna_dt_str))
year = np.zeros(len(coluna_dt_str))
day = np.ones(len(coluna_dt_str))

import re
li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for index_mês, mês in enumerate(li_meses, start=1):
    for index_col, col in enumerate(coluna_dt_str):
        matched = re.match(mês, col)
        is_match = bool(matched)
        #print(is_match)
        if is_match == True:
            month[index_col] = index_mês

index_z1 = -1
for col_dt, ano in zip(coluna_dt_str, coluna_ano):
    index_z1 += 1
    encontrado = re.search(r'\d{4}', col_dt, re.IGNORECASE)
    if encontrado != None:
        ano = encontrado.group(0)
        year[index_z1] = ano

li_zerar = ['Variável','Mês', 'Fonte']
for index_li_zerar, zerar in enumerate(li_zerar, start=1):
    for index_col, col in enumerate(coluna_dt_str):
        matched = re.match(zerar, col)
        is_match = bool(matched)
        #print(is_match)
        if is_match == True:
            month[index_col] = 0
            year[index_col] = 0
            day[index_col] = 0

df_data = pd.DataFrame({'year':year,'month':month,'day':day})

df_data['dt'] = pd.to_datetime(df_data[['year', 'month', 'day']],errors='coerce')

df_data = df_data['dt']






import re
texto = 'agosto 2000'
padrao = re.compile(r'\d{4}')
matches = padrao.finditer(texto)
print(matches.)
















title_search = re.search(r'\d{4}', texto, re.IGNORECASE)

if title_search:
    txt_encontrado = title_search.group(1)





title_search = re.search('<title>(.*)</title>', html, re.IGNORECASE)

if title_search:
    title = title_search.group(1)


encontrado = re.search(r'\d{4}', texto, re.IGNORECASE)
if encontrado != None:
    ano = encontrado.group(0)
    print(ano)




print(title_search.group(0))

if title_search:
    title = title_search.group(0)









print(dir(matches))

print(matches.group(0))


match = matches.group(0)

print(matches.match)

for match in matches:
    print(match.group(0))





import re

test_string = 'a1b2cdefg'

matched = re.match("[a-z][0-9][a-z][0-9]+", test_string)
is_match = bool(matched)

print(is_match)





        


str1 = pd.Series('maio 2000')
print(str1.str.match('janeiro'))


array_qtd_meses_coluna = list(range(len(coluna_dt_str)))
df_out = pd.DataFrame(array_qtd_meses_coluna)
df_out.set_index(0,inplace=True)
df_out = df_out.merge(coluna_dt_str,how='left',left_index=True,right_index=True)




print(len(coluna_dt_str))

li_meses = np.array(['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'])
mês = li_meses[0]

cond1 = coluna_dt_str.str.contains(mês)



print(array_qtd_meses_coluna)



li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for index, mês in enumerate(li_meses, start=1):
    cond1 = df_ipca['month_str'] == mês
    df.loc[cond1, 'month'] = index




def ipca_índice(arq_nome):
    
    import numpy as np
    import pandas as pd
    
    arq_nome = 'tabela3065.xlsx'
    
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
    df = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
    
    print(df.iloc[:,0:3])
    coluna_dt_str = df.iloc[:,0]
    

    df.drop(df.tail(1).index,inplace=True)
    
    df['year'] = df['Mês'].str.split(' ').str.get(1).astype('int')
    df['month_str'] = df['Mês'].str.split(' ').str.get(0)
    
    df.drop(['Mês'], axis=1, inplace=True)
    
    li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    for index, mês in enumerate(li_meses, start=1):
        cond1 = df_ipca['month_str'] == mês
        df.loc[cond1, 'month'] = index
    
    df['day'] = 1
    
    df.drop(['month_str'], axis=1, inplace=True)

    df['data'] = pd.to_datetime(df_ipca[['year', 'month', 'day']])
    df.set_index('data', inplace=True)
    df.index.freq = 'MS'
    
    df.rename(columns={'índice':'Índice'}, inplace=True)
    
    df.drop(['year','month','day'], axis=1, inplace=True)
    
    return df


df_ipca = ipca_índice()

import pandas as pd
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
with pd.ExcelWriter(pasta / 'tabela1737.xlsx', mode='a', engine="openpyxl") as writer:  
    df_ipca.to_excel(writer, sheet_name='Tabela_com_datas', index=True)

#########################################################

pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'

#########################################################

df_ipca['mês'] = df_ipca.index.month
df_ipca['ano'] = df_ipca.index.year

cond = df_ipca['mês'] == 10
df_ipca = df_ipca.loc[cond,:]

df_ipca.drop(['mês'], axis=1, inplace=True)











