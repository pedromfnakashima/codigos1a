# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 07:25:59 2020

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
import numpy as np
import pandas as pd

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


##########################################################################################################
##########################################################################################################
##########################################################################################################

def ipca():
    
    import numpy as np
    import pandas as pd
    
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela', skiprows=0)
    

    df_ipca.drop(df_ipca.tail(1).index,inplace=True)
    
    df_ipca['year'] = df_ipca['Mês'].str.split(' ').str.get(1).astype('int')
    df_ipca['month_str'] = df_ipca['Mês'].str.split(' ').str.get(0)
    
    df_ipca.drop(['Mês'], axis=1, inplace=True)
    
    li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    for index, mês in enumerate(li_meses, start=1):
        cond1 = df_ipca['month_str'] == mês
        df_ipca.loc[cond1, 'month'] = index
    
    df_ipca['day'] = 1
    
    df_ipca.drop(['month_str'], axis=1, inplace=True)

    df_ipca['data'] = pd.to_datetime(df_ipca[['year', 'month', 'day']])
    df_ipca.set_index('data', inplace=True)
    df_ipca.index.freq = 'MS'
    
    df_ipca.rename(columns={'índice':'Índice'}, inplace=True)
    
    df_ipca.drop(['year','month','day'], axis=1, inplace=True)
    
    return df_ipca


df_ipca = ipca()

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











