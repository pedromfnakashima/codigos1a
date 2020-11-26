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

soma_exp_set = df_exp_soma[2020,9]
soma_imp_set = df_imp_soma[2020,9]
tot_set = soma_exp_set + soma_imp_set
print(f'{tot_set:,}')

#corrente_2019 = df_exp_soma[2019] + df_imp_soma[2019]
#corrente_2020 = df_exp_soma[2020] + df_imp_soma[2020]
























