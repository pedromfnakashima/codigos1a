# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:41:29 2020

@author: pedro
Interpretador Python 3.8
"""
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
caminho_wd = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

""" Lista de arquivos zip do wd """
import glob
for arq_nome in glob.glob('*.zip'):
    print(arq_nome)

""" Lista de arquivos zip do wd
e coloca os nomes no dicionário
"""
import glob
for arq_nome in glob.glob('*.zip'):
    print(arq_nome)

""" Colocar dados dos arquivos em um dicionário """
meta_dados = {}
meta_dados.update({'pasta': caminho_wd.name})

""" Lê cabeçalho """
with open('finbraRGF.csv', 'r') as f:
    f_contents = f.readline()
    while f_contents.find(';') == -1:
        print(f_contents, end='')
        f_contents = f.readline()



# Funcionando
import zipfile
with zipfile.ZipFile('2015q1.zip', 'r') as my_zip:
    csv_nome = my_zip.namelist()[0]
    print(csv_nome)


# Funcionando
import pandas as pd
df = pd.read_csv('2015q1.zip', compression='zip', header=0, sep=';', quotechar='"', encoding = 'latin', skiprows=6)

# Funcionando
import zipfile
import io
with zipfile.ZipFile('2015q1.zip', 'r') as zf:
    csv_nome = zf.namelist()[0]
    with io.TextIOWrapper(zf.open(csv_nome), encoding="latin") as f:
        f_contents = f.readline()
        contador = 0
        while f_contents.find(';') == -1:
            contador += 1
            print(contador)
            print(f_contents, end='')
            f_contents = f.readline()

# Funcionando
import zipfile
import io
with zipfile.ZipFile('2015q1.zip', 'r') as zf:
    csv_nome = zf.namelist()[0]
    with io.TextIOWrapper(zf.open(csv_nome), encoding="latin") as f:
        f_contents = f.readline()
        contador = 0
        while f_contents.find(';') == -1:
            contador += 1
            f_contents = f.readline()

import pandas as pd
df = pd.read_csv('2015q1.zip', compression='zip', header=0, sep=';', quotechar='"', encoding = 'latin', skiprows=contador)

# Funcionando

def gera_df(nome_zip):
    import zipfile
    import io
    import pandas as pd
    with zipfile.ZipFile(nome_zip, 'r') as zf:
        csv_nome = zf.namelist()[0]
        with io.TextIOWrapper(zf.open(csv_nome), encoding="latin") as f:
            f_contents = f.readline()
            contador = 0
            while f_contents.find(';') == -1:
                contador += 1
                f_contents = f.readline()
    df = pd.read_csv(nome_zip, compression='zip', header=0, sep=';', quotechar='"', encoding = 'latin', skiprows=contador)
    return df

siconfi_df = gera_df('2015q1.zip')

# Funcionando

def gera_df(nome_zip):
    import zipfile
    import io
    import pandas as pd
    with zipfile.ZipFile(nome_zip, 'r') as zf:
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
    
    li_exercicio = lista[0].replace('\n','').split(':')
    li_exercicio = [elemento.strip() for elemento in li_exercicio]
    ano = li_exercicio[1]
    
    df['exercicio'] = int(ano)
    
    li_periodo = lista[1].replace('\n','').split(':')
    li_periodo = [elemento.strip() for elemento in li_periodo]
    li_periodo = li_periodo[1]
    li_periodo = li_periodo.split('.')
    li_periodo = [elemento.strip() for elemento in li_periodo]
    periodo_num = li_periodo[0][0]
    periodo_unidade = li_periodo[1]
    
    df[periodo_unidade] = int(periodo_num)
    
    return df

#df_siconfi = gera_df('2015q1.zip')
#df_siconfi.rename('outro')


#print(dir(df_siconfi))

# Funcionando

def processa_arquivos():
    import glob
    dicionario = {}
    print('Adicionados:')
    for arq_nome in glob.glob('*.zip'):
        pos_ponto = arq_nome.find('.zip')
        df_nome = f'df_{arq_nome[0:pos_ponto]}'
        
        print(f'  {df_nome}')
        
        dicionario[df_nome] = gera_df(arq_nome)

        
    return dicionario

dic = processa_arquivos()

# print(dic['df_2020q1']['Instituição'].unique())

lista = sorted(list(dic['df_2020q1']['Instituição'].unique()))


import pandas as pd
df = pd.DataFrame(lista)
df.rename(columns={0: 'instituições'}, inplace=True)

df['posicao'] = df['instituições'].str.find('do')

df['inst2'] = df['instituições'].str.slice(0,5)


df['inst2'] = df['instituições'].str.slice(0,df['instituições'].str.find('do'))

# https://stackoverflow.com/questions/37973757/slicing-a-pandas-column-based-on-the-position-of-a-matching-substring
# https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extract.html
















