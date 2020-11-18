# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:56:13 2020

@author: pedro

https://fiesc.com.br/pt-br/imprensa/exportacoes-de-outubro-tem-queda-de-97

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

pasta = caminho_base / 'Dados' / 'mdic'
df_ncm = pd.read_csv(pasta / 'NCM.csv',
                       encoding = 'latin',
                       delimiter = ';')
df_ncm = df_ncm.loc[:, ['CO_NCM','NO_NCM_POR']]

pasta = caminho_base / 'Dados' / 'mdic'
df_pais = pd.read_csv(pasta / 'PAIS.csv',
                       encoding = 'latin',
                       delimiter = ';')
df_pais = df_pais.loc[:, ['CO_PAIS','NO_PAIS']]



# --------------------------------------------------------------------------------------------

cond1 = df_ncm['NO_NCM_POR'].str.contains('suí')
filtro = df_ncm.loc[cond1,:]


# --------------------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')

cond1 = df['CO_MES'] == 10
cond2 = df['SG_UF_NCM'] == 'SC'
filtro = df.loc[cond1 & cond2, ['CO_NCM','VL_FOB']]

soma_por_ncm = filtro.groupby(['CO_NCM'])['VL_FOB'].sum().to_frame()
soma_por_ncm.reset_index(inplace=True)
soma_por_ncm.sort_values(by=['VL_FOB'], ascending=[False], inplace=True)

soma_por_ncm = soma_por_ncm.merge(df_ncm, how='left', left_on='CO_NCM', right_on='CO_NCM')

suíno_2020 = soma_por_ncm.loc[0,'VL_FOB']
# --------------------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2019.csv',
                       encoding = 'latin',
                       delimiter = ';')

cond1 = df['CO_MES'] == 10
cond2 = df['SG_UF_NCM'] == 'SC'
filtro = df.loc[cond1 & cond2, ['CO_NCM','VL_FOB']]

soma_por_ncm = filtro.groupby(['CO_NCM'])['VL_FOB'].sum().to_frame()
soma_por_ncm.reset_index(inplace=True)
soma_por_ncm.sort_values(by=['VL_FOB'], ascending=[False], inplace=True)

soma_por_ncm = soma_por_ncm.merge(df_ncm, how='left', left_on='CO_NCM', right_on='CO_NCM')

suíno_2019 = soma_por_ncm.loc[1,'VL_FOB']

# --------------------------------------------------------------------------------------------
variação = ((suíno_2020 - suíno_2019)/suíno_2019)*100

# --------------------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')

cond1 = df['CO_MES'] == 10
cond2 = df['SG_UF_NCM'] == 'SC'
filtro = df.loc[cond1 & cond2, ['CO_NCM','VL_FOB', 'CO_PAIS']]

soma_por_pais = filtro.groupby(['CO_PAIS'])['VL_FOB'].sum().to_frame()
soma_por_pais.reset_index(inplace=True)
soma_por_pais.sort_values(by=['VL_FOB'], ascending=[False], inplace=True)

soma_por_pais = soma_por_pais.merge(df_pais, how='left', left_on='CO_PAIS', right_on='CO_PAIS')

valor = 112_286_035

suíno_2020 = soma_por_ncm.loc[0,'VL_FOB']


# --------------------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')

cond1 = df['CO_MES'] == 10
cond2 = df['SG_UF_NCM'] == 'MS'
filtro = df.loc[cond1 & cond2, ['CO_NCM','VL_FOB', 'CO_PAIS']]

soma_por_pais = filtro.groupby(['CO_PAIS'])['VL_FOB'].sum().to_frame()
soma_por_pais.reset_index(inplace=True)
soma_por_pais.sort_values(by=['VL_FOB'], ascending=[False], inplace=True)

soma_por_pais = soma_por_pais.merge(df_pais, how='left', left_on='CO_PAIS', right_on='CO_PAIS')






# --------------------------------------------------------------------------------------------


pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')


cond1 = df['CO_MES'] == 9
cond2 = df['SG_UF_NCM'] == 'MS'
filtro = df.loc[cond1 & cond2, ['CO_NCM','VL_FOB']]


cond2 = df['SG_UF_NCM'] == 'SC'
filtro = df.loc[cond2, ['CO_NCM','VL_FOB']]

print(filtro['VL_FOB'].sum())


valor = 6_764_268_430

cond1 = df['CO_MES'] == out
cond2 = df['SG_UF_NCM'] == 'MS'
filtro = df.loc[cond1 & cond2, ['CO_NCM','VL_FOB']]


pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')










filtro_ncm = df.loc[cond1 & cond2, ['CO_NCM']].duplicated(keep='first')

print(filtro_ncm.sum())





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











