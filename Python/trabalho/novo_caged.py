# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

SITE PARA DOWNLOAD

ftp://ftp.mtps.gov.br/pdet/microdados/

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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged2020' / 'temp'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

import pandas as pd
#############################
#############################
#############################

def extrai_arquivos():
    import glob
    import py7zr
    import os
    dicionario = {}
    print('Extraídos:')
    for arq_nome in glob.glob('*.7z'):
        with py7zr.SevenZipFile(arq_nome, mode='r') as z:
            z.extractall()
            print(f'  {arq_nome}')
        
extrai_arquivos()

def gera_serie():
    import glob
    lista = []
    for arq_nome in glob.glob('*.txt'):
        df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
        br = df['saldomovimentação'].sum()
    return br

soma = gera_serie()

##########################################################################################################
##########################################################################################################

caminho_mun = caminho_base / 'Dados'

df_estados = pd.read_excel(caminho_mun / 'estados.xlsx', sheet_name='estados')

print(df_estados.dtypes)
print(df_estados['uf_cod_ibge'].nunique())


##########################################################################################################
##########################################################################################################

caminho_mun = caminho_base / 'Dados'

df_municipios = pd.read_excel(caminho_mun / 'municipios.xlsx', sheet_name='municipios')

print(df_municipios.dtypes)
print(df_municipios['mun_cod_ibge'].nunique())

##########################################################################################################
##########################################################################################################
df_julho_antigo = pd.read_csv('julho_antigo.txt', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
print(df_julho_antigo['saldomovimentação'].sum())

df_julho_antigo = df_julho_antigo.rename(columns = {'uf': 'uf_cod_ibge'})

df_julho_antigo = pd.merge(df_julho_antigo, df_estados, how='left', on='uf_cod_ibge')

df_soma_estados = df_julho_antigo.groupby('uf_sigla')['saldomovimentação'].sum().to_frame()
df_soma_estados_T = df_soma_estados.T
df_soma_estados_T['br'] = df_soma_estados_T.sum(axis=1)

data = '2020-01-01'
data = pd.to_datetime(data)

df_soma_estados_T['data'] = data
df_soma_estados_T = df_soma_estados_T.set_index('data')
df_soma_estados_T.index.freq = 'MS' # MS = Monthly Start
print(df_soma_estados_T.index)

print(df_soma_estados_T['MS'])

##########################################################################################################
##########################################################################################################

df_soma_estados.index = str(df_soma_estados.index)
print(df_soma_estados.index)

df_soma_estados_resh = df_soma_estados.T

print(df_soma_estados_resh.index)

df.groupby('Company').mean()













data = '2020-01-01'
data = pd.to_datetime(data)


dados = {'variavel': 'x', 'br': [1], 'ms':[4]}
teste = pd.DataFrame.from_dict(dados)
teste.index = [data]

print(teste.index.freq)

teste.index.freq = 'MS' # MS = Monthly Start


print(teste.index)









data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)
   col_1 col_2
0      3     a
1      2     b
2      1     c
3      0     d
Specify orient='index' to create the DataFrame using dictionary keys as rows:

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data, orient='index')
       0  1  2  3
row_1  3  2  1  0
row_2  a  b  c  d


mylist = [10, 20, 30]
labels = ['a', 'b', 'c']

np_arr = np.array(mylist)
pd_series = pd.Series(data = mylist)
pd_series = pd.Series(data = mylist, index = labels)










df8 = pd.read_csv('CAGEDMOV202008.txt', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
del df8

df7 = pd.read_csv('CAGEDMOV202007.txt', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
print(df7['saldomovimentação'].sum())



df_julho_velho = pd.read_csv('julho_velho.txt', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)


print(df_julho_velho['saldomovimentação'].sum())



df = df1.append(df8, ignore_index=True)

print(df8['saldomovimentação'].sum())

import os
os.remove("CAGEDMOV202001.txt")




del df7
del df_julho_velho










def gera_df(nome_zip):
    import zipfile
    import lzma
    import io
    import pandas as pd
    with lzma.open(nome_zip, 'r') as zf:
        csv_nome = zf.namelist()[0]
        with io.TextIOWrapper(zf.open(csv_nome), encoding="latin") as f:
            f_contents = f.readline()
            lista = [f_contents]
            contador = 0
            while f_contents.find(';') == -1:
                contador += 1
                f_contents = f.readline()
                lista.append(f_contents)
    df = pd.read_csv(nome_zip, compression='zip', header=0, sep=';', decimal=',', quotechar='"', encoding = 'latin', skiprows=contador)
    

    return df


df = gera_df('CAGEDMOV202001.7z')


import lzma
with lzma.open("CAGEDMOV202001.7z", "r") as f:
    df = pd.read_csv(f, compression='zip', header=0, sep=';', decimal=',', quotechar='"', encoding = 'latin', skiprows=contador)


import pandas as pd
import lzma
with lzma.open("CAGEDMOV202001.7z", "r") as f:
    df = pd.read_csv(f, header=0, compression='xz', sep=';', decimal=',', quotechar='"', encoding = 'latin', skiprows=0)




import py7zr
with py7zr.SevenZipFile('CAGEDMOV202001.7z', mode='r') as z:
    df = pd.read_csv(z.unpack_7zarchive(), header=0, compression='xz', sep=';', decimal=',', quotechar='"', encoding = 'latin', skiprows=0)

import libarchive.public


pip install libarchive.public


print(dir(py7zr))



df = dd.read_csv('CAGEDMOV202001.7z', storage_options={'compression': 'xz'},
                 blocksize=None)


pip install libarchive


import lzma
with lzma.open("CAGEDMOV202001.7z") as f:
    file_content = f.read()

















































