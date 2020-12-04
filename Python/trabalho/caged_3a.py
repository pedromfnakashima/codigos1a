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
    li_arqs_nomes = []
    início_com_dia = início + '-01'
    final_com_dia = final + '-01'
    datas = pd.to_datetime(np.arange(início_com_dia,final_com_dia, 1, dtype='datetime64[M]')).to_frame().reset_index()
    datas['index'] = datas['index'].astype('str')
    datas['index'] = (datas['index'].str.slice(0,4) + datas['index'].str.slice(4,7)).str.replace('-','')
    for index, row in datas.iterrows():
        arq_nome = prefixo + row['index'] + sufixo
        li_arqs_nomes.append(arq_nome)
    return li_arqs_nomes

li_arquivos = g_nome_arq(início='2020-04', final='2020-08', prefixo='CAGEDMOV', sufixo='.csv')

pasta = caminho_base / 'Dados'
df_municipios = pd.read_excel(pasta/'municipios.xlsx', sheet_name='municipios')
df_municipios = df_municipios[['mun_cod_ibge6','uf_sigla']]


arq_nome = 'CAGEDMOV202009.csv'
import pandas as pd
pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',')


df = df.merge(df_municipios,how='left',left_on='município',right_on='mun_cod_ibge6')





cgd_01a(uf='MS', início='2020-04', final='2020-08'):



def cgd_01a(uf, início, final):
    
    pasta = caminho_base / 'Dados'
    df_municipios = pd.read_excel(pasta/'municipios.xlsx', sheet_name='municipios')
    df_municipios = df_municipios[['mun_cod_ibge6','uf_sigla']]
    
    def g_nome_arq(início, final, prefixo, sufixo):
        li_arqs_nomes = []
        início_com_dia = início + '-01'
        final_com_dia = final + '-01'
        datas = pd.to_datetime(np.arange(início_com_dia,final_com_dia, 1, dtype='datetime64[M]')).to_frame().reset_index()
        datas['index'] = datas['index'].astype('str')
        datas['index'] = (datas['index'].str.slice(0,4) + datas['index'].str.slice(4,7)).str.replace('-','')
        for index, row in datas.iterrows():
            arq_nome = prefixo + row['index'] + sufixo
            li_arqs_nomes.append(arq_nome)
        return li_arqs_nomes
    
    li_arquivos = g_nome_arq(início='2020-04', final='2020-08', prefixo='CAGEDMOV', sufixo='.csv')
    
    for index_arq, arq_nome in enumerate(li_arquivos):
        
        pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
        df = pd.read_csv(pasta / arq_nome,
                         delimiter = ';',
                         decimal=',')
        
        if uf != 'BR':
            cond1 = df['SG_UF_NCM'] == uf
            df = df.loc[cond1, :]
        
        df.rename(columns={'CO_ANO':'year','CO_MES':'month'},inplace=True)
        df['day'] = 1
        df['dt'] = pd.to_datetime(df[['year', 'month', 'day']])
        df = df.groupby(['dt','CO_NCM'])['VL_FOB'].sum().to_frame().reset_index()
        if index_ano == 0:
            df_bruto = df.copy()
        else:
            df_bruto = df_bruto.append(df)
    df_bruto.index = range(len(df_bruto))
    if tipo == 'EXP':
        pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
        catsExp = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='4')
        catsExp = catsExp[['CO_NCM','NO_ISIC_DIVISAO','NO_ISIC_SECAO']]
        df_bruto = df_bruto.merge(catsExp,how='left',left_on='CO_NCM',right_on='CO_NCM')
    elif  tipo == 'IMP':
        pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
        catsImp = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='3')
        catsImp = catsImp[['CO_NCM','NO_CGCE_N1','NO_CGCE_N3']]
        df_bruto = df_bruto.merge(catsImp,how='left',left_on='CO_NCM',right_on='CO_NCM')
    return df_bruto
#######################################################################################################

def cgd_01b(tipo, uf, anos, milhoes, categoria):
    
    dicionário1 = {}
    #milhoes = True
    #tipo = 'EXP'
    #uf = 'RJ'
    #anos = [2018,2019,2020]
    #categoria = 'NO_ISIC_DIVISAO'
    
    df_tipo_uf = mdic_01c(tipo=tipo,uf=uf, anos=anos)
    #df_tipo_uf = mdic_01c(tipo='EXP',uf='MS', anos=[2018,2019,2020])
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Valor /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    ######################################################################################################
    ########## Mensal - Valor ############################################################################
    ######################################################################################################
    
    tipo_tot_mensal = df_tipo_uf.groupby(['dt'])['VL_FOB'].sum().to_frame()
    
    if tipo == 'EXP':
        tipo_extenso = 'Exportações'
    elif tipo == 'IMP':
        tipo_extenso = 'Importações'
    
    tipo_tot_mensal.rename(mapper={'VL_FOB':tipo_extenso},axis=1,inplace=True)
    tipo_tot_mensal.index.freq = 'MS'
    
    dicionário1['Mensal - Valor'] = tipo_tot_mensal
    
    soma = df_tipo_uf.groupby(['dt',categoria])['VL_FOB'].sum().to_frame()
    soma.reset_index(inplace=True)
    
    if milhoes == True:
        soma['VL_FOB'] = soma['VL_FOB'] / 1_000_000
        dicionário1['Mensal - Valor'] = dicionário1['Mensal - Valor'] / 1_000_000
    
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











































##########################################################################################################
##########################################################################################################
##########################################################################################################


arq_nome = 'CAGEDMOV200701.csv'
arq_nome = 'CAGEDMOV201912.csv'
arq_nome = 'CAGEDMOV202001.csv'

import pandas as pd
pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',')

import glob
import pandas as pd
from pathlib import Path

os.chdir(pasta)

pasta = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv_processados'
os.chdir(pasta)

for arq_num, arq_nome in enumerate(glob.glob('*.csv')):
    print(arq_nome)
    
    df = pd.read_csv(pasta / arq_nome,
                 delimiter = ';',
                 decimal=',')
    
    try:
        df.drop(['classe.1'],axis=1,inplace=True)
        df.to_csv(arq_nome, sep=';', decimal=',', index=False)
    except KeyError:
        print('coluna "classe.1" não encontrada')
    else:
        print('coluna "classe.1" deletada')







    











