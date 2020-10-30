# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:52:18 2020

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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos'# / 'temp1'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

##########################################################################################################
##########################################################################################################
##########################################################################################################


def cgd_agrega():
    
    import glob
    import pandas as pd
    
    for arq_num, arq_nome in enumerate(glob.glob('*.txt')):

        
        dic_colunas_tipos_0 = {'competência':'string',
                               'município':'string',
                               'cbo2002ocupação':'string',
                               'subclasse':'string',
                               'classe':'string',
                               'horascontratuais':'float64',
                               'graudeinstrução':'int64',
                               'idade':'int64',
                               'salário':'float64',
                               'saldomovimentação':'string'}
        
        dic_colunas_tipos_1 = {'Competência Declarada':'string',
                               'Município':'int64',
                               'CBO 2002 Ocupação':'string',
                               'CNAE 2.0 Subclas':'string',
                               'CNAE 2.0 Classe':'string',
                               'Qtd Hora Contrat':'float64',
                               'Grau Instrução':'int64',
                               'Idade':'int64',
                               'Salário Mensal':'float64',
                               'Saldo Mov':'int64'}
        
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        print(data)
        # IMPORTA DADOS
        if data.year >= 2020:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, dtype=dic_colunas_tipos_0)
        else:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype=dic_colunas_tipos_1)

        dic_colunas = {'Competência Declarada':'competência',
                       'Município':'município',
                       'CBO 2002 Ocupação':'cbo2002ocupação',
                       'CNAE 2.0 Subclas':'subclasse',
                       'CNAE 2.0 Classe':'classe',
                       'Qtd Hora Contrat':'horascontratuais',
                       'Grau Instrução':'graudeinstrução',
                       'Idade':'idade',
                       'Salário Mensal':'salário',
                       'Saldo Mov':'saldomovimentação'}
        
        li_colunas = list(dic_colunas.values())
        
        df = df.rename(columns = dic_colunas)
        
        df = df.loc[:,li_colunas]
        
        # VAI EMPILHANDO OS
        if arq_num == 0:
            df_final = df.copy()
        else:
            df_final = df_final.append(df)
        
    return df_final

    
df = cgd_agrega()






















##########################################################################################################
##########################################################################################################
##########################################################################################################

def cgd_agrega():
    import glob
    import pandas as pd

    for arq_num, arq_nome in enumerate(glob.glob('*.txt')):
        # GERA DATA NO FORMATO DATETIME
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        print(arq_num, data)
        # IMPORTA DADOS DE ACORDO COM A DATA
        if data.year >= 2020:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
        else:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin')
        
        # RENOMEIA COLUNAS DA UF E DO COD_IBGE
        df = df.rename(columns = {'uf':'uf_cod_ibge', 'UF':'uf_cod_ibge', 'Saldo Mov':'sm', 'saldomovimentação':'sm'})
        # AGREGAÇÃO BRASIL
        soma_br = df.loc[:, ['sm']].sum().to_frame()
        soma_br.index = [data]
        soma_br.index.freq = 'MS' # MS = Monthly Start
        soma_br = soma_br.rename(columns={0:'br'})
        # AGREGAÇÃO MS
        cond1 = df['uf_cod_ibge'] == 50
        soma_ms = df.loc[cond1, ['sm']].sum().to_frame()
        soma_ms.index = [data]
        soma_ms.index.freq = 'MS' # MS = Monthly Start
        soma_ms = soma_ms.rename(columns={0:'ms'})
        # FAZ O MERGE
        soma = pd.merge(soma_br, soma_ms, left_index=True, right_index=True)
        # VAI EMPILHANDO OS
        if arq_num == 0:
            df_final = soma.copy()
        else:
            df_final = df_final.append(soma)
    
    return df_final
    
df = cgd_agrega()

##########################################################################################################
##########################################################################################################
##########################################################################################################

def cgd_agrega():
    import glob
    import pandas as pd

    for arq_num, arq_nome in enumerate(glob.glob('*.txt')):
        # GERA DATA NO FORMATO DATETIME
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        print(arq_num, data)
        # IMPORTA DADOS DE ACORDO COM A DATA
        if data.year >= 2020:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
        else:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin')
        
        # RENOMEIA COLUNAS DA UF E DO COD_IBGE
        df = df.rename(columns = {'uf':'uf_cod_ibge', 'UF':'uf_cod_ibge', 'Saldo Mov':'sm', 'saldomovimentação':'sm'})
        # AGREGAÇÃO BRASIL
        soma_br = df.loc[:, ['sm']].sum().to_frame()
        soma_br.index = [data]
        soma_br.index.freq = 'MS' # MS = Monthly Start
        soma_br = soma_br.rename(columns={0:'br'})
        # AGREGAÇÃO MS
        cond1 = df['uf_cod_ibge'] == 50
        soma_ms = df.loc[cond1, ['sm']].sum().to_frame()
        soma_ms.index = [data]
        soma_ms.index.freq = 'MS' # MS = Monthly Start
        soma_ms = soma_ms.rename(columns={0:'ms'})
        # FAZ O MERGE
        soma = pd.merge(soma_br, soma_ms, left_index=True, right_index=True)
        # VAI EMPILHANDO OS
        if arq_num == 0:
            df_final = soma.copy()
        else:
            df_final = df_final.append(soma)
    
    return df_final
    
df = cgd_agrega()

##############################################################################
##############################################################################
##############################################################################
def cgd_agrega_antigo():
    import glob
    import pandas as pd

    for arq_num, arq_nome in enumerate(glob.glob('*.txt')):
        # GERA DATA NO FORMATO DATETIME
        print(arq_num, arq_nome)
        # IMPORTA DADOS
        df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype={'Competência Movimentação':'string'})
        df = df.rename(columns = {'uf':'uf_cod_ibge', 'UF':'uf_cod_ibge', 'Saldo Mov':'sm', 'saldomovimentação':'sm'})
        # AGREGAÇÃO MS
        cond1 = df['uf_cod_ibge'] == 50
        soma_ms = df.loc[cond1, :]
        soma_ms = soma_ms.groupby('Competência Movimentação')['sm'].sum().to_frame()
        soma_ms.index = pd.to_datetime(soma_ms.index, format='%Y%m', errors='ignore')
        soma_ms.index.freq = 'MS' # MS = Monthly Start
        soma_ms = soma_ms.rename(columns={'sm':'ms'})
        # AGREGAÇÃO BRASIL
        soma_br = df.groupby('Competência Movimentação')['sm'].sum().to_frame()
        soma_br.index = pd.to_datetime(soma_br.index, format='%Y%m', errors='ignore')
        soma_br.index.freq = 'MS' # MS = Monthly Start
        soma_br = soma_br.rename(columns={'sm':'br'})
        # FAZ O MERGE
        soma = pd.merge(soma_br, soma_ms, left_index=True, right_index=True)
        soma = soma.rename_axis("data", axis="rows")
        # VAI EMPILHANDO OS
        if arq_num == 0:
            df_final = soma.copy()
        else:
            df_final = df_final.append(soma)
    
    return df_final
    
df2 = cgd_agrega_antigo()

##############################################################################
##############################################################################
##############################################################################

import pandas as pd
arq_nome = 'CAGEDMOV200701.txt'

dic_colunas_tipos_0 = {'competência':'string',
                       'município':'string',
                       'cbo2002ocupação':'string',
                       'subclasse':'string',
                       'classe':'string',
                       'horascontratuais':'float64',
                       'graudeinstrução':'int64',
                       'idade':'int64',
                       'salário':'float64',
                       'saldomovimentação':'string'}

dic_colunas_tipos_1 = {'Competência Declarada':'string',
                       'Município':'int64',
                       'CBO 2002 Ocupação':'string',
                       'CNAE 2.0 Subclas':'string',
                       'CNAE 2.0 Classe':'string',
                       'Qtd Hora Contrat':'float64',
                       'Grau Instrução':'int64',
                       'Idade':'int64',
                       'Salário Mensal':'float64',
                       'Saldo Mov':'int64'}

data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
print(data)
# IMPORTA DADOS
if data.year >= 2020:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, dtype=dic_colunas_tipos_0)
else:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype=dic_colunas_tipos_1)

#df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype={'Competência Movimentação':'string'})
#df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, dtype={'Competência Movimentação':'string'})

print(df.dtypes)

dic_colunas = {'Competência Declarada':'competência',
               'Município':'município',
               'CBO 2002 Ocupação':'cbo2002ocupação',
               'CNAE 2.0 Subclas':'subclasse',
               'CNAE 2.0 Classe':'classe',
               'Qtd Hora Contrat':'horascontratuais',
               'Grau Instrução':'graudeinstrução',
               'Idade':'idade',
               'Salário Mensal':'salário',
               'Saldo Mov':'saldomovimentação'}

li_colunas = list(dic_colunas.values())

df = df.rename(columns = dic_colunas)

df = df.loc[:,li_colunas]




print(df['saldomovimentação'].sum())


# Testes: procurar pelo arroz

df2 = df.copy()



cond1 = df['classe'] == '01113'
print(cond1.sum())
df2 = df2.loc[cond1,:]


print(df2['subclasse'].unique())
print(df2['subclasse'].value_counts())


print(df2['saldomovimentação'].sum())





print(df2['subclasse'].count_values())


print(df.dtypes)

df = df.loc[:, li_colunas]

# AGREGAÇÃO MS
cond1 = df['uf_cod_ibge'] == 50
soma_ms = df.loc[cond1, :]
soma_ms = soma_ms.groupby('Competência Movimentação')['sm'].sum().to_frame()
soma_ms.index = pd.to_datetime(soma_ms.index, format='%Y%m', errors='ignore')
soma_ms.index.freq = 'MS' # MS = Monthly Start
soma_ms = soma_ms.rename(columns={'sm':'ms'})
# AGREGAÇÃO BRASIL
soma_br = df.groupby('Competência Movimentação')['sm'].sum().to_frame()
soma_br.index = pd.to_datetime(soma_br.index, format='%Y%m', errors='ignore')
soma_br.index.freq = 'MS' # MS = Monthly Start
soma_br = soma_br.rename(columns={'sm':'br'})
# FAZ O MERGE
soma = pd.merge(soma_br, soma_ms, left_index=True, right_index=True)
soma = soma.rename_axis("data", axis="rows")


##############################################################################
##############################################################################
##############################################################################

import pandas as pd
arq_nome = 'CAGEDMOV201001.txt'

data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

if data.year >= 2020:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0)
else:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin')

print(df.dtypes)

df = df.rename(columns = {'uf':'uf_cod_ibge', 'UF':'uf_cod_ibge', 'Saldo Mov':'sm', 'saldomovimentação':'sm'})

# AGREGAÇÃO BRASIL
soma_br = df.loc[:, ['sm']].sum().to_frame()
soma_br.index = [data]
soma_br.index.freq = 'MS' # MS = Monthly Start
soma_br = soma_br.rename(columns={0:'br'})
# AGREGAÇÃO MS
cond1 = df['uf_cod_ibge'] == 50
soma_ms = df.loc[cond1, ['sm']].sum().to_frame()
soma_ms.index = [data]
soma_ms.index.freq = 'MS' # MS = Monthly Start
soma_ms = soma_ms.rename(columns={0:'ms'})
# FAZ O MERGE
soma = pd.merge(soma_br, soma_ms, left_index=True, right_index=True)

print(soma_ms)
