# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 02:07:52 2020

@author: pedro
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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

##########################################################################################################
################################### TESTES ###############################################################
##########################################################################################################
import pandas as pd

pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / 'CAGEDMOV202009.csv', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)

print(df['saldomovimentação'].sum())

pasta = caminho_base / 'Dados' / 'trabalho' / 'rais_vinculos' / 'microdados'
df = pd.read_csv(pasta / 'MS2007.txt', header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}'])
print(df.dtypes)



print(df['saldomovimentação'].sum())


##########################################################################################################
#################################### FAZER O LOOPING #####################################################
##########################################################################################################
import pandas as pd


def caged_no_ano():
    anos = pd.Series(['2020', '2019'])
    meses = pd.Series(['09', '08', '07', '06', '05', '04', '03', '02', '01'])
    
    df_somas = pd.DataFrame(columns=['competência','saldomovimentação'])
    for ano in anos:
        for mes in meses:
            arq_nome = f'CAGEDMOV{ano}{mes}.csv'
            print(arq_nome)
            
            pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
            df = pd.read_csv(pasta / arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
            
            df_soma = df.groupby(['competência'])['saldomovimentação'].sum().to_frame()
            df_soma.reset_index(inplace=True)
            
            df_somas = df_somas.append(df_soma)
    
    
    print(df_somas.dtypes)
    
    
    df_somas['competência'] = df_somas['competência'].astype('str')
    
    
    df_somas['year'] = df_somas['competência'].str.slice(0, 4).astype('int64')
    df_somas['month'] = df_somas['competência'].str.slice(4, 6).astype('int64')
    df_somas['day'] = 1
    df_somas['mês'] = pd.to_datetime(df_somas[['year', 'month', 'day']])
    df_somas.drop(['year', 'month', 'day', 'competência'], axis=1, inplace=True)
    '''
    df_somas.set_index('mês', inplace=True)
    df_somas.sort_index(inplace=True)
    def _validate_frequency(cls, index, freq, **kwargs): # https://github.com/quantopian/alphalens/issues/371
        return None
    pd.core.arrays.datetimelike.DatetimeLikeArrayMixin._validate_frequency = _validate_frequency
    df_somas.index.freq = 'MS'
    '''

    
    return df_somas

df_caged_mensal = caged_no_ano()
df_caged_mensal['ano'] = df_caged_mensal['mês'].dt.year
df_caged_ano = df_caged_mensal.groupby(['ano'])['saldomovimentação'].sum()






print(df_somas.index)

pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
todos = pd.read_csv(pasta / 'CAGEDMOV202009.csv', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)

pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / 'CAGEDMOV202008.csv', header=0, sep=';', decimal=',', quotechar='"', skiprows=0)

todos = todos.append(df)

print(todos['competência'].unique())


del todos


df_somas = pd.DataFrame(columns=['competência','saldomovimentação'])

df_soma = df.groupby(['competência'])['saldomovimentação'].sum().to_frame()
df_soma.reset_index(inplace=True)

df_somas = df_somas.append(df_soma)

