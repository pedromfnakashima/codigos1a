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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'temp'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

##########################################################################################################
##########################################################################################################
##########################################################################################################

def gera_df():

    import pandas as pd
    df_estados_siglas = pd.read_excel(caminho_base / 'dados' / 'estados.xlsx', sheet_name='estados')
    
    import glob
    import pandas as pd
    df_estados_siglas = pd.read_excel(caminho_base / 'dados' / 'estados.xlsx', sheet_name='estados')
    lista = []
    
    for arq_num, arq_nome in enumerate(glob.glob('*.txt')):
        #print(arq_num, arq_nome)
        
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        
        print(data)
        
        if data.year >= 2020:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
        else:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin')
        
        df = df.rename(columns = {'uf': 'uf_cod_ibge', 'UF': 'uf_cod_ibge'})
        df = pd.merge(df, df_estados_siglas, how='left', on='uf_cod_ibge')
        ###################################################################################################
        df_agregacao_uf = df.groupby(['seção', 'uf_sigla'])['saldomovimentação'].sum().to_frame()
        
        df_agregacao_uf = df_agregacao_uf.reset_index()
        
        df_agregacao_br = df_agregacao_uf.groupby(['seção'])['saldomovimentação'].sum().to_frame()
        
        df_agregacao_br = df_agregacao_br.reset_index()
        
        df_agregacao_br['nova_var'] = 'sm_' + df_agregacao_br['seção'] + '_BR'
        
        del df_agregacao_br['seção']
        
        df_agregacao_br = df_agregacao_br.set_index('nova_var')
        
        df_agregacao_br = df_agregacao_br.T
        
        df_agregacao_uf['nova_var'] = 'sm_' + df_agregacao_uf['seção'] + '_' + df_agregacao_uf['uf_sigla']
        
        del df_agregacao_uf['seção'], df_agregacao_uf['uf_sigla']
        
        df_agregacao_uf = df_agregacao_uf.set_index('nova_var')
        
        df_agregacao_uf = df_agregacao_uf.T
        
        df_agregacao = pd.merge(df_agregacao_br, df_agregacao_uf, left_index=True, right_index=True)
        
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        
        df_agregacao.index = [data]
        
        df_agregacao.index.freq = 'MS' # MS = Monthly Start
        
        if arq_num == 0:
            df_final = df_agregacao.copy()
        else:
            df_final = df_final.append(df_agregacao)
    
    ##################
    return df_final

df = gera_df()


import pandas as pd
arq_nome = 'CAGEDMOV201001.txt'

data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

if data.year < 2020:
    print('é menor que 2020 !!!')

print(data)
df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin')
print(df.dtypes)
df = df.rename(columns = {'uf': 'uf_cod_ibge', 'UF': 'uf_cod_ibge'})


print(df.dtypes)

##########################################################################################################
##########################################################################################################
##########################################################################################################

import pandas as pd
df_estados_siglas = pd.read_excel(caminho_base / 'dados' / 'estados.xlsx', sheet_name='estados')

##########################################################################################################
##########################################################################################################
##########################################################################################################

def cgd_agrega(coluna):
    import glob
    import pandas as pd
    df_estados_siglas = pd.read_excel(caminho_base / 'dados' / 'estados.xlsx', sheet_name='estados')
    lista = []
    arq_num = 0
    for arq_nome in glob.glob('*.txt'):
        arq_num += 1
        print(arq_nome)
        
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        
        print(data)
        
        df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
        
        df = df.rename(columns = {'uf': 'uf_cod_ibge'})
        df = pd.merge(df, df_estados_siglas, how='left', on='uf_cod_ibge')
        
        df_agregacao = df.groupby('uf_sigla')[coluna].sum().to_frame()
        df_agregacao = df_agregacao.T
        df_agregacao['br'] = df_agregacao.sum(axis=1)
        
        data = pd.to_datetime(data)
        
        df_agregacao['data'] = data
        df_agregacao = df_agregacao.set_index('data')
        df_agregacao.index.freq = 'MS' # MS = Monthly Start
        print(df_agregacao.index)
        
        if arq_num == 1:
            df_final = df_agregacao.copy()
        else:
            df_final = df_final.append(df_agregacao)
        
    #
    return df_final
        


df = cgd_agrega(coluna = 'saldomovimentação')

##########################################################################################################
##########################################################################################################
##########################################################################################################

import pandas as pd
df_estados_siglas = pd.read_excel(caminho_base / 'dados' / 'estados.xlsx', sheet_name='estados')

arq_nome = 'CAGEDMOV202001.txt'
data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

print(data)

df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)

df = df.rename(columns = {'uf': 'uf_cod_ibge'})
df = pd.merge(df, df_estados_siglas, how='left', on='uf_cod_ibge')

df_agregacao_uf = df.groupby(['seção', 'uf_sigla'])['saldomovimentação'].sum().to_frame()

df_agregacao_uf = df_agregacao_uf.reset_index()

df_agregacao_br = df_agregacao_uf.groupby(['seção'])['saldomovimentação'].sum().to_frame()

df_agregacao_br = df_agregacao_br.reset_index()

df_agregacao_br['nova_var'] = 'sm_' + df_agregacao_br['seção'] + '_BR'

del df_agregacao_br['seção']

df_agregacao_br = df_agregacao_br.set_index('nova_var')

df_agregacao_br = df_agregacao_br.T

df_agregacao_uf['nova_var'] = 'sm_' + df_agregacao_uf['seção'] + '_' + df_agregacao_uf['uf_sigla']

del df_agregacao_uf['seção'], df_agregacao_uf['uf_sigla']

df_agregacao_uf = df_agregacao_uf.set_index('nova_var')

df_agregacao_uf = df_agregacao_uf.T

df_agregacao = pd.merge(df_agregacao_br, df_agregacao_uf, left_index=True, right_index=True)

data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

df_agregacao.index = [data]

df_agregacao.index.freq = 'MS' # MS = Monthly Start







df_agregacao = df_agregacao_br.append(df_agregacao_uf)


df_agregacao = pd.merge(df_agregacao_uf, df_agregacao_br, how='left', on='uf_cod_ibge')



df_agregacao2 = df_agregacao.unstack().reset_index()

df_agregacao2.columns = df.columns.reset_index()

print(df_agregacao2.index)
print(df_agregacao2.columns)

df2 = df_agregacao.reset_index(col_level=1)
del df2['index']
df2['nova_var'] = df2['seção'] + '_' + df2['uf_sigla']
del df2['seção'], df2['uf_sigla']
df2 = df2.set_index('nova_var')
df2 = df2.T






































df2 = df[['CID','FE', 'FID']].groupby(by=['CID','FE']).count().unstack().reset_index()


df_agregacao = df_agregacao.T
df_agregacao['br'] = df_agregacao.sum(axis=1)

data = pd.to_datetime(data)

df_agregacao['data'] = data
df_agregacao = df_agregacao.set_index('data')
df_agregacao.index.freq = 'MS' # MS = Monthly Start
print(df_agregacao.index)

df1 = df_agregacao.copy()




##########################################################################################################
##########################################################################################################
##########################################################################################################
import pandas as pd
arq_nome = 'CAGEDMOV202002.txt'
data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

print(data)

df = pd.read_csv(arq_nome, header=0, sep=';', decimal='.', quotechar='"', skiprows=0)

print(df.dtypes)

ax = df['salário'].plot.hist(bins=100, range=(0, 10000))

ax.ticklabel_format(useOffset=False, style='plain')



cond1 = df['salário'] > 1000
df = df.loc[cond1,:]

df['salário'].plot.hist(bins=20, edgecolor='k').autoscale(enable=True, axis='both')


movies['CriticRating'].plot.hist()

df = df.rename(columns = {'uf': 'uf_cod_ibge'})
df = pd.merge(df, df_estados_siglas, how='left', on='uf_cod_ibge')
del df_estados_siglas

df_agregacao = df.groupby('uf_sigla')['saldomovimentação'].sum().to_frame()
df_agregacao = df_agregacao.T
df_agregacao['br'] = df_agregacao.sum(axis=1)

data = pd.to_datetime(data)

df_agregacao['data'] = data
df_agregacao = df_agregacao.set_index('data')
df_agregacao.index.freq = 'MS' # MS = Monthly Start
print(df_agregacao.index)

df2 = df_agregacao.copy()

dft = df1.append(df2)



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























colunas2020 = ['competência',
           'município',
           'seção',
           'subclasse',
           'saldomovimentação',
           'cbo2002ocupação',
           'graudeinstrução',
           'idade',
           'horascontratuais',
           'raçacor',
           'sexo',
           'tipoempregador',
           'tipomovimentação',
           'indtrabintermitente',
           'indtrabparcial',
           'salário']

col_excl_2020 = ['']

print(colunas)

























