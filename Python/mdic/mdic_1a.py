# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:56:13 2020

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
##########################################################################################################
##########################################################################################################
##########################################################################################################










import pandas as pd

pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')


cond1 = df['CO_MES'] == 9
cond2 = df['SG_UF_NCM'] == 'RJ'
filtro = df.loc[cond1 & cond2, :]









caminho = caminho_base / 'Dados' / 'mdic' / 'IMP_COMPLETA.zip'
df = pd.read_csv(caminho, compression='zip', header=0, sep=';', decimal=',',  encoding = 'latin')


somas_ano = df.groupby(['CO_ANO'])['VL_FOB'].sum()







pasta = caminho_base / 'Dados' / 'mdic'
mdic_imp = pd.read_csv(pasta / 'IMP_COMPLETA.csv',
                       encoding = 'latin',
                       delimiter = ';')

somas_ano = mdic_imp.groupby(['CO_ANO'])['VL_FOB'].sum()


somas_desag = mdic_imp.groupby(['CO_ANO', 'CO_MES', 'CO_NCM', 'CO_PAIS', 'SG_UF_NCM'])['VL_FOB'].sum()


ano = 2017
print(f'\nSoma importações de {ano}: {somas_desag[ano].sum():,.0f}')





s_soma_votos = df_tse_1.groupby(['NM_URNA_CANDIDATO','NM_MUNICIPIO'])['QT_VOTOS_NOMINAIS'].sum()

print(mdic_imp.head())

novo <- df_ncm %>%
  group_by(CO_ANO, CO_MES, CO_NCM, CO_PAIS, SG_UF_NCM) %>%
  summarise(VL_FOB = sum(VL_FOB)) %>%
  arrange(CO_ANO, CO_MES, CO_NCM) # <- Funcionando











