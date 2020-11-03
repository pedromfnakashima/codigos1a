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
        
        print(f'Processando {arq_nome}')
        
        dic_colunas_tipos_0 = {'competência':'string',
                               'município':pd.Int64Dtype(),
                               'cbo2002ocupação':pd.Int64Dtype(),
                               'subclasse':pd.Int64Dtype(),
                               'classe':pd.Int64Dtype(),
                               'horascontratuais':'float64',
                               'graudeinstrução':pd.Int64Dtype(),
                               'idade':pd.Int64Dtype(),
                               'salário':'float64',
                               'saldomovimentação':pd.Int64Dtype()}
        
        dic_colunas_tipos_1 = {'Competência Declarada':'string',
                               'Município':pd.Int64Dtype(),
                               'CBO 2002 Ocupação':pd.Int64Dtype(),
                               'CNAE 2.0 Subclas':pd.Int64Dtype(),
                               'CNAE 2.0 Classe':pd.Int64Dtype(),
                               'Qtd Hora Contrat':'float64',
                               'Grau Instrução':pd.Int64Dtype(),
                               'Idade':pd.Int64Dtype(),
                               'Salário Mensal':'float64',
                               'Saldo Mov':pd.Int64Dtype()}
        
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

        # IMPORTA DADOS
        if data.year >= 2020:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, dtype=dic_colunas_tipos_0, na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}'])
        else:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype=dic_colunas_tipos_1, na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}'])

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
        
        df = df.rename(columns = dic_colunas)
        
        li_colunas = list(dic_colunas.values())
        
        if data.year < 2020:
            li_colunas.append('classe')
        
        df = df[li_colunas]
        
        # VAI EMPILHANDO OS
        if arq_num == 0:
            df_final = df.copy()
        else:
            df_final = df_final.append(df)
        
        print(f'  -> {arq_nome} processado.')
        
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
        # print(arq_num, arq_nome)
        print(f'Processando arquivo {arq_nome} ...')
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
        
        print(f'   {arq_nome} processado.')
    
    return df_final
    
df2 = cgd_agrega_antigo()

##############################################################################
##############################################################################
##############################################################################

globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')

caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
os.chdir(caminho_wd)

import pandas as pd
arq_nome = 'CAGEDMOV201206.txt'

df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', na_values = ['{ñ'])

dic_colunas_tipos_0 = {'competência':'string',
                       'município':pd.Int64Dtype(),
                       'cbo2002ocupação':pd.Int64Dtype(),
                       'subclasse':pd.Int64Dtype(),
                       'classe':pd.Int64Dtype(),
                       'horascontratuais':'float64',
                       'graudeinstrução':pd.Int64Dtype(),
                       'idade':pd.Int64Dtype(),
                       'salário':'float64',
                       'saldomovimentação':pd.Int64Dtype()}

dic_colunas_tipos_1 = {'Competência Declarada':'string',
                       'Município':pd.Int64Dtype(),
                       'CBO 2002 Ocupação':pd.Int64Dtype(),
                       'CNAE 2.0 Subclas':pd.Int64Dtype(),
                       'CNAE 2.0 Classe':pd.Int64Dtype(),
                       'Qtd Hora Contrat':'float64',
                       'Grau Instrução':pd.Int64Dtype(),
                       'Idade':pd.Int64Dtype(),
                       'Salário Mensal':'float64',
                       'Saldo Mov':pd.Int64Dtype()}

data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')

if data.year >= 2020:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, dtype=dic_colunas_tipos_0, na_values = ['{ñ','00000-1', '0000-1'])
else:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype=dic_colunas_tipos_1, na_values = ['{ñ','00000-1', '0000-1'])

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

if data.year < 2020:
    li_colunas.append('classe')

df = df[li_colunas]




#print(df.dtypes)
print(df['subclasse'].value_counts())
print(df['subclasse'].nunique())








##############################################################################
##############################################################################
##############################################################################

import pandas as pd
arq_nome = '2020_1_teste.txt'

#df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', na_values = ['{ñ'])

#print(df.dtypes)
#print(df['Grau Instrução'].value_counts())

dic_colunas_tipos_0 = {'competência':'string',
                       'município':'string',
                       'cbo2002ocupação':'string',
                       'subclasse':'string',
                       'classe':'string',
                       'horascontratuais':'float64',
                       'graudeinstrução':pd.Int64Dtype(),
                       'idade':pd.Int64Dtype(),
                       #'salário':'float64',
                       'saldomovimentação':pd.Int64Dtype()}

dic_colunas_tipos_1 = {'Competência Declarada':'string',
                       'Município':'string',
                       'CBO 2002 Ocupação':'string',
                       'CNAE 2.0 Subclas':'string',
                       'CNAE 2.0 Classe':'string',
                       'Qtd Hora Contrat':'float64',
                       'Grau Instrução':pd.Int64Dtype(),
                       'Idade':pd.Int64Dtype(),
                       'Salário Mensal':'float64',
                       'Saldo Mov':pd.Int64Dtype()}

data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
print(data)
# IMPORTA DADOS
if data.year >= 2020:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal='.', quotechar='"', skiprows=0, dtype=dic_colunas_tipos_0, na_values = ['{ñ','00000-1'])
else:
    df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype=dic_colunas_tipos_1, na_values = ['{ñ','00000-1'])

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



if data.year < 2020:
    li_colunas.append('classe')

df = df[li_colunas]



print(df.dtypes)
print(df['graudeinstrução'].value_counts())



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
