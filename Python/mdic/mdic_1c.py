# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:45:00 2020

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

##########################################################################################################
##########################################################################################################
##########################################################################################################


def g_expImp_ncms(país=False, uf=False):
    import glob
    import pandas as pd
    
    pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
    os.chdir(pasta)
    
    dicionário = {}
    
    cats = ['EXP', 'IMP']
    for cat in cats:
        busca = cat + '_????.csv'
        for index_arq, arq_nome in enumerate(glob.glob(busca)):
            print(arq_nome)
            ano = arq_nome[4:8]
    
            df = pd.read_csv(pasta / arq_nome,
                                   encoding = 'latin',
                                   delimiter = ';')
            

            if uf != False:
                cond1 = df['SG_UF_NCM'] == uf
            
            filtro = df.loc[cond1, :]
            soma_por_mês = filtro.groupby(['CO_MES'])['VL_FOB'].sum().to_frame()
            soma_por_mês.reset_index(inplace=True)
            soma_por_mês.rename(columns={'VL_FOB':uf, 'CO_MES':'month'}, inplace=True)
            soma_por_mês['year'] = ano
            soma_por_mês['day'] = 1
            soma_por_mês['mês'] = pd.to_datetime(soma_por_mês[['year', 'month', 'day']])
            soma_por_mês.drop(['year','month','day'],axis=1,inplace=True)
            soma_por_mês.set_index('mês', inplace=True)
                

        
            if index_arq == 0:
                df_ufs_anos = df_ufs.copy()
            else:
                df_ufs_anos = df_ufs_anos.append(df_ufs)
    
        dicionário[cat] = df_ufs_anos
    
    return dicionário

dic_expImp = g_expImp_ufs()

import pandas as pd
pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')
ncms = df['CO_NCM'].unique()













