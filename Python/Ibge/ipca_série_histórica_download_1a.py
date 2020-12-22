# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:29:50 2020

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
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)

#import numpy as np
import pandas as pd




#################################################################################################
##################################### DOWNLOAD COMPLETO #########################################
#################################################################################################


'''
Períodos e tabelas (IPCA)
2938: julho/2006 até dezembro/2011 (link: https://sidra.ibge.gov.br/Tabela/2938)
1419: janeiro/2012 até dezembro/2019 (link: https://sidra.ibge.gov.br/tabela/1419)
7060: a partir de janeiro/2020 (link: https://sidra.ibge.gov.br/tabela/7060)
Períodos e tabelas (IPCA-15)
'''



#################################################################################################
################################# DOWNLOAD DOS ARQUIVOS #########################################
#################################################################################################

#################################################################################################
########################################## FUNÇÕES ##############################################
#################################################################################################

# Gera lista das datas disponíveis

def g_data_MinMax(tab_num):
   
    import requests
    
    # tab_num='2938'
    dtCol='dt'
    
    url = f'https://apisidra.ibge.gov.br/values/t/{tab_num}/n1/all/v/63/p/all/c315/7169/d/v63%202'
    r = requests.get(url)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    
    df[dtCol] = pd.to_datetime(df['D3C'], format='%Y%m', errors='coerce')
    cond1 = ~ df[dtCol].isnull()
    
    li_datas_pdDateTime = df.loc[cond1,['dt']]['dt']
    data_máx = li_datas_pdDateTime.max()
    data_mín = li_datas_pdDateTime.min()
    
    li_datas_str = [str(dt.year) + str(dt.month).zfill(2) for dt in li_datas_pdDateTime]
    
    # print(data_máx)
    # print(str(data_máx))
    # print(str(data_máx.year))
    # print(str(data_máx.month))
    
    data_máx_str = str(data_máx.year) + str(data_máx.month).zfill(2)
    data_mín_str = str(data_mín.year) + str(data_mín.month).zfill(2)
    
    return li_datas_str, data_máx_str, data_mín_str

# li_datas_str, data_máx, data_mín = g_data_MinMax(tab_num='2938')

# Gera datas no formato IBGE
def g_li_datas_ibge(início, final):
    
    # início = '200607'
    # final = '201212'
    # início = '2006-07'
    # final = '2012-12'
    
    if início == final:
        str_dt_ibge = início.replace('-','')
        li_meses = [str_dt_ibge]
    else:
        import numpy as np
        from datetime import datetime
        import pandas as pd
        import re
        # Formato de data: yyyy-mm
        matched = re.match('\d{4}\-\d{2}', início, re.IGNORECASE)
        is_match = bool(matched)
        # print(is_match)
        if is_match == True:
            ano_início = int(início.split('-')[0])
            mês_início = int(início.split('-')[1])
            ano_final = int(final.split('-')[0])
            mês_final = int(final.split('-')[1])
        else:
            # Formato de data: yyyymm
            ano_início = int(início[:4])
            mês_início = int(início[4:])
            ano_final = int(final[:4])
            mês_final = int(final[4:])
        # Gera data formato datetime
        data1 = datetime(ano_início, mês_início, 1)
        data2 = datetime(ano_final, mês_final, 1) + pd.DateOffset(months=1)
        np_meses = np.arange(data1,data2, 1, dtype='datetime64[M]').astype(str)
        li_meses = [s.replace('-','') for s in np_meses]
    return li_meses

# li_meses = g_li_datas_ibge('2020-01', '2020-01')
# li_meses = g_li_datas_ibge(data_mín, data_máx)

# tab_num = '7060'
# tab_num = '2938'

# Download de tabelas
def download_tabela(tabela, li_meses):
    import requests
    
    for index, mês in enumerate(li_meses):
        print(f'Baixando: {mês}')
    
        #mês = '201201'
        url = f'https://apisidra.ibge.gov.br/values/t/{tabela}/n1/all/n6/all/v/63,66/p/{mês}/c315/all/d/v63%202,v66%204'
        r = requests.get(url)
        j = r.json()
        df = pd.DataFrame.from_dict(j)
        
        if index == 0:
            df_completo = df.copy()
        else:
            df_completo = df_completo.append(df)
    
    # Necessário tornar os index únicos para o looping das linhas da função g_cols_cód_desc
    df_completo.index = range(len(df_completo))
    return df_completo

# df = download_tabela(tab_num, g_li_datas_ibge('2020-01', '2020-02'))
# df = download_tabela(tab_num, g_li_datas_ibge('2006-07', '2006-08'))

# Gera colunas de código e de descrição
def g_cols_cód_desc(df, colCód, colDesc):
    print('Adicionando colunas de código e descrição do IBGE')
    for index_linha, linha in df.iterrows():
        df.loc[index_linha,colCód] = linha['D4N'].split(".")[0] 
        try: # Roda o seguinte código
            df.loc[index_linha,colDesc] = linha['D4N'].split(".")[1]
        except IndexError:  # Executa esse código quando há a exceção
            import re
            is_match = bool(re.match('^índice', df.loc[index_linha,'D4N'], re.IGNORECASE))
            if is_match == True:
                df.loc[index_linha,colDesc] = 'Índice geral'
                df.loc[index_linha,colCód] = '0'
            else:
                df.loc[index_linha,colDesc] = ''
        else:  # se não há exceção, roda esse código
            pass
        finally: # sempre roda esse código
            pass
    cond1 = df[colDesc] != ''
    df = df.loc[cond1,:]
    return df

# df2 = g_cols_cód_desc(df, colCód='códIBGE', colDesc='descCatIBGE')

# Gera coluna de categoria IBGE
def g_col_categoriaIBGE(df, colCód, colCat):
    # Classifica as entradas como Geral, Grupo, Subgrupo, Item, Subitem
    print('Classificando código IBGE como Geral, Grupo, Subgrupo, Item ou Subitem')
    cond1 = df[colCód] == '0'
    cond = cond1
    df.loc[cond1,colCat] = 'Geral'
    
    cond1 = df[colCód].str.len() == 1
    cond2 = df[colCód] != '0'
    cond = cond1 & cond2
    df.loc[cond,colCat] = 'Grupo'
    
    cond1 = df[colCód].str.len() == 2
    df.loc[cond1,colCat] = 'Subgrupo'
    
    cond1 = df[colCód].str.len() == 4
    df.loc[cond1,colCat] = 'Item'
    
    cond1 = df[colCód].str.len() == 7
    df.loc[cond1,colCat] = 'Subitem'
    
    return df

# df = g_col_categoriaIBGE(df, colCód='códIBGE', colCat='tipoCatIBGE')

# print(df.dtypes)

################################# ADICIONA CÓDIGOS DO BACEN ######################################

# Necessário rodar antes o código ipca_popula_xlsx_categoriasBC.py, que
# popula o arquivo categoriasBC.xlsx
def add_cols_catBC(df, tab_num, colCódDF, colCódPlanilha, colDescPlanilha):
    print('Adicionando categorias do BC (comercializáveis, duráveis, serviços...)')
    # colCódPlanilha = 'código'
    # colDescPlanilha = 'descrição'
    arq_xlsx_catBC = 'categoriasBC.xlsx'
    sheet_name = 't' + tab_num
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    catsBC = pd.read_excel(pasta / arq_xlsx_catBC, sheet_name=sheet_name, skiprows=0, dtype={colCódPlanilha:'str'})
    # catsBC.drop([colDescPlanilha],axis=1,inplace=True)
    
    df = df.merge(catsBC,how='left',left_on=colCódDF,right_on=colCódPlanilha)
    
    cond1 = ~ df[colCódPlanilha].isnull()
    df = df.loc[cond1,:]
    
    df.drop([colDescPlanilha, colCódPlanilha],axis=1,inplace=True)
    
    return df

# df = add_cols_catBC(df, tab_num=tab_num, colCódDF='códIBGE', colCódPlanilha='código', colDescPlanilha='descrição')

################################# ADICIONA DATAS DATETIME ######################################

def g_col_dt(df, dtCol):
    print('Adicionando datas')
    df[dtCol] = pd.to_datetime(df['D3C'], format='%Y%m')
    return df

# df = g_col_dt(df, dtCol='dt')


##################################### TABELA 7060 #####################################
tab_num = '7060'

li_datas_str, data_máx, data_mín = g_data_MinMax(tab_num=tab_num)
df = download_tabela(tab_num, g_li_datas_ibge(data_mín, data_máx))
df = g_cols_cód_desc(df, colCód='códIBGE', colDesc='descCatIBGE')
df = g_col_categoriaIBGE(df, colCód='códIBGE', colCat='tipoCatIBGE')
df = add_cols_catBC(df, tab_num=tab_num, colCódDF='códIBGE', colCódPlanilha='código', colDescPlanilha='descrição')
df = g_col_dt(df, dtCol='dt')

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't' + tab_num + '.csv'
df.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)

##################################### TABELA 1419 #####################################

tab_num = '1419'

li_datas_str, data_máx, data_mín = g_data_MinMax(tab_num=tab_num)
df = download_tabela(tab_num, g_li_datas_ibge(data_mín, data_máx))
df = g_cols_cód_desc(df, colCód='códIBGE', colDesc='descCatIBGE')
df = g_col_categoriaIBGE(df, colCód='códIBGE', colCat='tipoCatIBGE')
df = add_cols_catBC(df, tab_num=tab_num, colCódDF='códIBGE', colCódPlanilha='código', colDescPlanilha='descrição')
df = g_col_dt(df, dtCol='dt')

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't' + tab_num + '.csv'
df.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)

##################################### TABELA 2938 #####################################

tab_num = '2938'

li_datas_str, data_máx, data_mín = g_data_MinMax(tab_num=tab_num)
df = download_tabela(tab_num, g_li_datas_ibge(data_mín, data_máx))
df = g_cols_cód_desc(df, colCód='códIBGE', colDesc='descCatIBGE')
df = g_col_categoriaIBGE(df, colCód='códIBGE', colCat='tipoCatIBGE')
df = add_cols_catBC(df, tab_num=tab_num, colCódDF='códIBGE', colCódPlanilha='código', colDescPlanilha='descrição')
df = g_col_dt(df, dtCol='dt')

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't' + tab_num + '.csv'
df.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)

#################################################################################################
##################################### DOWNLOAD ATUALIZAÇÕES #####################################
##################################### CRIA BASE PARA TESTES #####################################
#################################################################################################
# del df

def g_base_incompleta(arq_nome, pasta, exclusões, salva=False):
    
    # tab_num = '7060'
    # pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
    # arq_nome = 't' + tab_num + '.csv'
    
    df = pd.read_csv(pasta / arq_nome,
                                  delimiter = '|',
                                  decimal=',',
                                  dtype='str',
                                  parse_dates=['dt'])
    
    li_datas = pd.DatetimeIndex(df['dt'].unique()) # passo (aplicar a função pd.DatetimeIndex) essencial para aplicar as funções min() e max()
    
    # exclusões = ['2020-01-01', '2020-05-01']
    
    # cond1 = df['dt'] != '2020-01-01'
    # cond2 = df['dt'] != '2020-05-01'
    
    for exclusão in exclusões:
        cond1 = df['dt'] != exclusão
        df = df.loc[cond1,:]
    
    if salva == True:
        novo_arq_nome = '(incompleto)' + arq_nome
        print(f'Salvando DF incompleto: {novo_arq_nome}')
        df.to_csv(pasta / novo_arq_nome, sep='|', decimal=',', index=False)
    
    return df

arq_nome = 't7060.csv'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
exclusões = ['2020-01-01', '2020-05-01']

df_incompleto = g_base_incompleta(arq_nome, pasta, exclusões, salva=True)

li_datas_incompleto = pd.DatetimeIndex(df_incompleto['dt'].unique())

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't' + tab_num + '(incompleto).csv'
df.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)
# arquivo: t7060(incompleto).csv


#################################################################################################
##################################### DOWNLOAD ATUALIZAÇÕES #####################################
#################################################################################################
del df


tab_num = '7060'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
# arq_nome = 't' + tab_num + '.csv'

arq_nome = 't7060.csv'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
exclusões = ['2020-01-01', '2020-05-01']

df_incompleto = g_base_incompleta(arq_nome, pasta, exclusões, salva=True)

# li_datas = pd.DatetimeIndex(df_incompleto['dt'].unique())

def g_li_datas_faltantes(df, tab_num):
    # Precisa da função g_data_MinMax(tab_num=tab_num)
    print('Comparando datas do df com a nuvem, e gerando lista de datas faltantes')
    li_datas = pd.DatetimeIndex(df['dt'].unique()) # passo (aplicar a função pd.DatetimeIndex) essencial para aplicar as funções min() e max()
    li_datas_str = [str(dt.year) + str(dt.month).zfill(2) for dt in li_datas]
    set_datas_str_noDataset = set(li_datas_str)
    
    li_datas_str, _, _ = g_data_MinMax(tab_num=tab_num)
    set_datas_str_naNuvem = set(li_datas_str)
    
    li_datas_faltantes = list(set_datas_str_naNuvem - set_datas_str_noDataset)
    
    return li_datas_faltantes

def atualiza_df(df, tab_num):
    df = df.copy()
    # Lista os dados faltantes
    li_datas_faltantes = g_li_datas_faltantes(df, tab_num='7060')
    # Baixa os dados faltantes para df2
    print('Baixando os dados faltantes')
    df2 = download_tabela(tab_num, li_datas_faltantes)
    df2 = g_cols_cód_desc(df2, colCód='códIBGE', colDesc='descCatIBGE')
    df2 = g_col_categoriaIBGE(df2, colCód='códIBGE', colCat='tipoCatIBGE')
    df2 = add_cols_catBC(df2, tab_num=tab_num, colCódDF='códIBGE', colCódPlanilha='código', colDescPlanilha='descrição')
    df2 = g_col_dt(df2, dtCol='dt')
    # Junta df2 a df
    print('Juntando DFs')
    df = df.append(df2)
    print('Ordenando')
    df.sort_values(by=['dt'],inplace=True)
    return df

df_completo = atualiza_df(df_incompleto, tab_num)

# li_datas = pd.DatetimeIndex(df_completo['dt'].unique())

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = 't' + tab_num + '(completo).csv'
df_completo.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)

#################################################################################################
##################################### ATUALIZA ARQUIVO ##########################################
#################################################################################################

def atualiza_csv(arq_nome, pasta, salva=False):
    
    # arq_nome = 't7060(incompleto).csv'
    # pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
    
    df_incompleto = pd.read_csv(pasta / arq_nome,
                                  delimiter = '|',
                                  decimal=',',
                                  dtype='str',
                                  parse_dates=['dt'])
    
    df_completo = atualiza_df(df_incompleto, tab_num)
    
    if salva == True:
        print('Salvando')
        df_completo.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)
    
    return df_completo


arq_nome = 't7060.csv'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
exclusões = ['2020-01-01', '2020-05-01']

df_incompleto = g_base_incompleta(arq_nome, pasta, exclusões, salva=True)

arq_nome = '(incompleto)t7060.csv'
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'

df_arq_completo = atualiza_csv(arq_nome=arq_nome, pasta=pasta, salva=True)

# li_datas = pd.DatetimeIndex(df_arq_completo['dt'].unique())
















