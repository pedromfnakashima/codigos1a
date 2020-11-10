# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:41:29 2020

@author: pedro
Interpretador Python 3.8
"""
#############################
##### CONFIGURAÇÃO GERAL ####
#############################
globals().clear()
import numpy as np
import pandas as pd
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
#caminho_wd = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
caminho_wd = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Estados' / 'Despesas por Função'
os.chdir(caminho_wd)


#############################
#############################
#############################

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
    
    
    """ Manipula coluna Instituição """
    """ Usando regex """
    df['Instituição'] = df['Instituição'].str.replace('\sdo[\s\w]+', '')
    """ Usando filtro """
    filtro = df['Instituição'].str.contains('Justiça Militar')
    df.loc[filtro, 'Instituição'] = 'Tribunal de Justiça Militar'
    
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
    
    i = 1
    for key in dicionario.keys():
        
        if i == 1:
            novo_df = dicionario[key]
        else:
            novo_df = novo_df.append(dicionario[key])
        i += 1
        
    return novo_df

#dic = processa_arquivos()
df = processa_arquivos()

print(list(df['Instituição'].unique()))


df.to_csv("siconfi_completo.csv")

# Para preparar para merge
print(df.shape)
print(df['Instituição'].nunique())

# Filtrando:

ms = df.loc[df.UF =="MS", ['Instituição', 'Coluna', 'Conta', 'Valor', 'exercicio', 'quadrimestre']]



teste = pd.read_html('http://www.transparencia.al.ms.gov.br/pages/index.php/consultaservidores')[0]


filtro = teste['Nome'].str.contains('JOÃO')
filtrados = teste.loc[filtro, :]
print(filtrados)

filtro = teste['Cargo'].str.contains('ASSESSOR I')
filtrados = teste.loc[filtro, :]
print(filtrados)
























