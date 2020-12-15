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

pip install -U sidrapy

import sidrapy

data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="last 12")

data_7060 = sidrapy.get_table(table_code="7060", territorial_level="1", ibge_territorial_code="all", period="all")

data_1737 = sidrapy.get_table(table_code="1737", territorial_level="1", ibge_territorial_code="all", period="all", variable='all')

print(dir(sidrapy.get_table))

help(sidrapy.get_table)

# Tabela - tabela7060
# Tabela - tabela1737


# arq_nome = 'tabela3065.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
# df = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)



def g_col_data(coluna):
    
    cond1 = coluna.isnull()
    coluna.loc[cond1] = ''
    
    month = np.zeros(len(coluna))
    year = np.zeros(len(coluna))
    day = np.ones(len(coluna))
    
    import re
    li_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    for index_mês, mês in enumerate(li_meses, start=1):
        for index_col, col in enumerate(coluna):
            matched = re.match(mês, col)
            is_match = bool(matched)
            #print(is_match)
            if is_match == True:
                month[index_col] = index_mês
    
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
            #print(is_match)
            if is_match == True:
                month[index_col] = 0
                year[index_col] = 0
                day[index_col] = 0
    
    df_data = pd.DataFrame({'year':year,'month':month,'day':day})
    
    df_data['dt'] = pd.to_datetime(df_data[['year', 'month', 'day']],errors='coerce')
    
    df_data = df_data['dt']
    
    return df_data

#coluna_dt_str = df.iloc[:,0]

#col_dt = g_col_data(coluna_dt_str)

#df['dt'] = g_col_data(coluna_dt_str)

#cond1 = ~ df['dt'].isnull()
#df = df.loc[cond1,:]

##########################################################################################################
##########################################################################################################
##########################################################################################################


# arq_nome = 'tabela3065.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca-15'
# df_ipca15 = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# # -------------------------------------------------------------------------------
# arq_nome = 'tabela1737.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
# df_ipca = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# # -------------------------------------------------------------------------------
# arq_nome = 'tabela1736.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Inpc'
# df_inpc = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# # -------------------------------------------------------------------------------
# arq_nome = 'tabela6903.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
# df_ipp = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)

# # -------------------------------------------------------------------------------
# arq_nome = 'tabela6903_2.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
# df_ipp_grande = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)

#coluna_dt_str = df.iloc[:,0]
#coluna = coluna_dt_str.copy()


def g_df_com_data(df, colMês, colVar, nomeVar):
    
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
    nome_antigo_valor = li_colunas[colVar]
    nome_antigo_mês = li_colunas[colMês]
    
    df_cp.rename(mapper={nome_antigo_valor:nomeVar},axis=1,inplace=True)
    
    coluna = df_cp.iloc[:,colMês]
    cond1 = coluna.isnull()
    coluna.loc[cond1] = ''
    
    df_cp[nome_antigo_mês] = g_col_data(coluna)
    df_cp.rename(mapper={nome_antigo_mês:'dt'},axis=1,inplace=True)
    
    
    cond1 = ~ df_cp['dt'].isnull()
    df_cp = df_cp.loc[cond1,:]
    
    df_cp = df_cp.iloc[:, [colMês,colVar]]
    df_cp.set_index('dt',inplace=True)
    
    df_cp[nomeVar] = pd.to_numeric(df_cp[nomeVar], errors='coerce')
    
    return df_cp

#col_dt = g_col_data(coluna_dt_str)

# df_ipca15 = g_df_com_data(df_ipca15, colMês=0, colVar=2, nomeVar='IPCA15')
# df_ipca = g_df_com_data(df_ipca, colMês=0, colVar=1, nomeVar='IPCA')
# df_inpc = g_df_com_data(df_inpc, colMês=1, colVar=2, nomeVar='INPC')
# df_ipp = g_df_com_data(df_ipp, colMês=1, colVar=2, nomeVar='IPP')


# df = df_ipca.merge(df_ipca15,how='outer',left_index=True,right_index=True)
# df = df.merge(df_inpc,how='outer',left_index=True,right_index=True)
# df = df.merge(df_ipp,how='outer',left_index=True,right_index=True)
# del df_ipca, df_ipca15, df_inpc, df_ipp

##########################################################################################################
##########################################################################################################
##########################################################################################################

# -------------------------------------------------------------------------------
# arq_nome = 'tabela6903_2.xlsx'
# pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
# df = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
# coluna_dt_str = df_ipp_grande.iloc[:,1]
# df_ipp_grande['dt'] = g_col_data(coluna_dt_str)
# -------------------------------------------------------------------------------

def g_df_com_data_2(df, colCategorias, colMês, colVar):
    
    # colMês: o número da coluna que tem o mês no formato IBGE
    
    # colCategorias = 1
    # colMês = 2
    # colVar = 3

    # -------------------------------------------------------------------------------
    # arq_nome = 'tabela6903_2.xlsx'
    # pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
    # df_cp = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
    # coluna_dt_str = df_cp.iloc[:,1]
    # df_cp['dt'] = g_col_data(coluna_dt_str)
    # -------------------------------------------------------------------------------
    
    import numpy as np
    import pandas as pd
    
    df_cp = df.copy()
    
    colunas = df_cp.columns
    
    nome_antigo_valor = colunas[colVar]
    nome_antigo_categoria = colunas[colCategorias]
    
    
    coluna_dt_str = df_cp.iloc[:,colMês]
    df_cp['dt'] = g_col_data(coluna_dt_str)

    cond1 = ~ df_cp['dt'].isnull()
    df_cp = df_cp.loc[cond1,:]
    df_cp[nome_antigo_categoria].fillna(method='ffill', inplace=True)
    
    li_categorias = df_cp[nome_antigo_categoria].unique()
    
    #col1_str = 'Tabela 6903 - Índice de Preços ao Produtor, por tipo de índice, indústria geral, indústrias extrativas e indústrias de transformação e atividades (dezembro de 2018 = 100)'
    
    # li_categorias = df_cp[col1_str].unique()
    
    
    #colVar = 2
    
    # colunas = df_cp.columns
    
    # nome_antigo_valor = colunas[colVar]
    
    # nomeVar='Valor'
    
    #df_cp.rename(mapper={nome_antigo_valor:nomeVar},axis=1,inplace=True)
    
    
    df_cp[nome_antigo_valor] = pd.to_numeric(df_cp[nome_antigo_valor], errors='coerce')
    
    
    for index_unico, categoria_str in enumerate(li_categorias):
        #print(index_unico, unico_str)
        
        # index_unico = 0
        # categoria_str = 'Indústria Geral'
        
        cond1 = df_cp.iloc[:,colCategorias] == categoria_str
        filtro = df_cp.loc[cond1,:]
        
        filtro.rename(mapper={nome_antigo_valor:categoria_str},axis=1,inplace=True)
        
        filtro = filtro.loc[:,['dt', categoria_str]]
        
        filtro.set_index('dt',inplace=True)
        
        if index_unico == 0:
            df_completo = filtro.copy()
        else:
            df_completo = df_completo.merge(filtro,how='outer',left_index=True,right_index=True)

    
    return df_completo

# colCategorias = 0
# colMês = 1
# colVar = 2

# ipp_categorias = g_df_com_data_2(df, colCategorias=0, colMês=1, colVar=2)




##########################################################################################################
##########################################################################################################
##########################################################################################################
# IPCA por categorias

arq_nome = 'tabela7060.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df = pd.read_excel(pasta / arq_nome, sheet_name=0, skiprows=0)

colCategorias_VmVp = 1
colCategorias_Grupo = 2
colMês = 3
colVar = 4


import numpy as np
import pandas as pd

df_cp = df.copy()

colunas = df_cp.columns

nome_antigo_valor = colunas[colVar]
nome_antigo_data = colunas[colMês]
nome_antigo_categoria_VmVp = colunas[colCategorias_VmVp]
nome_antigo_categoria_Grupo = colunas[colCategorias_Grupo]

# Pega apenas colunas que têm a data
coluna_dt_str = df_cp.loc[:,nome_antigo_data]
df_cp['dt'] = g_col_data(coluna_dt_str)
cond1 = ~ df_cp['dt'].isnull()
df_cp = df_cp.loc[cond1,:]

# Espalha para baixo os valores
df_cp[nome_antigo_categoria_VmVp].fillna(method='ffill', inplace=True)
df_cp[nome_antigo_categoria_Grupo].fillna(method='ffill', inplace=True)

li_categorias_VmVp = df_cp[nome_antigo_categoria_VmVp].unique()
li_categorias_Grupo = df_cp[nome_antigo_categoria_Grupo].unique()

# Assegura que o valor é numérico
df_cp[nome_antigo_valor] = pd.to_numeric(df_cp[nome_antigo_valor], errors='coerce')

# Cria o dicionário
dicionário1 = {}

index_unico = 0
categoria_VmVp_str = 'IPCA - Variação mensal (%)'

# Cria colunas com os códigos das categorias (usando regex)


def retorna_código_e_desc(texto):
    import re
    matches = re.search('^\d+', texto)
    é_índice = bool(re.match('índice', texto, re.IGNORECASE))
    posição_início = texto.find('.') + 1 # posição do ponto mais 1
    if matches != None:
        #print(matches.group(0))
        cód = matches.group(0)
        str_texto = texto[posição_início:]
    elif é_índice == True:
        #print('é índice')
        cód = '0'
        str_texto = texto
    else:
        #print('outra coisa')
        cód = ''
        str_texto = ''
    return cód, str_texto


# txt = '1.Alimentação e bebidas'
# txt = '1101.Cereais, leguminosas e oleaginosas'
# txt = 'Índice geral'
# txt = 'asfsdf'

# cód1, texto1 = retorna_código_e_desc(txt)
# print(f'Código: {cód1}; Texto: {texto1}')

import pandas as pd

for index_linha, linha in df_cp.iterrows():
    #print(linha[nome_antigo_categoria_Grupo])
    código, descrição = retorna_código_e_desc(linha[nome_antigo_categoria_Grupo])
    #print(cód1)
    df_cp.loc[index_linha,'código'] = código
    df_cp.loc[index_linha,'descrição'] = descrição

# Classifica as entradas como Geral, Grupo, Subgrupo, Item, Subitem
cond1 = df_cp['código'] == '0'
cond = cond1
df_cp.loc[cond1,'categoria'] = 'Geral'

cond1 = df_cp['código'].str.len() == 1
cond2 = df_cp['código'] != '0'
cond = cond1 & cond2
df_cp.loc[cond,'categoria'] = 'Grupo'

cond1 = df_cp['código'].str.len() == 2
df_cp.loc[cond1,'categoria'] = 'Subgrupo'

cond1 = df_cp['código'].str.len() == 4
df_cp.loc[cond1,'categoria'] = 'Item'

cond1 = df_cp['código'].str.len() == 7
df_cp.loc[cond1,'categoria'] = 'Subitem'

# Tabelas com as descrições e códigos

li_categorias = ['Grupo','Subgrupo','Item','Subitem']

# GRUPOS

dicionário2 = {}

for categoria in li_categorias:
    #categoria = 'Subgrupo'
    
    cond1 = df_cp['categoria'] == categoria
    df_categoria = df_cp.loc[cond1,:]
    
    df_categoria = df_categoria.groupby(['código']).head(1)
    
    dicionário2[categoria] = df_categoria








import re
texto = 'Índice geral'
matches = re.search('^\d+', texto)
é_índice = bool(re.match('índice', texto, re.IGNORECASE))
#print(is_match)
if é_índice == True:
    print('É índice!!!!')






df_cp['categoria_cod'] = df_cp[nome_antigo_categoria_Grupo].str.




# Filtra por Variação Mensal ou Peso no Mês

cond1 = df_cp.iloc[:,colCategorias_VmVp] == categoria_VmVp_str
df_categoria_VmVp = df_cp.loc[cond1,:]

# 









# Muda o formato do DF
for index_unico, categoria_VmVp_str in enumerate(li_categorias_VmVp):
    print(index_unico, categoria_VmVp_str)
    
    # index_unico = 0
    # categoria_str = 'Indústria Geral'











##########################################################################################################
##########################################################################################################
##########################################################################################################

















print(df_ipp_grande.dtypes)

# -------------------------------------------------------------------------------
arq_nome = 'tabela6903_2.xlsx'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipp'
df_ipp_grande = pd.read_excel(pasta / arq_nome, sheet_name='Tabela', skiprows=0)
coluna_dt_str = df_ipp_grande.iloc[:,1]
df_ipp_grande['dt'] = g_col_data(coluna_dt_str)
# -------------------------------------------------------------------------------

cond1 = ~ df_ipp_grande['dt'].isnull()
df_ipp_grande = df_ipp_grande.loc[cond1,:]
df_ipp_grande[col1_str].fillna(method='ffill', inplace=True)

col1_str = 'Tabela 6903 - Índice de Preços ao Produtor, por tipo de índice, indústria geral, indústrias extrativas e indústrias de transformação e atividades (dezembro de 2018 = 100)'

li_categorias = df_ipp_grande[col1_str].unique()


colVar = 2

colunas = df_ipp_grande.columns

nome_antigo_valor = colunas[colVar]

nomeVar='Valor'

#df_ipp_grande.rename(mapper={nome_antigo_valor:nomeVar},axis=1,inplace=True)


df_ipp_grande[nome_antigo_valor] = pd.to_numeric(df_ipp_grande[nome_antigo_valor], errors='coerce')


for index_unico, unico_str in enumerate(li_categorias):
    print(index_unico, unico_str)

    categoria_str = 'Indústria Geral'
    cond1 = df_ipp_grande.iloc[:,0] == unico_str
    filtro = df_ipp_grande.loc[cond1,:]
    
    filtro.rename(mapper={nome_antigo_valor:categoria_str},axis=1,inplace=True)
    
    filtro = filtro.loc[:,['dt', categoria_str]]
    
    filtro.set_index('dt',inplace=True)
    
    if index_unico == 0:
        df_completo = filtro.copy()
    else:
        df_completo = df_completo.merge(filtro,how='outer',left_index=True,right_index=True)












li_categorias = df_ipp_grande[col1_str].unique()
for index_unico, unico_str in enumerate(li_categorias):
    print(index_unico, unico_str)
    
    
    
    cond1 = df_ipp_grande.iloc[0] == index_unico











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











