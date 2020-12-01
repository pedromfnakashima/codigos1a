# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:06:27 2020

@author: pedro
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

def mdic_01a(tipo, uf, anos):
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
        catsExp = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='7')
        catsExp = catsExp[['CO_NCM','NO_FAT_AGREG']]
        df_bruto = df_bruto.merge(catsExp,how='left',left_on='CO_NCM',right_on='CO_NCM')
    elif  tipo == 'IMP':
        pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
        catsImp = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='3')
        catsImp = catsImp[['CO_NCM','NO_CGCE_N1','NO_CGCE_N3']]
        df_bruto = df_bruto.merge(catsImp,how='left',left_on='CO_NCM',right_on='CO_NCM')
    return df_bruto

def mdic_01b(uf, anos, milhões=False):
    dicionário = {}
    # /\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\//\ Valor /\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/
    ##################################################################################################
    ########## Mensal - Valor ########################################################################
    ##################################################################################################
    df_exp = mdic_01a(tipo='EXP',uf=uf, anos=anos)
    df_imp = mdic_01a(tipo='IMP',uf=uf, anos=anos)
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
    ##################################################################################################
    ########## Acumulado no Ano - Valor ##############################################################
    ##################################################################################################
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
    ##################################################################################################
    ########## Acumulado em 12 meses - Valor #########################################################
    ##################################################################################################
    df_acum12m = df_mensal.copy()
    colunas = list(df_acum12m.columns)
    for coluna in colunas:
        df_acum12m[coluna] = df_acum12m[coluna].rolling(12).sum()
    df_acum12m.dropna(thresh=1, inplace=True)
    #     --->>>> Muda a frequência do index para MS <<<<< ---   #
    df_acum12m.index.freq = 'MS'
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Acumulado em 12 meses - Valor'] = df_acum12m
    ##################################################################################################
    ########## Média Móvel de 12 meses - Valor #######################################################
    ##################################################################################################
    df_media12m = df_mensal.copy()
    colunas = list(df_media12m.columns)
    for coluna in colunas:
        df_media12m[coluna] = df_media12m[coluna].rolling(12).mean()
    df_media12m.dropna(thresh=1, inplace=True)
    #     --->>>> Muda a frequência do index para MS <<<<< ---   #
    df_media12m.index.freq = 'MS'
    #     --->>>> Coloca no dicionário <<<<< ---   #
    dicionário['Média Móvel de 12 meses - Valor'] = df_media12m
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Entradas do dicionário até aqui \/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    l_variaveis = pd.Series(['Mensal - Valor','Acumulado no Ano - Valor','Acumulado em 12 meses - Valor','Média Móvel de 12 meses - Valor'])

    
    # /\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\//\ Participação /\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/
    # /\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Participação')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        df_part = dicionário[l_variavel].copy()
        # Importações
        colunas = pd.Series(dicionário[l_variavel].columns)
        cond1 = colunas.str.contains('Imp\.')
        colunas = list(colunas[cond1])
        for coluna in colunas:
            df_part[coluna] = (df_part[coluna] / df_part['Importações']) * 100
        # Exportações
        colunas = pd.Series(dicionário[l_variavel].columns)
        cond1 = colunas.str.contains('Exp\.')
        colunas = list(colunas[cond1])
        for coluna in colunas:
            df_part[coluna] = (df_part[coluna] / df_part['Exportações']) * 100
        # Deleta colunas inúteis do DF
        df_part.drop(['Saldo Comercial','Corrente de Comércio'],axis=1,inplace=True)
        df_part.dropna(thresh=1, inplace=True)
        df_part['Exportações'] = 100
        df_part['Importações'] = 100
        #     --->>>> Coloca no dicionário <<<<< ---   #
        dicionário[novo_nome] = df_part
    
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao ano anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varB = dicionário[l_variavel].copy()
        df_varB_L12 = df_varB.shift(periods=12)
        colunas = list(df_varB.columns)
        
        for coluna in colunas:
            df_varB[coluna] = df_varB[coluna] - df_varB_L12[coluna]
        df_varB.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varB.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário <<<<< ---   #
        dicionário[novo_nome] = df_varB
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao ano anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao ano anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varP = dicionário[l_variavel].copy()
        df_varP_L12 = df_varP.shift(periods=12)
        colunas = list(df_varP.columns)
        
        for coluna in colunas:
            df_varP[coluna] = ((df_varP[coluna] - df_varP_L12[coluna]) / df_varP_L12[coluna]) * 100
        df_varP.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varP.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário <<<<< ---   #
        dicionário[novo_nome] = df_varP
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Bruta com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Bruta com relação ao mês anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varB = dicionário[l_variavel].copy()
        df_varB_L1 = df_varB.shift(periods=1)
        colunas = list(df_varB.columns)
        
        for coluna in colunas:
            df_varB[coluna] = df_varB[coluna] - df_varB_L1[coluna]
        df_varB.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varB.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário <<<<< ---   #
        dicionário[novo_nome] = df_varB
    
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/ Variação Percentual com relação ao mês anterior /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
    novos_nomes = l_variaveis.str.replace('- Valor','- Variação Percentual com relação ao mês anterior')
    
    for l_variavel, novo_nome in zip(l_variaveis, novos_nomes):
        
        df_varP = dicionário[l_variavel].copy()
        df_varP_L1 = df_varP.shift(periods=1)
        colunas = list(df_varP.columns)
        
        for coluna in colunas:
            df_varP[coluna] = ((df_varP[coluna] - df_varP_L1[coluna]) / df_varP_L1[coluna]) * 100
        df_varP.dropna(thresh=1, inplace=True)
        #     --->>>> Preenche NA com 0 <<<<< ---   #
        df_varP.fillna(0, inplace=True)
        #     --->>>> Coloca no dicionário <<<<< ---   #
        dicionário[novo_nome] = df_varP
    
    # *************************************************************************************************
    #     --->>>> Retorna o dicionário <<<<< ---   #
    return dicionário

######################################################################################################
######################################################################################################
######################################################################################################

tabMdicMS = mdic_01b('MS', anos=[2018,2019,2020], milhões=True)

tabMdicRJ = mdic_01b('RJ', anos=[2018,2019,2020], milhões=True)

tabMdicSP = mdic_01b('SP', anos=[2018,2019,2020], milhões=True)

tabMdicBR = mdic_01b('BR', anos=[2018,2019,2020], milhões=True)

######################################################################################################
######################################################################################################
######################################################################################################




























df_mensal = tabMdicSP['Mensal - Valor'].copy()

df_mensal.fillna(0, inplace=True)










df_acum12m = tabMdicMS['Mensal - Valor'].copy()
colunas = list(df_acum12m.columns)
for coluna in colunas:
    print(coluna)
    df_acum12m[coluna] = df_acum12m[coluna].rolling(12).sum()


df_acum12m.dropna(thresh=1, inplace=True)
#     --->>>> Muda a frequência do index para MS <<<<< ---   #
df_acum12m.index.freq = 'MS'
#     --->>>> Coloca no dicionário <<<<< ---   #
dicionário['Acumulado em 12 meses - Valor'] = df_acum12m







tabMdic_cp = tabMdic['Mensal - Valor'].copy()
tabMdic_cp_L12 = tabMdic_cp.shift(periods=12)
colunas = list(tabMdic_cp.columns)
for coluna in colunas:
    print(coluna)
    tabMdic_cp[coluna] = ((tabMdic_cp[coluna] - tabMdic_cp_L12[coluna]) / tabMdic_cp_L12[coluna]) * 100
tabMdic_cp.dropna(inplace=True)


df.shift(periods=3)


print(tabMdic_cp.index)

colunas = list(tabMdic_cp.columns)
for coluna in colunas:
    tabMdic_cp[coluna] = tabMdic_cp[coluna].rolling(12).sum()

















tabMdic_cp = tabMdic['Acumulado em 12 meses - Participação'].copy()
tabMdic_cp.drop(['Exportações','Importações'],axis=1,inplace=True)
tabMdic_cp.dropna(inplace=True)


tabMdic_cp = tabMdic['Valor Mensal'].copy() / 1_000_000

colunas = pd.Series(tabMdic_cp.columns)
cond1 = colunas.str.contains('Imp\.')
colunas = list(colunas[cond1])
for coluna in colunas:
    print(coluna)
    tabMdic_cp[coluna] = (tabMdic_cp[coluna] / tabMdic_cp['Importações']) * 100

colunas = pd.Series(tabMdic_cp.columns)
cond1 = colunas.str.contains('Exp\.')
colunas = list(colunas[cond1])
for coluna in colunas:
    print(coluna)
    tabMdic_cp[coluna] = (tabMdic_cp[coluna] / tabMdic_cp['Exportações']) * 100
    

['Saldo Comercial','Corrente de Comércio']

str1 = 'abc'
print('d' in str1)




del bool




tabMdic_cp = tabMdic['Valor Mensal'].copy() / 1_000_000
colunas = list(tabMdic_cp.columns)
for coluna in colunas:
    tabMdic_cp[coluna] = tabMdic_cp[coluna].rolling(12).sum()



tabMdic_cp = tabMdic['Valor Mensal'].copy() / 1_000_000
tabMdic_cp['dt_ano'] = bcnd.index.year
colunas = list(set(list(tabMdic_cp.columns)) - {'dt_ano'})
for coluna in colunas:
    print(coluna)
    tabMdic_cp[coluna] = tabMdic_cp.groupby(['dt_ano'])[coluna].cumsum()
tabMdic_cp.drop(['dt_ano'],axis=1,inplace=True)










tabMdic_cp = tabMdic_cp.groupby(['dt_ano'])['Imp. Bens de Consumo não-duráveis'].cumsum()


bcnd = tabMdic_cp['Imp. Bens de Consumo não-duráveis'].to_frame()
bcnd['dt_ano'] = bcnd.index.year

bcnd['cumsum'] = bcnd.groupby(['dt_ano'])['Imp. Bens de Consumo não-duráveis'].cumsum()



print(tabMdic_cp.columns)



pasta = caminho_base / 'Dados' / 'alems' / 'Boletim de conjuntura'
with pd.ExcelWriter(pasta / 'Dados_01a.xlsx', mode='a', engine="openpyxl") as writer:  
    bcnd.to_excel(writer, sheet_name='planTeste1', index=True)





