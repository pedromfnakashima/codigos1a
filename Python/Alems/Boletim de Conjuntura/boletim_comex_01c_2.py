# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:30:57 2020

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

df_exp = mdic_01a(tipo='EXP',uf='MS', anos=[2019,2020])
df_imp = mdic_01a(tipo='IMP',uf='MS', anos=[2019,2020])

# EXPORTAÇÕES TOTAIS MENSAIS
soma = df_exp.groupby(['dt'])['VL_FOB'].sum().to_frame()
soma.rename(mapper={'VL_FOB':'Exportações'},axis=1,inplace=True)
df_final = soma.copy()

# IMPORTAÇÕES TOTAIS MENSAIS
soma = df_imp.groupby(['dt'])['VL_FOB'].sum().to_frame()
soma.rename(mapper={'VL_FOB':'Importações'},axis=1,inplace=True)
df_final = df_final.merge(soma,how='left',left_index=True,right_index=True)

# EXPORTAÇÕES: BÁSICOS, MANUFATURADOS, SEMIFATURADOS E INDUSTRIALIZADOS
soma = df_exp.groupby(['dt','NO_FAT_AGREG'])['VL_FOB'].sum().to_frame().reset_index()
# Exp. Básicos
cond1 = soma['NO_FAT_AGREG'].str.contains('basicos',case=False)
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.set_index('dt',inplace=True)
filtro.rename(mapper={'VL_FOB':'Exp. Básicos'},axis=1,inplace=True)
df_final = df_final.merge(filtro,how='left',left_index=True,right_index=True)
# Exp. Manufaturados
cond1 = soma['NO_FAT_AGREG'].str.contains('\smanufaturados',case=False)
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.set_index('dt',inplace=True)
filtro.rename(mapper={'VL_FOB':'Exp. Manufaturados'},axis=1,inplace=True)
df_final = df_final.merge(filtro,how='left',left_index=True,right_index=True)
# Exp. Semimanufaturados
cond1 = soma['NO_FAT_AGREG'].str.contains('\ssemimanufaturados',case=False)
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.set_index('dt',inplace=True)
filtro.rename(mapper={'VL_FOB':'Exp. Semimanufaturados'},axis=1,inplace=True)
df_final = df_final.merge(filtro,how='left',left_index=True,right_index=True)
# Exp. Industrializados
df_final['Exp. Industrializados'] = df_final['Exp. Manufaturados'] + df_final['Exp. Semimanufaturados']
# IMPORTAÇÕES: BENS INDUSTRIAIS, BENS INTERMEDIÁRIOS, BENS DE CAPITAL, COMBUSTÍVEIS E LUBRIFICANTES, BENS DE CONSUMO DURÁVEIS E NÃO DURÁVEIS, NÃO CLASSIFICADOS
soma = df_imp.groupby(['dt','NO_CGCE_N1'])['VL_FOB'].sum().to_frame().reset_index()
# Imp. Bens Intermediários
cond1 = soma['NO_CGCE_N1'].str.contains('\sintermediários',case=False)
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.set_index('dt',inplace=True)
filtro.rename(mapper={'VL_FOB':'Imp. Bens Intermediários'},axis=1,inplace=True)
df_final = df_final.merge(filtro,how='left',left_index=True,right_index=True)
# Imp. Bens de Capital
cond1 = soma['NO_CGCE_N1'].str.contains('\scapital',case=False)
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.set_index('dt',inplace=True)
filtro.rename(mapper={'VL_FOB':'Imp. Bens de Capital'},axis=1,inplace=True)
df_final = df_final.merge(filtro,how='left',left_index=True,right_index=True)
# Imp. Bens Industriais
df_final['Imp. Bens Industriais'] = df_final['Imp. Bens Intermediários'] + df_final['Imp. Bens de Capital']
# Imp. Combustíveis e Lubrificantes
cond1 = soma['NO_CGCE_N1'].str.contains('^combustíveis',case=False)
filtro = soma.loc[cond1,['dt','VL_FOB']]
filtro.set_index('dt',inplace=True)
filtro.rename(mapper={'VL_FOB':'Imp. Combustíveis e Lubrificantes'},axis=1,inplace=True)
df_final = df_final.merge(filtro,how='left',left_index=True,right_index=True)
# Imp. Bens de Consumo não-duráveis
cond1 = df_imp['NO_CGCE_N1'].str.contains('bc',case=False)
cond2 = df_imp['NO_CGCE_N3'].str.contains('alimentos',case=False)
cond3 = df_imp['NO_CGCE_N3'].str.contains('não\sduráveis',case=False)
cond4 = df_imp['NO_CGCE_N3'].str.contains('semiduráveis',case=False)
cond = cond1 & (cond2 | cond3 | cond4)
filtro = df_imp.loc[cond,:]
soma = filtro.groupby(['dt'])['VL_FOB'].sum().to_frame()
soma.rename(mapper={'VL_FOB':'Imp. Bens de Consumo não-duráveis'},axis=1,inplace=True)
df_final = df_final.merge(soma,how='left',left_index=True,right_index=True)
# Imp. Bens de Consumo duráveis
cond1 = df_imp['NO_CGCE_N1'].str.contains('bc',case=False)
cond2 = df_imp['NO_CGCE_N3'].str.contains('automóveis',case=False)
cond3 = df_imp['NO_CGCE_N3'].str.contains('consumo\sduráveis',case=False)
cond4 = df_imp['NO_CGCE_N3'].str.contains('Equipamentos',case=False)
cond = cond1 & (cond2 | cond3 | cond4)
filtro = df_imp.loc[cond,:]
soma = filtro.groupby(['dt'])['VL_FOB'].sum().to_frame()
soma.rename(mapper={'VL_FOB':'Imp. Bens de Consumo duráveis'},axis=1,inplace=True)
df_final = df_final.merge(soma,how='left',left_index=True,right_index=True)



# Imp. Bens de Consumo
df_final['Imp. Bens de Consumo'] = df_final['Imp. Bens de Consumo não-duráveis'] + df_final['Imp. Bens de Consumo duráveis']
# Imp. Não Classificados
cond1 = df_imp['NO_CGCE_N1'].str.contains('não esp',case=False)
filtro = df_imp.loc[cond1,:]
soma = filtro.groupby(['dt'])['VL_FOB'].sum().to_frame()
soma.rename(mapper={'VL_FOB':'Imp. Não Classificados'},axis=1,inplace=True)
df_final = df_final.merge(soma,how='left',left_index=True,right_index=True)
# SALDO COMERCIAL
df_final['Saldo Comercial'] = df_final['Exportações'] - df_final['Importações']
# CORRENTE DE COMÉRCIO
df_final['Corrente de Comércio'] = df_final['Exportações'] + df_final['Importações']




print(f'{df_final.loc["2020-09-01","Saldo Comercial"]:,.2f}\n')
print(f'{df_final.loc["2020-09-01","Corrente de Comércio"]:,.2f}\n')


print(f'{soma.loc["2020-09-01","VL_FOB"]:,.2f}\n')





soma_bcnd = df_imp_cats_bcnd['VL_FOB'].sum()




soma = df_imp.groupby(['dt','NO_CGCE_N1','NO_CGCE_N3'])['VL_FOB'].sum().to_frame().reset_index()



filtro = soma.loc[cond1,['dt','VL_FOB','NO_CGCE_N1']]


















