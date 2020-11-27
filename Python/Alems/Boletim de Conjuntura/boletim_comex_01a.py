# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:16:56 2020

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
import pandas as pd
##########################################################################################################
##########################################################################################################
##########################################################################################################

def g_texto():
    mês = 'setembro'
    ano_atual = 2020
    ano_anterior = ano_atual - 1
    correnteCom_bi = 34.3
    estado = 'Rio de Janeiro'
    aumentoRecuo = 'recuo'
    percentual = 54
    
    texto = f"Em {mês} de {ano_atual}, o Estado de {estado} somou\
    US$ {correnteCom_bi} bilhões em corrente de comércio, um \
    {aumentoRecuo} de {percentual}% quando comparado ao mesmo \
    mês de {ano_anterior}"
    
    return texto

texto = g_texto()
print(texto)

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
        df['mês'] = pd.to_datetime(df[['year', 'month', 'day']])
        df.drop(['day'],axis=1,inplace=True)
        
        cond1 = df['SG_UF_NCM'] == uf
        filtro = df.loc[cond1, :]
        
        if index_ano == 0:
            df_bruto = filtro.copy()
        else:
            df_bruto = df_bruto.append(filtro)
    return df_bruto

df_exp = mdic_01a(tipo='EXP',uf='RJ', anos=[2020, 2019])
df_imp = mdic_01a(tipo='IMP',uf='RJ', anos=[2020, 2019])

df_exp_somaMeses = df_exp.groupby(['year','month'])['VL_FOB'].sum()
df_imp_somaMeses = df_imp.groupby(['year','month'])['VL_FOB'].sum()

soma_exp_set2020 = df_exp_somaMeses[2020,9]
soma_imp_set2020 = df_imp_somaMeses[2020,9]
tot_set2020 = soma_exp_set2020 + soma_imp_set2020
print(f'\nCorrente de comércio em set/2020:')
print(f'{tot_set2020:,}\n')
print(f'Exportações set/2020:')
print(f'{soma_exp_set2020:,.2f}\n')
print(f'Importações set/2020:')
print(f'{soma_imp_set2020:,.2f}\n')

soma_exp_set2019 = df_exp_somaMeses[2019,9]
soma_imp_set2019 = df_imp_somaMeses[2019,9]
tot_set2019 = soma_exp_set2019 + soma_imp_set2019
print('=============================')

print(f'\nCorrente de comércio em set/2019:')
print(f'{tot_set2019:,}\n')
print(f'Exportações set/2020:')
print(f'{soma_exp_set2019:,.2f}\n')
print(f'Importações set/2020:')
print(f'{soma_imp_set2019:,.2f}\n')

print('=============================')

print('\nVariação das importações (set/2019-set/2020):')
print(f'{((soma_imp_set2020-soma_imp_set2019)/soma_imp_set2019)*100:,.2f} %\n')
print('Variação das exportações (set/2019-set/2020):')
print(f'{((soma_exp_set2020-soma_exp_set2019)/soma_exp_set2019)*100:,.2f} %\n')

print('=============================')

print('\nSaldo comercial set/2020:')
print(f'{soma_exp_set2020-soma_imp_set2020:,.2f}\n')
print('Saldo comercial set/2019:')
print(f'{soma_exp_set2019-soma_imp_set2019:,.2f}\n')

print('=============================')

df_exp_somaMeses = df_exp_somaMeses.to_frame().reset_index()
df_imp_somaMeses = df_imp_somaMeses.to_frame().reset_index()

cond1 = df_exp_somaMeses['month'] <= 9
df_exp_somaMeses = df_exp_somaMeses.loc[cond1, :]
cond1 = df_imp_somaMeses['month'] <= 9
df_imp_somaMeses = df_imp_somaMeses.loc[cond1, :]

df_exp_somaAnos = df_exp_somaMeses.groupby(['year'])['VL_FOB'].sum()
df_imp_somaAnos = df_imp_somaMeses.groupby(['year'])['VL_FOB'].sum()

print(f'\nConta corrente acumulada 2020:')
soma2020 = df_exp_somaAnos[2020]+df_imp_somaAnos[2020]
print(f'{soma2020:,.2f}\n')

print(f'Conta corrente acumulada 2019:')
soma2019 = df_exp_somaAnos[2019]+df_imp_somaAnos[2019]
print(f'{soma2019:,.2f}\n')

print(f'Variação 2019-2020:')
variacaoB = soma2020-soma2019
variacaoP = (variacaoB/soma2019)*100
print(f'{variacaoP:,.2f} %\n')

print(f'\nExportações 2020:')
print(f'{df_exp_somaAnos[2020]:,.2f}\n')
print(f'Exportações 2019:')
print(f'{df_exp_somaAnos[2019]:,.2f}\n')
variacaoB = df_exp_somaAnos[2020]-df_exp_somaAnos[2019]
variacaoP = (variacaoB/df_exp_somaAnos[2019])*100
print(f'Variação Percentual:')
print(f'{variacaoP:,.2f} %\n')
print(f'Variação Bruta:')
print(f'{variacaoB:,.2f}\n')

print(f'\nImportações 2020:')
print(f'{df_imp_somaAnos[2020]:,.2f}\n')
print(f'Importações 2019:')
print(f'{df_imp_somaAnos[2019]:,.2f}\n')
variacaoB = df_imp_somaAnos[2020]-df_imp_somaAnos[2019]
variacaoP = (variacaoB/df_exp_somaAnos[2019])*100
print(f'Variação Percentual:')
print(f'{variacaoP:,.2f} %\n')
print(f'Variação Bruta:')
print(f'{variacaoB:,.2f}\n')

saldocomercial = df_exp_somaAnos[2020]-df_imp_somaAnos[2020]
print(f'Saldo comercial 2020:')
print(f'{saldocomercial:,.2f}\n')

print('=============================')
print('=============================')
print('=============================')

pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
fatorAgregado = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='7')
print(fatorAgregado['NO_FAT_AGREG'].value_counts())
print(fatorAgregado['NO_FAT_AGREG_GP'].value_counts())

df_exp_fatorAgregado = df_exp.merge(fatorAgregado,how='left',left_on='CO_NCM',right_on='CO_NCM')

cond1 = df_exp_fatorAgregado['month'] <= 9
df_exp_fatorAgregado = df_exp_fatorAgregado.loc[cond1,:]

df_exp_fatorAgregado_fatAgregGP_somaAnos = df_exp_fatorAgregado.groupby(['year','NO_FAT_AGREG_GP'])['VL_FOB'].sum()
print(f'\nProdutos industrializados 2020:')
print(f'{df_exp_fatorAgregado_fatAgregGP_somaAnos[2020,"PRODUTOS INDUSTRIALIZADOS"]:,.2f}\n')

df_exp_fatorAgregado_fatAgreg_somaAnos = df_exp_fatorAgregado.groupby(['year','NO_FAT_AGREG'])['VL_FOB'].sum()
print(f'\nProdutos industrializados 2020:')
print(f'{df_exp_fatorAgregado_fatAgreg_somaAnos[2020,"PRODUTOS SEMIMANUFATURADOS"]:,.2f}\n')

cond1 = df_exp_fatorAgregado['NO_NCM_POR'].str.contains('máquinas')
filtro = df_exp_fatorAgregado.loc[cond1,:]

print('=============================')

pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
fatorAgregado = pd.read_csv(pasta/'NCM.csv')

ncmNomes = pd.read_csv(pasta / 'NCM.csv',
                       encoding = 'latin',
                       delimiter = ';')

ncmNomes = ncmNomes[['CO_NCM','NO_NCM_POR']]

cond1 = ncmNomes['NO_NCM_POR'].str.contains('coque')
filtro = ncmNomes.loc[cond1,:]

print('=============================')

pasta = caminho_base / 'Dados' / 'mdic' / 'Tabelas - classificações'
isic = pd.read_excel(pasta/'TABELAS_AUXILIARES.xlsx', sheet_name='4')

isic = isic[['CO_NCM', 'NO_ISIC_DIVISAO']]

df_exp_fatorAgregado_isic = df_exp_fatorAgregado.merge(isic,how='left',left_on='CO_NCM',right_on='CO_NCM')

print(df_exp_fatorAgregado_isic['month'].value_counts())

df_exp_fatorAgregado_isic_somaAnos = df_exp_fatorAgregado_isic.groupby(['year','NO_ISIC_DIVISAO'])['VL_FOB'].sum().to_frame().reset_index()

df_exp_fatorAgregado_isic_somaAnos.sort_values(by=['year','VL_FOB'], ascending=[False,False], inplace=True)

df_exp_fatorAgregado_isic_soma2019 = df_exp_fatorAgregado_isic_somaAnos.loc[df_exp_fatorAgregado_isic_somaAnos['year']==2019,:]
df_exp_fatorAgregado_isic_soma2020 = df_exp_fatorAgregado_isic_somaAnos.loc[df_exp_fatorAgregado_isic_somaAnos['year']==2020,:]
df_exp_fatorAgregado_isic_soma2019.rename(columns={'VL_FOB':'2019'},inplace=True)
df_exp_fatorAgregado_isic_soma2020.rename(columns={'VL_FOB':'2020'},inplace=True)

df_exp_fatorAgregado_isic_somaAnos2 = df_exp_fatorAgregado_isic_soma2019.merge(df_exp_fatorAgregado_isic_soma2020,how='left',left_on='NO_ISIC_DIVISAO',right_on='NO_ISIC_DIVISAO')

df_exp_fatorAgregado_isic_somaAnos2['variação'] = df_exp_fatorAgregado_isic_somaAnos2['2020'] - df_exp_fatorAgregado_isic_somaAnos2['2019']

df_exp_fatorAgregado_isic_somaAnos2.sort_values(by=['variação'], inplace=True)

df_exp_fatorAgregado_isic_somaAnos2['variaçãoP'] = (df_exp_fatorAgregado_isic_somaAnos2['variação'] / df_exp_fatorAgregado_isic_somaAnos2['2019'])*100

vl_coque = df_exp_fatorAgregado_isic_somaAnos2.loc[3,'variaçãoP']
vl_transp = df_exp_fatorAgregado_isic_somaAnos2.loc[2,'variaçãoP']

print(f'{vl_coque:,.2f}\n')
print(f'{vl_transp:,.2f}\n')


########################################################################
############################## IMPORTAÇÕES #############################
########################################################################









print(f'{:,.2f}\n')
print(f'{:,.2f}\n')







