# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:15:25 2020

@author: pedro-salj
"""

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
import numpy as np
import pandas as pd
##########################################################################################################
##########################################################################################################
##########################################################################################################

########################################################################################
############ Exportações do Estado segundo as principais indústrias ####################
########################################################################################






##########################################################################################################
##########################################################################################################
##########################################################################################################

def mdic_01c(tipo, uf, anos):
    for index_ano, ano in enumerate(anos):
        arq_nome = tipo + '_' + str(ano) + '.csv'
        
        pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
        df = pd.read_csv(pasta / arq_nome,
                         encoding = 'latin',
                         delimiter = ';')
        
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
########################################################################################

dicionário = {}



df_exp = mdic_01c(tipo='EXP',uf='RJ', anos=[2018,2019,2020])
#df_exp = mdic_01c(tipo='EXP',uf='MS', anos=[2018,2019,2020])

meses = df_exp.groupby(['dt']).head(1)['dt'].to_frame().set_index('dt')
meses.index.freq = 'MS'

# 
soma = df_exp.groupby(['dt','NO_ISIC_DIVISAO'])['VL_FOB'].sum().to_frame()
soma.reset_index(inplace=True)
unicos = list(soma['NO_ISIC_DIVISAO'].unique())
for unico in unicos:
    print(unico)

unico = 'Atividades criativas, artes e entretenimento'
index_unico = 0

unico = 'Extração de petróleo bruto e gás natural'
index_unico = 1
print(unico)

cond1 = soma['NO_ISIC_DIVISAO'] == unico
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.rename(mapper={'VL_FOB':unico},axis=1,inplace=True)
filtro.set_index('dt',inplace=True)

meses_cp = meses.copy()
meses_cp = meses_cp.merge(filtro,how='left',left_index=True,right_index=True)
meses_cp.fillna(0, inplace=True)

if index_unico == 0:
    dicionário['Mensal - Valor'] = meses_cp
else:
    dicionário['Mensal - Valor'] = dicionário['Mensal - Valor'].merge(meses_cp,how='left',left_index=True,right_index=True)



'Mensal - Valor'
'Acumulado no Ano - Valor'
'Acumulado em 12 meses - Valor'



















soma.rename(mapper={'VL_FOB':'Exportações'},axis=1,inplace=True)
df_mensal = soma.copy()












def mdic_01d(uf, anos, milhões=False):
    dicionário = {}
    #################################################################################
    ########## Mensal - Valor #######################################################
    #################################################################################
    df_exp = mdic_01c(tipo='EXP',uf=uf, anos=anos)
    df_imp = mdic_01c(tipo='IMP',uf=uf, anos=anos)
    # EXPORTAÇÕES TOTAIS MENSAIS
    soma = df_exp.groupby(['dt'])['VL_FOB'].sum().to_frame()
    soma.rename(mapper={'VL_FOB':'Exportações'},axis=1,inplace=True)
    df_mensal = soma.copy()
    # IMPORTAÇÕES TOTAIS MENSAIS
    soma = df_imp.groupby(['dt'])['VL_FOB'].sum().to_frame()
    soma.rename(mapper={'VL_FOB':'Importações'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(soma,how='left',left_index=True,right_index=True)
    # EXPORTAÇÕES: BÁSICOS, MANUFATURADOS, SEMIFATURADOS E INDUSTRIALIZADOS
    soma = df_exp.groupby(['dt','NO_FAT_AGREG'])['VL_FOB'].sum().to_frame().reset_index()
    # Exp. Básicos
    cond1 = soma['NO_FAT_AGREG'].str.contains('basicos',case=False)
    filtro = soma.loc[cond1,['dt','VL_FOB']]
    filtro.set_index('dt',inplace=True)
    filtro.rename(mapper={'VL_FOB':'Exp. Básicos'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    # Exp. Manufaturados
    cond1 = soma['NO_FAT_AGREG'].str.contains('\smanufaturados',case=False)
    filtro = soma.loc[cond1,['dt','VL_FOB']]
    filtro.set_index('dt',inplace=True)
    filtro.rename(mapper={'VL_FOB':'Exp. Manufaturados'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    # Exp. Semimanufaturados
    cond1 = soma['NO_FAT_AGREG'].str.contains('\ssemimanufaturados',case=False)
    filtro = soma.loc[cond1,['dt','VL_FOB']]
    filtro.set_index('dt',inplace=True)
    filtro.rename(mapper={'VL_FOB':'Exp. Semimanufaturados'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    # Exp. Industrializados
    df_mensal['Exp. Industrializados'] = df_mensal['Exp. Manufaturados'] + df_mensal['Exp. Semimanufaturados']
    # IMPORTAÇÕES: BENS INDUSTRIAIS, BENS INTERMEDIÁRIOS, BENS DE CAPITAL, COMBUSTÍVEIS E LUBRIFICANTES, BENS DE CONSUMO DURÁVEIS E NÃO DURÁVEIS, NÃO CLASSIFICADOS
    soma = df_imp.groupby(['dt','NO_CGCE_N1'])['VL_FOB'].sum().to_frame().reset_index()
    # Imp. Bens Intermediários
    cond1 = soma['NO_CGCE_N1'].str.contains('\sintermediários',case=False)
    filtro = soma.loc[cond1,['dt','VL_FOB']]
    filtro.set_index('dt',inplace=True)
    filtro.rename(mapper={'VL_FOB':'Imp. Bens Intermediários'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    # Imp. Bens de Capital
    cond1 = soma['NO_CGCE_N1'].str.contains('\scapital',case=False)
    filtro = soma.loc[cond1,['dt','VL_FOB']]
    filtro.set_index('dt',inplace=True)
    filtro.rename(mapper={'VL_FOB':'Imp. Bens de Capital'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    # Imp. Bens Industriais
    df_mensal['Imp. Bens Industriais'] = df_mensal['Imp. Bens Intermediários'] + df_mensal['Imp. Bens de Capital']
    # Imp. Combustíveis e Lubrificantes
    cond1 = soma['NO_CGCE_N1'].str.contains('^combustíveis',case=False)
    filtro = soma.loc[cond1,['dt','VL_FOB']]
    filtro.set_index('dt',inplace=True)
    filtro.rename(mapper={'VL_FOB':'Imp. Combustíveis e Lubrificantes'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(filtro,how='left',left_index=True,right_index=True)
    # Imp. Bens de Consumo não-duráveis
    cond1 = df_imp['NO_CGCE_N1'].str.contains('bc',case=False)
    cond2 = df_imp['NO_CGCE_N3'].str.contains('alimentos',case=False)
    cond3 = df_imp['NO_CGCE_N3'].str.contains('não\sduráveis',case=False)
    cond4 = df_imp['NO_CGCE_N3'].str.contains('semiduráveis',case=False)
    cond = cond1 & (cond2 | cond3 | cond4)
    filtro = df_imp.loc[cond,:]
    soma = filtro.groupby(['dt'])['VL_FOB'].sum().to_frame()
    soma.rename(mapper={'VL_FOB':'Imp. Bens de Consumo não-duráveis'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(soma,how='left',left_index=True,right_index=True)
    # Imp. Bens de Consumo duráveis
    cond1 = df_imp['NO_CGCE_N1'].str.contains('bc',case=False)
    cond2 = df_imp['NO_CGCE_N3'].str.contains('automóveis',case=False)
    cond3 = df_imp['NO_CGCE_N3'].str.contains('consumo\sduráveis',case=False)
    cond4 = df_imp['NO_CGCE_N3'].str.contains('Equipamentos',case=False)
    cond = cond1 & (cond2 | cond3 | cond4)
    filtro = df_imp.loc[cond,:]
    soma = filtro.groupby(['dt'])['VL_FOB'].sum().to_frame()
    soma.rename(mapper={'VL_FOB':'Imp. Bens de Consumo duráveis'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(soma,how='left',left_index=True,right_index=True)
    # Imp. Bens de Consumo
    df_mensal['Imp. Bens de Consumo'] = df_mensal['Imp. Bens de Consumo não-duráveis'] + df_mensal['Imp. Bens de Consumo duráveis']
    # Imp. Não Classificados
    cond1 = df_imp['NO_CGCE_N1'].str.contains('não esp',case=False)
    filtro = df_imp.loc[cond1,:]
    soma = filtro.groupby(['dt'])['VL_FOB'].sum().to_frame()
    soma.rename(mapper={'VL_FOB':'Imp. Não Classificados'},axis=1,inplace=True)
    df_mensal = df_mensal.merge(soma,how='left',left_index=True,right_index=True)
    # SALDO COMERCIAL
    df_mensal['Saldo Comercial'] = df_mensal['Exportações'] - df_mensal['Importações']
    # CORRENTE DE COMÉRCIO
    df_mensal['Corrente de Comércio'] = df_mensal['Exportações'] + df_mensal['Importações']
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_mensal.fillna(0, inplace=True)
    #     --->>>> Converte para milhões <<<<< ---   #
    if milhões == True:
        df_mensal = df_mensal / 1_000_000
    #     --->>>> Muda a frequência do index para MS <<<<< ---   #
    df_mensal.index.freq = 'MS'
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Mensal - Valor'] = df_mensal
    #################################################################################
    ########## Acumulado no Ano - Valor #############################################
    #################################################################################
    df_acumAno = df_mensal.copy()
    df_acumAno['dt_ano'] = df_acumAno.index.year
    colunas = list(set(list(df_acumAno.columns)) - {'dt_ano'})
    for coluna in colunas:
        df_acumAno[coluna] = df_acumAno.groupby(['dt_ano'])[coluna].cumsum()
    df_acumAno.drop(['dt_ano'],axis=1,inplace=True)
    #     --->>>> Muda a frequência do index para MS <<<<< ---   #
    df_acumAno.index.freq = 'MS'
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado no Ano - Valor'] = df_acumAno
    #################################################################################
    ########## Acumulado em 12 meses - Valor ########################################
    #################################################################################
    df_acum12m = df_mensal.copy()
    colunas = list(df_acum12m.columns)
    for coluna in colunas:
        df_acum12m[coluna] = df_acum12m[coluna].rolling(12).sum()
    df_acum12m.dropna(thresh=1, inplace=True)
    #     --->>>> Muda a frequência do index para MS <<<<< ---   #
    df_acum12m.index.freq = 'MS'
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado em 12 meses - Valor'] = df_acum12m
    #################################################################################
    ########## Média de 12 meses - Valor ############################################
    #################################################################################
    df_media12m = df_mensal.copy()
    colunas = list(df_media12m.columns)
    for coluna in colunas:
        df_media12m[coluna] = df_media12m[coluna].rolling(12).mean()
    df_media12m.dropna(thresh=1, inplace=True)
    #     --->>>> Muda a frequência do index para MS <<<<< ---   #
    df_media12m.index.freq = 'MS'
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Média de 12 meses - Valor'] = df_media12m
    #################################################################################
    ########## Mensal - Participação ################################################
    #################################################################################
    df_mensal_part = df_mensal.copy()
    colunas = pd.Series(df_mensal_part.columns)
    cond1 = colunas.str.contains('Imp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_mensal_part[coluna] = (df_mensal_part[coluna] / df_mensal_part['Importações']) * 100
    colunas = pd.Series(df_mensal_part.columns)
    cond1 = colunas.str.contains('Exp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_mensal_part[coluna] = (df_mensal_part[coluna] / df_mensal_part['Exportações']) * 100
    df_mensal_part.drop(['Saldo Comercial','Corrente de Comércio'],axis=1,inplace=True)
    df_mensal_part.dropna(thresh=1, inplace=True)
    df_mensal_part['Exportações'] = 100
    df_mensal_part['Importações'] = 100
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Mensal - Participação'] = df_mensal_part
    #################################################################################
    ########## Acumulado no Ano - Participação ######################################
    #################################################################################
    df_acumAno_part = df_acumAno.copy()
    colunas = pd.Series(df_acumAno_part.columns)
    cond1 = colunas.str.contains('Imp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_acumAno_part[coluna] = (df_acumAno_part[coluna] / df_acumAno_part['Importações']) * 100
    colunas = pd.Series(df_acumAno_part.columns)
    cond1 = colunas.str.contains('Exp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_acumAno_part[coluna] = (df_acumAno_part[coluna] / df_acumAno_part['Exportações']) * 100
    df_acumAno_part.drop(['Saldo Comercial','Corrente de Comércio'],axis=1,inplace=True)
    df_acumAno_part.dropna(thresh=1, inplace=True)
    df_acumAno_part['Exportações'] = 100
    df_acumAno_part['Importações'] = 100
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado no Ano - Participação'] = df_acumAno_part
    #################################################################################
    ########## Acumulado em 12 meses - Participação #################################
    #################################################################################
    df_acum12m_part = df_acum12m.copy()
    colunas = pd.Series(df_acum12m_part.columns)
    cond1 = colunas.str.contains('Imp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_acum12m_part[coluna] = (df_acum12m_part[coluna] / df_acum12m_part['Importações']) * 100
    colunas = pd.Series(df_acum12m_part.columns)
    cond1 = colunas.str.contains('Exp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_acum12m_part[coluna] = (df_acum12m_part[coluna] / df_acum12m_part['Exportações']) * 100
    df_acum12m_part.drop(['Saldo Comercial','Corrente de Comércio'],axis=1,inplace=True)
    df_acum12m_part.dropna(thresh=1, inplace=True)
    df_acum12m_part['Exportações'] = 100
    df_acum12m_part['Importações'] = 100
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado em 12 meses - Participação'] = df_acum12m_part
    #################################################################################
    ########## Média de 12 meses - Participação #####################################
    #################################################################################
    df_media12m_part = df_media12m.copy()
    colunas = pd.Series(df_media12m_part.columns)
    cond1 = colunas.str.contains('Imp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_media12m_part[coluna] = (df_media12m_part[coluna] / df_media12m_part['Importações']) * 100
    colunas = pd.Series(df_media12m_part.columns)
    cond1 = colunas.str.contains('Exp\.')
    colunas = list(colunas[cond1])
    for coluna in colunas:
        df_media12m_part[coluna] = (df_media12m_part[coluna] / df_media12m_part['Exportações']) * 100
    df_media12m_part.drop(['Saldo Comercial','Corrente de Comércio'],axis=1,inplace=True)
    df_media12m_part.dropna(thresh=1, inplace=True)
    df_media12m_part['Exportações'] = 100
    df_media12m_part['Importações'] = 100
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Média de 12 meses - Participação'] = df_media12m_part
    #################################################################################
    ########## Mensal - Variação com relação ao ano anterior ########################
    #################################################################################
    df_mensal_var = df_mensal.copy()
    df_mensal_var_L12 = df_mensal_var.shift(periods=12)
    colunas = list(df_mensal_var.columns)
    for coluna in colunas:
        df_mensal_var[coluna] = ((df_mensal_var[coluna] - df_mensal_var_L12[coluna]) / df_mensal_var_L12[coluna]) * 100
    df_mensal_var.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_mensal_var.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Mensal - Variação com relação ao ano anterior'] = df_mensal_var
    #################################################################################
    ########## Acumulado no Ano - Variação com relação ao ano anterior ##############
    #################################################################################
    df_acumAno_var = df_acumAno.copy()
    df_acumAno_var_L12 = df_acumAno_var.shift(periods=12)
    colunas = list(df_acumAno_var.columns)
    for coluna in colunas:
        df_acumAno_var[coluna] = ((df_acumAno_var[coluna] - df_acumAno_var_L12[coluna]) / df_acumAno_var_L12[coluna]) * 100
    df_acumAno_var.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_acumAno_var.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado no Ano - Variação com relação ao ano anterior'] = df_acumAno_var
    #################################################################################
    ########## Acumulado em 12 meses - Variação com relação ao ano anterior #########
    #################################################################################
    df_acum12m_var = df_acum12m.copy()
    df_acum12m_var_L12 = df_acum12m_var.shift(periods=12)
    colunas = list(df_acum12m_var.columns)
    for coluna in colunas:
        df_acum12m_var[coluna] = ((df_acum12m_var[coluna] - df_acum12m_var_L12[coluna]) / df_acum12m_var_L12[coluna]) * 100
    df_acum12m_var.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_acum12m_var.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado em 12 meses - Variação com relação ao ano anterior'] = df_acum12m_var
    #################################################################################
    ########## Média de 12 meses - Variação com relação ao ano anterior #############
    #################################################################################
    df_media12m_var = df_media12m.copy()
    df_media12m_var_L12 = df_media12m_var.shift(periods=12)
    colunas = list(df_media12m_var.columns)
    for coluna in colunas:
        df_media12m_var[coluna] = ((df_media12m_var[coluna] - df_media12m_var_L12[coluna]) / df_media12m_var_L12[coluna]) * 100
    df_media12m_var.dropna(thresh=1, inplace=True)
    #     --->>>> Preenche NA com 0 <<<<< ---   #
    df_media12m_var.fillna(0, inplace=True)
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Média de 12 meses - Variação com relação ao ano anterior'] = df_media12m_var
    # *************************************************************************************************
    #     --->>>> Retorna o dicionário <<<<< ---   #
    return dicionário

######################################################################################################
######################################################################################################
######################################################################################################


tabMdicRJ = mdic_01d('RJ', anos=[2018,2019,2020], milhões=True)



######################################################################################################
######################################################################################################
######################################################################################################









