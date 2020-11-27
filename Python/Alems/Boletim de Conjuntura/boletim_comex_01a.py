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

df_exp_soma = df_exp.groupby(['year','month'])['VL_FOB'].sum()
df_imp_soma = df_imp.groupby(['year','month'])['VL_FOB'].sum()

soma_exp_set2020 = df_exp_soma[2020,9]
soma_imp_set2020 = df_imp_soma[2020,9]
tot_set2020 = soma_exp_set2020 + soma_imp_set2020
print(f'\nCorrente de comércio em set/2020:')
print(f'{tot_set2020:,}\n')
print(f'Exportações set/2020:')
print(f'{soma_exp_set2020:,.2f}\n')
print(f'Importações set/2020:')
print(f'{soma_imp_set2020:,.2f}\n')

soma_exp_set2019 = df_exp_soma[2019,9]
soma_imp_set2019 = df_imp_soma[2019,9]
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

df_exp_soma = df_exp_soma.to_frame().reset_index()
df_imp_soma = df_imp_soma.to_frame().reset_index()

cond1 = df_exp_soma['month'] <= 9
df_exp_soma = df_exp_soma.loc[cond1, :]
cond1 = df_imp_soma['month'] <= 9
df_imp_soma = df_imp_soma.loc[cond1, :]

df_exp_soma_anos = df_exp_soma.groupby(['year'])['VL_FOB'].sum()
df_imp_soma_anos = df_imp_soma.groupby(['year'])['VL_FOB'].sum()

print(f'\nConta corrente acumulada 2020:')
soma2020 = df_exp_soma_anos[2020]+df_imp_soma_anos[2020]
print(f'{soma2020:,.2f}\n')

print(f'Conta corrente acumulada 2019:')
soma2019 = df_exp_soma_anos[2019]+df_imp_soma_anos[2019]
print(f'{soma2019:,.2f}\n')

print(f'Variação 2019-2020:')
variacaoB = soma2020-soma2019
variacaoP = (variacaoB/soma2019)*100
print(f'{variacao:,.2f} %\n')

print(f'\nExportações 2020:')
print(f'{df_exp_soma_anos[2020]:,.2f}\n')
print(f'Exportações 2019:')
print(f'{df_exp_soma_anos[2019]:,.2f}\n')
variacaoB = df_exp_soma_anos[2020]-df_exp_soma_anos[2019]
variacaoP = (variacaoB/df_exp_soma_anos[2019])*100
print(f'Variação Percentual:')
print(f'{variacaoP:,.2f} %\n')
print(f'Variação Bruta:')
print(f'{variacaoB:,.2f}\n')

print(f'\nImportações 2020:')
print(f'{df_imp_soma_anos[2020]:,.2f}\n')
print(f'Importações 2019:')
print(f'{df_imp_soma_anos[2019]:,.2f}\n')
variacaoB = df_imp_soma_anos[2020]-df_imp_soma_anos[2019]
variacaoP = (variacaoB/df_exp_soma_anos[2019])*100
print(f'Variação Percentual:')
print(f'{variacaoP:,.2f} %\n')
print(f'Variação Bruta:')
print(f'{variacaoB:,.2f}\n')

saldocomercial = df_exp_soma_anos[2020]-df_imp_soma_anos[2020]
print(f'Saldo comercial 2020:')
print(f'{saldocomercial:,.2f}\n')


df_exp_soma_anos = df_exp_soma[2020,9]
df_imp_soma_anos = df_imp_soma[2020,9]



print(f'{:,.2f}\n')

#corrente_2019 = df_exp_soma[2019] + df_imp_soma[2019]
#corrente_2020 = df_exp_soma[2020] + df_imp_soma[2020]
























