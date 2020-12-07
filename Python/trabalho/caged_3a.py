# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:28:09 2020

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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

def g_nome_arq(início, final, prefixo, sufixo):
    
    #início = '2020-04'
    #final = '2020-08'
    #prefixo = 'CAGEDMOV'
    #sufixo ='.csv'
    
    li_arqs_nomes = []
    início_com_dia = início + '-01'
    final_com_dia = final + '-01'
    df_datas = pd.to_datetime(np.arange(início_com_dia, final_com_dia, 1, dtype='datetime64[M]')).to_frame()#.reset_index()
    df_datas.rename(mapper={0:'col_data'},axis=1,inplace=True)
    
    nova_linha = pd.DataFrame({'col_data': pd.date_range(start=df_datas['col_data'].iloc[-1], periods=2, freq='MS', closed='right')})
    df_datas = df_datas.append(nova_linha)
    
    df_datas['col_data'] = df_datas['col_data'].astype('str')
    df_datas['col_data'] = (df_datas['col_data'].str.slice(0,4) + df_datas['col_data'].str.slice(4,7)).str.replace('-','')
    for index, row in df_datas.iterrows():
        arq_nome = prefixo + row['col_data'] + sufixo
        li_arqs_nomes.append(arq_nome)
    return li_arqs_nomes

li_arquivos = g_nome_arq(início='2018-01', final='2020-09', prefixo='CAGEDMOV', sufixo='.csv')

pasta = caminho_base / 'Dados'
df_municipios = pd.read_excel(pasta/'municipios.xlsx', sheet_name='municipios')
df_municipios = df_municipios[['mun_cod6_ibge','uf_sigla']]

dtype = {'subclasse':'str','classe':'str', 'competência':'str'}

arq_nome = 'CAGEDMOV202009.csv'
import pandas as pd
pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',',
                 dtype=dtype)
print(df.dtypes)
df = df.merge(df_municipios,how='left',left_on='mun_cod6_ibge',right_on='mun_cod6_ibge')

df['year'] = df['competência'].str.slice(0,4)
df['month'] = df['competência'].str.slice(4,6)
df['day'] = 1
df['dt'] = pd.to_datetime(df[['year', 'month', 'day']])
df.drop(['year','month','day','competência'],axis=1,inplace=True)

#######################################################################################################

def cgd_01a(uf, início, final):
    
    dtype = {'subclasse':'str','classe':'str', 'competência':'str'}
    
    pasta = caminho_base / 'Dados'
    df_municipios = pd.read_excel(pasta/'municipios.xlsx', sheet_name='municipios')
    df_municipios = df_municipios[['mun_cod6_ibge','uf_sigla']]
    
    def g_nome_arq(início, final, prefixo, sufixo):
        li_arqs_nomes = []
        início_com_dia = início + '-01'
        final_com_dia = final + '-01'
        df_datas = pd.to_datetime(np.arange(início_com_dia, final_com_dia, 1, dtype='datetime64[M]')).to_frame()#.reset_index()
        df_datas.rename(mapper={0:'col_data'},axis=1,inplace=True)
        
        nova_linha = pd.DataFrame({'col_data': pd.date_range(start=df_datas['col_data'].iloc[-1], periods=2, freq='MS', closed='right')})
        df_datas = df_datas.append(nova_linha)
        
        df_datas['col_data'] = df_datas['col_data'].astype('str')
        df_datas['col_data'] = (df_datas['col_data'].str.slice(0,4) + df_datas['col_data'].str.slice(4,7)).str.replace('-','')
        for index, row in df_datas.iterrows():
            arq_nome = prefixo + row['col_data'] + sufixo
            li_arqs_nomes.append(arq_nome)
        return li_arqs_nomes
    
    li_arquivos = g_nome_arq(início=início, final=final, prefixo='CAGEDMOV', sufixo='.csv')
    
    for index_arq, arq_nome in enumerate(li_arquivos):
        print(arq_nome)
        pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
        df = pd.read_csv(pasta / arq_nome,
                         delimiter = ';',
                         decimal=',',
                         dtype=dtype)
        df = df.merge(df_municipios,how='left',left_on='mun_cod6_ibge',right_on='mun_cod6_ibge')
        
        if uf != 'BR':
            cond1 = df['uf_sigla'] == uf
            df = df.loc[cond1, :]
        
        df['year'] = df['competência'].str.slice(0,4)
        df['month'] = df['competência'].str.slice(4,6)
        df['day'] = 1
        df['dt'] = pd.to_datetime(df[['year', 'month', 'day']])
        df.drop(['year','month','day','competência'],axis=1,inplace=True)

        df = df.groupby(['dt','cnae2_subclasse_cod7'])['saldomovimentação'].sum().to_frame().reset_index()
        
        if index_arq == 0:
            df_bruto = df.copy()
        else:
            df_bruto = df_bruto.append(df)
    
    df_bruto.index = range(len(df_bruto))
    
    return df_bruto
#######################################################################################################

df = cgd_01a(uf='MS', início='2018-01', final='2020-09')

print(df1.dtypes)

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
dicionário1 = {}
df_cp = df.copy()
print(df_cp.dtypes)

######################################################################################################
########## Mensal - Valor ############################################################################
######################################################################################################

tot_mensal = df_cp.groupby(['dt'])['saldomovimentação'].sum().to_frame()
tot_mensal.rename(mapper={'saldomovimentação':'total'},axis=1,inplace=True)
tot_mensal.index.freq = 'MS'
dicionário1['Mensal - Valor'] = tot_mensal


unicos = list(df_cp['cnae2_subclasse_cod7'].unique())
for index_unico, unico in enumerate(unicos):
    cond1 = df_cp['cnae2_subclasse_cod7'] == unico
    filtro = df_cp.loc[cond1,['dt','saldomovimentação']]
    filtro.rename(mapper={'saldomovimentação':unico},axis=1,inplace=True)
    filtro.set_index('dt',inplace=True)
    dicionário1['Mensal - Valor'] = dicionário1['Mensal - Valor'].merge(filtro,how='left',left_index=True,right_index=True)

dicionário1['Mensal - Valor'].fillna(0,inplace=True)

######################################################################################################
########## Acumulado no Ano - Valor ##################################################################
######################################################################################################

df_acumAno = dicionário1['Mensal - Valor'].copy()
df_acumAno['dt_ano'] = df_acumAno.index.year
colunas = list(set(list(df_acumAno.columns)) - {'dt_ano'})
for coluna in colunas:
    df_acumAno[coluna] = df_acumAno.groupby(['dt_ano'])[coluna].cumsum()
df_acumAno.drop(['dt_ano'],axis=1,inplace=True)
#     --->>>> Coloca no dicionário1 <<<<< ---   #
dicionário1['Acumulado no Ano - Valor'] = df_acumAno

######################################################################################################
########## Acumulado em 12 meses - Valor #############################################################
######################################################################################################
df_acum12m = dicionário1['Mensal - Valor'].copy()
colunas = list(df_acum12m.columns)
for coluna in colunas:
    df_acum12m[coluna] = df_acum12m[coluna].rolling(12).sum()
df_acum12m.dropna(thresh=1, inplace=True)
#     --->>>> Coloca no dicionário1 <<<<< ---   #
dicionário1['Acumulado em 12 meses - Valor'] = df_acum12m

######################################################################################################
########## Média Móvel de 12 meses - Valor ###########################################################
######################################################################################################
df_media12m = dicionário1['Mensal - Valor'].copy()
colunas = list(df_media12m.columns)
for coluna in colunas:
    df_media12m[coluna] = df_media12m[coluna].rolling(12).mean()
df_media12m.dropna(thresh=1, inplace=True)

#     --->>>> Coloca no dicionário1 <<<<< ---   #
dicionário1['Média Móvel de 12 meses - Valor'] = df_media12m

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/ Entradas do dicionário1 até aqui \/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

l_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor','Média Móvel de 12 meses - Valor'])

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/ Participação /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

colunas = list(set(list(dicionário1['Mensal - Valor'].columns)) - {'total'})

novos_nomes = l_variaveis.str.replace('- Valor','- Participação')

for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
    
    df_part = dicionário1[l_variavel].copy()
    for coluna in colunas:
        df_part[coluna] = (df_part[coluna] / df_part['total']) * 100
    
    df_part.dropna(thresh=1, inplace=True)
    df_part['total'] = 100
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1[novo_nome] = df_part




# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao ano anterior')

for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
    
    df_varB = dicionário1[l_variavel].copy()
    df_varB_L12 = df_varB.shift(periods=12)
    colunas = list(df_varB.columns)
    
    for coluna in colunas:
        df_varB[coluna] = df_varB[coluna] - df_varB_L12[coluna]
    df_varB.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_varB.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1[novo_nome] = df_varB

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao ano anterior')

for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
    
    df_varP = dicionário1[l_variavel].copy()
    df_varP_L12 = df_varP.shift(periods=12)
    colunas = list(df_varP.columns)
    
    for coluna in colunas:
        df_varP[coluna] = ((df_varP[coluna] - df_varP_L12[coluna]) / df_varP_L12[coluna]) * 100
    df_varP.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_varP.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1[novo_nome] = df_varP

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao mês anterior')

for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
    
    df_varB = dicionário1[l_variavel].copy()
    df_varB_L1 = df_varB.shift(periods=1)
    colunas = list(df_varB.columns)
    
    for coluna in colunas:
        df_varB[coluna] = df_varB[coluna] - df_varB_L1[coluna]
    df_varB.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_varB.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1[novo_nome] = df_varB

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao mês anterior')

for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
    
    df_varP = dicionário1[l_variavel].copy()
    df_varP_L1 = df_varP.shift(periods=1)
    colunas = list(df_varP.columns)
    
    for coluna in colunas:
        df_varP[coluna] = ((df_varP[coluna] - df_varP_L1[coluna]) / df_varP_L1[coluna]) * 100
    df_varP.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_varP.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1[novo_nome] = df_varP

######################################################################################################################
############################## Função que retorna duas listas com as variáveis mais e menos importantes ##############
######################################################################################################################

def mais_relevantes(df):
    # Copia o data frame
    df_cp = df.copy()
    # Cria coluna do mês por extenso
    df_cp['dt_ano_mes'] = df_cp.index.year.astype('str') + '_' + df_cp.index.month.astype('str')
    # Deleta coluna do total
    df_cp.drop(['total'],axis=1,inplace=True)
    # Pega o último mês, que vai servir de referência para a ordenação
    ultimo = df_cp.iloc[-1,-1]
    # Ordena o index por ordem decrescente
    df_cp.sort_index(ascending=False, inplace=True)
    # Coloca o mês string no índice
    df_cp.set_index('dt_ano_mes',inplace=True)
    # Transpõe o df
    df_longo = df_cp.T
    # Ordena pela coluna do último mês
    df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
    # Seleciona os setores MAIS e MENOS importantes
    df_importantesMais = df_longo.iloc[0:10,:]
    df_importantesMenos = df_longo.iloc[10:,:]
    # Coloca na lista as variáveis dos setores MAIS e MENOS importantes (usado nos loopings do próximo bloco)
    li_importantesMais_variaveis = list(df_importantesMais.copy().reset_index()['index'])
    li_importantesMenos_variaveis = list(df_importantesMenos.copy().reset_index()['index'])
    
    return li_importantesMais_variaveis, li_importantesMenos_variaveis, ultimo

li_importantesMais_variaveis, li_importantesMenos_variaveis, ultimo = mais_relevantes(dicionário1['Acumulado em 12 meses - Valor'])


########################################################################################################
########### Top: Mensal, Acumulado no ano, acumulado em 12 meses, e média móvel de 12 meses ############
########################################################################################################

dicionário2 = {}

# Coloca na lista as variáveis dos setores MAIS e MENOS importantes

li_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor', 'Média Móvel de 12 meses - Valor'])

# ------------------------------------------------------------------------------------------------------

for vl_variavel in li_variaveis:
    
    #vl_variavel = 'Mensal - Valor'
    
    # Copia o df
    df_cp = dicionário1[vl_variavel].copy()
    # Deleta coluna das exportações ou importações
    df_cp.drop(['total'],axis=1,inplace=True)
    # Cria coluna do mês por extenso
    df_cp['dt_ano_mes'] = df_cp.index.year.astype('str') + '_' + df_cp.index.month.astype('str')
    # Ordena o index por ordem decrescente
    df_cp.sort_index(ascending=False, inplace=True)
    # Coloca o mês string no índice
    df_cp.set_index('dt_ano_mes',inplace=True)
    # Transpõe o df
    df_longo = df_cp.T
    # Ordena pela coluna do último mês
    df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
    
    # Seleciona os setores MAIS e MENOS importantes
    df_importantesMais = df_longo.loc[li_importantesMais_variaveis,:]
    df_importantesMenos = df_longo.loc[li_importantesMenos_variaveis,:]
    
    # Ordena o df curto pelos mais importantes
    df_importantesMais.sort_values(by=[ultimo],ascending=[False],inplace=True)
    
    # Soma (ao longo das linhas), para cada mês (nas colunas), o valor dos setores menos importantes
    df_importantesMenos_soma = df_importantesMenos.sum(axis=0).to_frame().T
    
    # Renomeia a linha da soma para 'Outros'
    df_importantesMenos_soma.rename(mapper={0:'Outros'},axis=0,inplace=True)
    
    # Junta a soma dos valores menos importantes aos setores mais importantes
    df_importantesMais = df_importantesMais.append(df_importantesMenos_soma)
    
    # Cria linha com total geral
    df_importantesMais.loc['Total Geral',:] = df_importantesMais.sum(axis=0)
    
    nome_longo = vl_variavel + ' - Maiores setores (longo)'
    nome_curto = vl_variavel + ' - Maiores setores (curto)'
    
    # Adiciona a dicionário2
    dicionário2[nome_longo] = df_longo.copy()
    dicionário2[nome_curto] = df_importantesMais.copy()

####################################################################################################

dtype = {'subclasse':'str','classe':'str', 'competência':'str'}

arq_nome = 'cnae20_subclasse_desc.csv'
import pandas as pd
pasta = caminho_base / 'Dados' / 'cnae e ncm'
df_subclasse_desc = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',')


df2 = dicionário2['Mensal - Valor - Maiores setores (curto)'].merge(df_subclasse_desc,how='left',left_index=True,right_on='subclasse')

















#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

def cgd_01b(uf, início, final):
    
    dicionário1 = {}
    #milhoes = True
    #tipo = 'EXP'
    #uf = 'RJ'
    #anos = [2018,2019,2020]
    #categoria = 'NO_ISIC_DIVISAO'
    
    df_uf = cgd_01a(uf='MS', início='2020-04', final='2020-08')
    
    #df_tipo_uf = mdic_01c(tipo=tipo,uf=uf, anos=anos)
    #df_tipo_uf = mdic_01c(tipo='EXP',uf='MS', anos=[2018,2019,2020])
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Valor /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    ######################################################################################################
    ########## Mensal - Valor ############################################################################
    ######################################################################################################
    
    tot_mensal = df_uf.groupby(['dt'])['saldomovimentação'].sum().to_frame()
    
    tot_mensal.rename(mapper={'saldomovimentação':'total'},axis=1,inplace=True)
    tot_mensal.index.freq = 'MS'
    
    dicionário1['Mensal - Valor'] = tot_mensal
    
    

    
    
    unicos = list(soma[categoria].unique())
    for index_unico, unico in enumerate(unicos):
        #print(unico)
        cond1 = soma[categoria] == unico
        filtro = soma.loc[cond1,['dt','VL_FOB']]
        filtro.rename(mapper={'VL_FOB':unico},axis=1,inplace=True)
        filtro.set_index('dt',inplace=True)
        dicionário1['Mensal - Valor'] = dicionário1['Mensal - Valor'].merge(filtro,how='left',left_index=True,right_index=True)
    
    dicionário1['Mensal - Valor'].fillna(0,inplace=True)
    
    ######################################################################################################
    ########## Acumulado no Ano - Valor ##################################################################
    ######################################################################################################
    df_acumAno = dicionário1['Mensal - Valor'].copy()
    df_acumAno['dt_ano'] = df_acumAno.index.year
    colunas = list(set(list(df_acumAno.columns)) - {'dt_ano'})
    for coluna in colunas:
        df_acumAno[coluna] = df_acumAno.groupby(['dt_ano'])[coluna].cumsum()
    df_acumAno.drop(['dt_ano'],axis=1,inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1['Acumulado no Ano - Valor'] = df_acumAno
    
    ######################################################################################################
    ########## Acumulado em 12 meses - Valor #############################################################
    ######################################################################################################
    df_acum12m = dicionário1['Mensal - Valor'].copy()
    colunas = list(df_acum12m.columns)
    for coluna in colunas:
        df_acum12m[coluna] = df_acum12m[coluna].rolling(12).sum()
    df_acum12m.dropna(thresh=1, inplace=True)
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1['Acumulado em 12 meses - Valor'] = df_acum12m
    
    ######################################################################################################
    ########## Média Móvel de 12 meses - Valor ###########################################################
    ######################################################################################################
    df_media12m = dicionário1['Mensal - Valor'].copy()
    colunas = list(df_media12m.columns)
    for coluna in colunas:
        df_media12m[coluna] = df_media12m[coluna].rolling(12).mean()
    df_media12m.dropna(thresh=1, inplace=True)
    
    #     --->>>> Coloca no dicionário1 <<<<< ---   #
    dicionário1['Média Móvel de 12 meses - Valor'] = df_media12m
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Entradas do dicionário1 até aqui \/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    l_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor','Média Móvel de 12 meses - Valor'])
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Participação /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    colunas = list(set(list(dicionário1['Mensal - Valor'].columns)) - {tipo_extenso})
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Participação')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_part = dicionário1[l_variavel].copy()
        for coluna in colunas:
            df_part[coluna] = (df_part[coluna] / df_part[tipo_extenso]) * 100
        
        df_part.dropna(thresh=1, inplace=True)
        df_part[tipo_extenso] = 100
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_part
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao ano anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varB = dicionário1[l_variavel].copy()
        df_varB_L12 = df_varB.shift(periods=12)
        colunas = list(df_varB.columns)
        
        for coluna in colunas:
            df_varB[coluna] = df_varB[coluna] - df_varB_L12[coluna]
        df_varB.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varB.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varB
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao ano anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varP = dicionário1[l_variavel].copy()
        df_varP_L12 = df_varP.shift(periods=12)
        colunas = list(df_varP.columns)
        
        for coluna in colunas:
            df_varP[coluna] = ((df_varP[coluna] - df_varP_L12[coluna]) / df_varP_L12[coluna]) * 100
        df_varP.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varP.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varP
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao mês anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varB = dicionário1[l_variavel].copy()
        df_varB_L1 = df_varB.shift(periods=1)
        colunas = list(df_varB.columns)
        
        for coluna in colunas:
            df_varB[coluna] = df_varB[coluna] - df_varB_L1[coluna]
        df_varB.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varB.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varB
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao mês anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varP = dicionário1[l_variavel].copy()
        df_varP_L1 = df_varP.shift(periods=1)
        colunas = list(df_varP.columns)
        
        for coluna in colunas:
            df_varP[coluna] = ((df_varP[coluna] - df_varP_L1[coluna]) / df_varP_L1[coluna]) * 100
        df_varP.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varP.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário1 <<<<< ---   #
        dicionário1[novo_nome] = df_varP

    
    ######################################################################################################################
    ############################## Função que retorna duas listas com as variáveis mais e menos importantes ##############
    ######################################################################################################################
    
    def mais_relevantes(df):
        # Copia o data frame
        df_cp = df.copy()
        # Cria coluna do mês por extenso
        df_cp['dt_ano_mes'] = df_cp.index.year.astype('str') + '_' + df_cp.index.month.astype('str')
        # Deleta coluna das exportações ou importações
        df_cp.drop([tipo_extenso],axis=1,inplace=True)
        # Pega o último mês, que vai servir de referência para a ordenação
        ultimo = df_cp.iloc[-1,-1]
        # Ordena o index por ordem decrescente
        df_cp.sort_index(ascending=False, inplace=True)
        # Coloca o mês string no índice
        df_cp.set_index('dt_ano_mes',inplace=True)
        # Transpõe o df
        df_longo = df_cp.T
        # Ordena pela coluna do último mês
        df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
        # Seleciona os setores MAIS e MENOS importantes
        df_importantesMais = df_longo.iloc[0:10,:]
        df_importantesMenos = df_longo.iloc[10:,:]
        # Coloca na lista as variáveis dos setores MAIS e MENOS importantes (usado nos loopings do próximo bloco)
        li_importantesMais_variaveis = list(df_importantesMais.copy().reset_index()['index'])
        li_importantesMenos_variaveis = list(df_importantesMenos.copy().reset_index()['index'])
        
        return li_importantesMais_variaveis, li_importantesMenos_variaveis, ultimo
    
    li_importantesMais_variaveis, li_importantesMenos_variaveis, ultimo = mais_relevantes(dicionário1['Acumulado em 12 meses - Valor'])
    
    
    ########################################################################################################
    ########### Top: Mensal, Acumulado no ano, acumulado em 12 meses, e média móvel de 12 meses ############
    ########################################################################################################
    
    dicionário2 = {}
    
    # Coloca na lista as variáveis dos setores MAIS e MENOS importantes
    
    li_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor', 'Média Móvel de 12 meses - Valor'])
    
    # ------------------------------------------------------------------------------------------------------
    
    for vl_variavel in li_variaveis:
        
        #vl_variavel = 'Mensal - Valor'
        
        # Copia o df
        df_cp = dicionário1[vl_variavel].copy()
        # Deleta coluna das exportações ou importações
        df_cp.drop([tipo_extenso],axis=1,inplace=True)
        # Cria coluna do mês por extenso
        df_cp['dt_ano_mes'] = df_cp.index.year.astype('str') + '_' + df_cp.index.month.astype('str')
        # Ordena o index por ordem decrescente
        df_cp.sort_index(ascending=False, inplace=True)
        # Coloca o mês string no índice
        df_cp.set_index('dt_ano_mes',inplace=True)
        # Transpõe o df
        df_longo = df_cp.T
        # Ordena pela coluna do último mês
        df_longo.sort_values(by=[ultimo],ascending=[False],inplace=True)
        
        # Seleciona os setores MAIS e MENOS importantes
        df_importantesMais = df_longo.loc[li_importantesMais_variaveis,:]
        df_importantesMenos = df_longo.loc[li_importantesMenos_variaveis,:]
        
        # Soma (ao longo das linhas), para cada mês (nas colunas), o valor dos setores menos importantes
        df_importantesMenos_soma = df_importantesMenos.sum(axis=0).to_frame().T
        
        # Renomeia a linha da soma para 'Outros'
        df_importantesMenos_soma.rename(mapper={0:'Outros'},axis=0,inplace=True)
        
        # Junta a soma dos valores menos importantes aos setores mais importantes
        df_importantesMais = df_importantesMais.append(df_importantesMenos_soma)
        
        # Cria linha com total geral
        df_importantesMais.loc['Total Geral',:] = df_importantesMais.sum(axis=0)
        
        nome_longo = vl_variavel + ' - Maiores setores (longo)'
        nome_curto = vl_variavel + ' - Maiores setores (curto)'
        
        # Adiciona a dicionário2
        dicionário2[nome_longo] = df_longo.copy()
        dicionário2[nome_curto] = df_importantesMais.copy()
    
    return dicionário1, dicionário2

dic1, dic2 = mdic_01d(tipo='EXP', uf='RJ', anos=[2018,2019,2020], milhoes=True, categoria='NO_ISIC_DIVISAO')

dic3, dic4 = mdic_01d(tipo='EXP', uf='RJ', anos=[2018,2019,2020], milhoes=True, categoria='CO_NCM')

teste = dic4['Mensal - Valor - Maiores setores (curto)']
teste['CO_NCM'] = pd.to_numeric(teste.index,errors='coerce')


pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
cod_ncm = pd.read_csv(pasta / 'NCM.csv',
                 encoding = 'latin',
                 delimiter = ';')

cod_ncm = cod_ncm[['CO_NCM','NO_NCM_POR']]
print(teste['CO_NCM'].dtype)

teste = teste.merge(cod_ncm,how='left',left_index=True,right_on='CO_NCM')



_, dic4_MS = mdic_01d(tipo='EXP', uf='MS', anos=[2018,2019,2020], milhoes=True, categoria='CO_NCM')
teste = dic4_MS['Mensal - Valor - Maiores setores (curto)']
teste['CO_NCM'] = pd.to_numeric(teste.index,errors='coerce')
teste = teste.merge(cod_ncm,how='left',left_index=True,right_on='CO_NCM')



















