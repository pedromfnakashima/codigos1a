# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:02:39 2020

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
    #anos = [2020, 2019]
    #tipo = 'EXP'
    #uf = 'RJ'
    for index_ano, ano in enumerate(anos):
        
        #tipo = 'EXP'
        #ano = 2020
        #uf = 'RJ'
        
        arq_nome = tipo + '_' + str(ano) + '.csv'
        
        pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
        df = pd.read_csv(pasta / arq_nome,
                         encoding = 'latin',
                         delimiter = ';')
        
        df.rename(columns={'CO_ANO':'year','CO_MES':'month'},inplace=True)
        df['day'] = 1
        df['dt'] = pd.to_datetime(df[['year', 'month', 'day']])
        
        df = df.groupby(['dt','CO_NCM','SG_UF_NCM','CO_PAIS'])['VL_FOB'].sum().to_frame().reset_index()
        
        df['dt_mês'] = df['dt'].dt.month
        df['dt_ano'] = df['dt'].dt.year
        
        cond1 = df['SG_UF_NCM'] == uf
        filtro = df.loc[cond1, :]
        
        if index_ano == 0:
            df_bruto = filtro.copy()
        else:
            df_bruto = df_bruto.append(filtro)
    
    df_bruto.index = range(len(df_bruto))
    return df_bruto

df_exp = mdic_01a(tipo='EXP',uf='RJ', anos=[2020, 2019])
df_imp = mdic_01a(tipo='IMP',uf='RJ', anos=[2020, 2019])

############################################################
dic_meses_pt={1:'Jan',2:'Fev',3:'Mar',4:'Abr',5:'Mai',6:'Jun',7:'Jul',8:'Ago',9:'Set',10:'Out',11:'Nov',12:'Dez'}
print(dic_meses_pt[9])


'''
CO_NCM
EXPORTAÇÕES
catsExp: planilha 7, coluna NO_FAT_AGREG
Básicos, 
IMPORTAÇÕES
catsImp: planilha 3, colunas NO_CGCE_N1 e NO_CGCE_N3
'''
############################################################
##################### TABELA GRANDE ########################
############################################################
pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
catsExp = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='7')
catsExp = catsExp[['CO_NCM','NO_FAT_AGREG']]
catsImp = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='3')
catsImp = catsImp[['CO_NCM','NO_CGCE_N1','NO_CGCE_N3']]

ref_mês = '2020-09-01'
ref_mês_dt = pd.to_datetime(ref_mês)
ref_mês_str = dic_meses_pt[ref_mês_dt.month] + str(ref_mês_dt.year)

tabelas_mdic = {}
tabelas_mdic[ref_mês_str] = pd.DataFrame(columns=['vl_Mês','vl_AcumAno','vl_Acum12Meses','p_Mês','p_AcumAno','p_Acum12Meses','vr_Mês','vr_AcumAno','vr_Acum12Meses'])

#print(len(tabelas_mdic[ref_mês_str].columns))

# --------------------- EXPORTAÇÕES -----------------------#
df_exp = mdic_01a(tipo='EXP',uf='RJ', anos=[2020, 2019])
df_exp = df_exp.merge(catsExp,how='left',left_on='CO_NCM',right_on='CO_NCM')
df_imp = mdic_01a(tipo='IMP',uf='RJ', anos=[2020, 2019])
df_imp = df_imp.merge(catsImp,how='left',left_on='CO_NCM',right_on='CO_NCM')

############################################################
####################### vl_Mês #############################
############################################################

# Delimita para o mês de referência
cond1 = df_exp['dt'] == ref_mês
df_exp = df_exp.loc[cond1,:]
cond1 = df_imp['dt'] == ref_mês
df_imp = df_imp.loc[cond1,:]

# Exportações - Totais
tot_exp = df_exp['VL_FOB'].sum() / 1_000_000
tabelas_mdic[ref_mês_str].loc['Exportações','vl_Mês'] = tot_exp

# Exportações - categorias: Básicos, Industrializados, Manufaturados, Semimanufaturados
df_exp_cats = df_exp.groupby(['NO_FAT_AGREG'])['VL_FOB'].sum().to_frame()
df_exp_cats.rename(mapper={'PRODUTOS BASICOS':'Exp. Básicos','PRODUTOS MANUFATURADOS':'Exp. Manufaturados','PRODUTOS SEMIMANUFATURADOS':'Exp. Semimanufaturados'},axis=0,inplace=True)
df_exp_cats.loc['Exp. Industrializados','VL_FOB'] = df_exp_cats.loc['Exp. Manufaturados','VL_FOB'] + df_exp_cats.loc['Exp. Semimanufaturados','VL_FOB']
df_exp_cats['VL_FOB'] = df_exp_cats['VL_FOB'] / 1_000_000
df_exp_cats.rename(mapper={'VL_FOB':'vl_Mês'},axis=1,inplace=True)
df_exp_cats = df_exp_cats.loc[['Exp. Básicos','Exp. Industrializados','Exp. Manufaturados','Exp. Semimanufaturados'],:]
tabelas_mdic[ref_mês_str] = tabelas_mdic[ref_mês_str].append(df_exp_cats)

# Importações - Totais
tot_imp = df_imp['VL_FOB'].sum() / 1_000_000
tabelas_mdic[ref_mês_str].loc['Importações','vl_Mês'] = tot_imp

# Exportações - categorias:
'''
Bens Intermediários
Bens de Capital
Combustíveis e lubrificantes
Bens de Consumo não-duráveis
Bens de Consumo duráveis
'''

'''
Alimentos e bebidas básicos, destinados principalmente ao consumo doméstico
Alimentos e bebidas elaborados, destinados principalmente ao consumo doméstico
Bens de consumo não duráveis
Bens de consumo semiduráveis
# ---------------------------------------------------------------------------
Automóveis para passageiros
Bens de consumo duráveis – exceto equipamentos de transportes
Equipamentos de transporte não industrial
'''
df_imp_cats_pequeno = df_imp.groupby(['NO_CGCE_N1'])['VL_FOB'].sum().to_frame()
df_imp_cats_pequeno['VL_FOB'] = df_imp_cats_pequeno['VL_FOB'] / 1_000_000
df_imp_cats_pequeno.loc['Imp. Bens Industriais','VL_FOB'] = df_imp_cats_pequeno.loc['BENS INTERMEDIÁRIOS (BI)','VL_FOB'] + df_imp_cats_pequeno.loc['BENS DE CAPITAL (BK)','VL_FOB']
df_imp_cats_pequeno = df_imp_cats_pequeno.loc[['Imp. Bens Industriais','BENS INTERMEDIÁRIOS (BI)','BENS DE CAPITAL (BK)','COMBUSTÍVEIS E LUBRIFICANTES']]
df_imp_cats_pequeno.rename(mapper={'BENS DE CAPITAL (BK)':'Imp. Bens de Capital','BENS INTERMEDIÁRIOS (BI)':'Imp. Bens Intermediários e matéria-prima','COMBUSTÍVEIS E LUBRIFICANTES':'Imp. Combustíveis e Lubrificantes'},axis=0,inplace=True)
df_imp_cats_pequeno.rename(mapper={'VL_FOB':'vl_Mês'},axis=1,inplace=True)
tabelas_mdic[ref_mês_str] = tabelas_mdic[ref_mês_str].append(df_imp_cats_pequeno)


df_imp_cats_grande = df_imp.groupby(['NO_CGCE_N1','NO_CGCE_N3'])['VL_FOB'].sum().to_frame()
df_imp_cats_grande['VL_FOB'] = df_imp_cats_grande['VL_FOB'] / 1_000_000
df_imp_cats_grande.reset_index(inplace=True)

# Bens de Consumo não-duráveis
cond1 = df_imp_cats_grande['NO_CGCE_N1'].str.contains('bc',case=False)
cond2 = df_imp_cats_grande['NO_CGCE_N3'].str.contains('alimentos',case=False)
cond3 = df_imp_cats_grande['NO_CGCE_N3'].str.contains('não duráveis',case=False)
cond4 = df_imp_cats_grande['NO_CGCE_N3'].str.contains('semiduráveis',case=False)
cond = cond1 & (cond2 | cond3 | cond4)
df_imp_cats_bcnd = df_imp_cats_grande.loc[cond,:]
soma_bcnd = df_imp_cats_bcnd['VL_FOB'].sum()

# Bens de Consumo duráveis
cond1 = df_imp_cats_grande['NO_CGCE_N1'].str.contains('bc',case=False)
cond2 = df_imp_cats_grande['NO_CGCE_N3'].str.contains('automóveis',case=False)
cond3 = df_imp_cats_grande['NO_CGCE_N3'].str.contains('consumo\sduráveis',case=False)
cond4 = df_imp_cats_grande['NO_CGCE_N3'].str.contains('Equipamentos',case=False)
cond = cond1 & (cond2 | cond3 | cond4)
df_imp_cats_bcd = df_imp_cats_grande.loc[cond,:]
soma_bcd = df_imp_cats_bcd['VL_FOB'].sum()

# Bens de Consumo
soma_bc = soma_bcnd + soma_bcd

# Não classificados
cond1 = df_imp_cats_grande['NO_CGCE_N1'].str.contains('não esp',case=False)
df_não_esp = df_imp_cats_grande.loc[cond1,'VL_FOB'].to_frame().reset_index()
df_não_esp.reset_index(inplace=True)
soma_não_esp = df_não_esp.loc[0,'VL_FOB']

tabelas_mdic[ref_mês_str].loc['Imp. Bens de Consumo','vl_Mês'] = soma_bc
tabelas_mdic[ref_mês_str].loc['Imp. Bens de Consumo não-duráveis','vl_Mês'] = soma_bcnd
tabelas_mdic[ref_mês_str].loc['Imp. Bens de Consumo duráveis','vl_Mês'] = soma_bcd
tabelas_mdic[ref_mês_str].loc['Imp. Não Classificados','vl_Mês'] = soma_não_esp
tabelas_mdic[ref_mês_str].loc['Saldo Comercial','vl_Mês'] = tabelas_mdic[ref_mês_str].loc['Exportações','vl_Mês'] - tabelas_mdic[ref_mês_str].loc['Importações','vl_Mês']
tabelas_mdic[ref_mês_str].loc['Corrente de Comércio','vl_Mês'] = tabelas_mdic[ref_mês_str].loc['Exportações','vl_Mês'] + tabelas_mdic[ref_mês_str].loc['Importações','vl_Mês']












