# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:49:28 2020

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
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)

#import numpy as np
import pandas as pd

############################
############################
############################

import numpy as np
import pandas as pd

dfx1 = pd.DataFrame(np.arange('2019-07-01','2020-12-01', 1, dtype='datetime64[M]'))
dfx1.set_index(0, inplace=True)
dfx1['Valor'] = np.nan

# ----------------------------------------------------------------------------------------
# Função processa_arquivos_zip no script junta_siconfi_01c.py

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
df = processa_arquivos_zip(arquivo='2020b3.zip',
                                           caminho=pasta,
                                           pasta=False)

cond1 = df['UF'] == 'MS'
cond2 = df['Conta'].str.contains('icms', case=False)
cond3 = df['mês'].notnull()
cond = cond1 & cond2 & cond3
filtro = df.loc[cond, ['mês','Valor']]
filtro.set_index('mês', inplace=True)

# ----------------------------------------------------------------------------------------

dfx1.update(filtro)

# ----------------------------------------------------------------------------------------

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
df = processa_arquivos_zip(arquivo='2020b4.zip',
                                           caminho=pasta,
                                           pasta=False)

cond1 = df['UF'] == 'MS'
cond2 = df['Conta'].str.contains('^impostos, taxas', case=False)
cond3 = df['mês'].notnull()
cond = cond1 & cond2 & cond3
filtro = df.loc[cond, :]
filtro = df.loc[cond, ['mês','Valor']]
filtro.set_index('mês', inplace=True)

# ----------------------------------------------------------------------------------------

dfx1.update(filtro)

# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
import numpy as np

dfx1 = pd.DataFrame(np.arange('2019-07-01','2020-12-01', 1, dtype='datetime64[M]'))
dfx1.set_index(0, inplace=True)
dfx1['Valor'] = np.nan

# ----------------------------------------------------------------------------------------

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
df = processa_arquivos_zip(arquivo='2015b1.zip',
                                           caminho=pasta,
                                           pasta=True)


cond1 = df['UF'] == 'SP'
cond2 = df['Conta'].str.contains('icms', case=False)
cond3 = df['mês'].notnull()
cond = cond1 & cond2 & cond3
filtro = df.loc[cond, ['mês','Valor', 'Conta', 'Coluna', 'MR']]
#filtro.sort_values(['mês','MR'], ascending=[True,True], inplace=True)
filtro = filtro.sort_values(['mês','MR'], ascending=[True,True]).groupby('mês').tail(1)
filtro = filtro.loc[:, ['mês','Valor']]
filtro.set_index('mês', inplace=True)
filtro.rename(columns={'Valor':'icms'}, inplace=True)

df_series = filtro.copy()

# ----------------------------------------------------------------------------------------

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
df = processa_arquivos_zip(arquivo='2015b1.zip',
                                           caminho=pasta,
                                           pasta=True)


meses = df.groupby('mês').head(1)['mês'].to_frame()
meses.set_index('mês', inplace=True)
meses['Valor'] = np.nan

cond1 = df['UF'] == 'SP'
cond2 = df['Conta'].str.contains('Transferências.+FUNDEB', case=False)
cond3 = df['mês'].notnull()
cond = cond1 & cond2 & cond3
filtro = df.loc[cond, ['mês','Valor', 'Conta', 'Coluna', 'MR']]
#filtro.sort_values(['mês','MR'], ascending=[True,True], inplace=True)
filtro = filtro.sort_values(['mês','MR'], ascending=[True,True]).groupby('mês').tail(1)
filtro = filtro.loc[:, ['mês','Valor']]
filtro.set_index('mês', inplace=True)
if len(filtro) == 0:
    filtro = meses.copy()
filtro.rename(columns={'Valor':'transfFundeb'}, inplace=True)



df_series = df_series.merge(filtro, left_index=True, right_index=True)


# ----------------------------------------------------------------------------------------


'''
SÉRIES OK (TEM EM 2015b1 e 2020b4):

cond2 = df['Conta'].str.contains('^receitas correntes', case=False)
cond2 = df['Conta'].str.contains('icms', case=False)
cond2 = df['Conta'].str.contains('ipva', case=False)
cond2 = df['Conta'].str.contains('itcd', case=False)
cond2 = df['Conta'].str.contains('irrf', case=False)
cond2 = df['Conta'].str.contains('contribuições', case=False)
cond2 = df['Conta'].str.contains('^transferências correntes', case=False)
cond2 = df['Conta'].str.contains('fpe', case=False)
cond2 = df['Conta'].str.contains('Transferências.+FUNDEB', case=False)

'''

colunas = ['recCorr', 'icms', 'ipva', 'itcd', 'irrf', 'contrib', 'transfCorr', 'fpe', 'tranfFudeb']
buscas = ['^receitas correntes','icms','ipva','itcd','irrf','contribuições','^transferências correntes','fpe','Transferências.+FUNDEB']

colunas = ['recCorr']
buscas = ['^receitas correntes']

for coluna, busca in zip(colunas,buscas):
    print(coluna,busca)




#################################################################################################
################################### FAZER O LOOPING #############################################
#################################################################################################
import numpy as np
import pandas as pd

dfx1 = pd.DataFrame(np.arange('2019-07-01','2020-12-01', 1, dtype='datetime64[M]'))
dfx1.set_index(0, inplace=True)
dfx1['Valor'] = np.nan

ufs = ['MS', 'MT', 'AM', 'RO', 'BA', 'SP', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
 'SE', 'PB', 'MA', 'CE', 'RJ', 'PI', 'AC', 'RS', 'RR', 'MG', 'RN', 'AL', 'DF']
colunas = ['recCorr', 'icms', 'ipva', 'itcd', 'irrf', 'contrib', 'transfCorr', 'fpe', 'tranfFudeb']
buscas = ['^receitas correntes','icms','ipva','itcd','irrf','contribuições','^transferências correntes','fpe','Transferências.+FUNDEB']


ufs = ['MS']
colunas = ['recCorr']
buscas = ['^receitas correntes']



cond2 = df['Conta'].str.contains('^impostos, taxas', case=False)


def g_series_mensais():
    dicionario = {}
    
    pasta = caminho_base / 'Dados' / 'Siconfi' / 'RREO - Estados' / 'Anexo 03 - Demonstrativo da Receita Corrente Líquida'
    df = processa_arquivos_zip(arquivo='2015b1.zip',
                                           caminho=pasta,
                                           pasta=True)
            

    ufs = ['MS', 'MT', 'AM', 'RO', 'BA', 'SP', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
           'SE', 'PB', 'MA', 'CE', 'RJ', 'PI', 'AC', 'RS', 'RR', 'MG', 'RN', 'AL', 'DF']
    colunas = ['recCorr', 'itcm', 'icms', 'ipva', 'itcd', 'irrf', 'contrib', 'transfCorr', 'fpe', 'transfFundeb']
    buscas = ['^receitas correntes','^impostos, taxas','icms','ipva','itcd','irrf','contribuições','^transferências correntes','fpe','Transferências.+FUNDEB']
    
    #ufs = ['SP']
    #colunas = ['icms', 'ipva']
    #buscas = ['icms', 'ipva']
    
    for uf in ufs:
        
        print(f'Adicionando Estado: {uf}')
        
        for index, (coluna, busca) in enumerate(zip(colunas,buscas)):
            #print(index,coluna,busca)
            
            cond1 = df['UF'] == uf
            cond2 = df['Conta'].str.contains(busca, case=False)
            cond3 = df['mês'].notnull()
            cond = cond1 & cond2 & cond3
            filtro = df.loc[cond, ['mês','Valor', 'Conta', 'Coluna', 'MR']]
            #filtro.sort_values(['mês','MR'], ascending=[True,True], inplace=True)
            filtro = filtro.sort_values(['mês','MR'], ascending=[True,True]).groupby('mês').tail(1)
            filtro = filtro.loc[:, ['mês','Valor']]
            filtro.set_index('mês', inplace=True)
            filtro.rename(columns={'Valor':coluna}, inplace=True)
            
            if index == 0:
                df_series = filtro.copy()
                
            else:
                df_series = df_series.merge(filtro, how='left', left_index=True, right_index=True)
        
        dicionario[uf] = df_series
    
    return dicionario


dic_series_mensais = g_series_mensais()
# Valores nominais. Fazer valores reais no arquivo m.

















