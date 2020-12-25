# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 08:30:03 2020

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

#import numpy as np
import pandas as pd

#################################################################################################
################################# DOWNLOAD DOS ARQUIVOS #########################################
#################################################################################################
'''
Períodos e tabelas
2938: julho/2006 até dezembro/2011 (link: https://sidra.ibge.gov.br/Tabela/2938)
1419: janeiro/2012 até dezembro/2019 (link: https://sidra.ibge.gov.br/tabela/1419)
7060: a partir de janeiro/2020 (link: https://sidra.ibge.gov.br/tabela/7060)
'''
##########################################################################################################
##################################### Importa dados #####################################
##########################################################################################################

def junta_arqs(arqs_csv, pasta):
    import pandas as pd
    for index_arq, arq_nome in enumerate(arqs_csv):
        
        # arq_nome = "t7060.csv"
        print(arq_nome)
    
        df = pd.read_csv(pasta / arq_nome,
                                      delimiter = '|',
                                      decimal=',',
                                      dtype='str',
                                      parse_dates=['dt'])
        if index_arq == 0:
            df2 = df.copy()
        else:
            df2 = df2.append(df)
    
                # Converte para numérico
    df2['V'] = pd.to_numeric(df2['V'], errors='coerce')
    return df2

arqs_csv = ['t2938.csv','t1419.csv','t7060.csv']
pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'


df1 = junta_arqs(arqs_csv=arqs_csv, pasta=pasta)

df = df1.copy()
# li_datas = pd.DatetimeIndex(df['dt'].unique())
# df_datas = pd.DataFrame({'dt':li_datas})
# df_datas.set_index('dt',inplace=True)
# del li_datas
print(df1.dtypes)
##########################################################################################################
################################# Importa categorias IBGE ######################################
##########################################################################################################

cond1 = df['D1C'] == '1'
filtro1 = df.copy().loc[cond1,['dt','códIBGE','D2N','C_NC_M','D_SD_ND_M_S','V']]

filtro1.sort_values(by=['dt','códIBGE','D2N'],ascending=[True,True,False],inplace=True)

cond1 = filtro1['D2N'].str.contains('Variação',case=False)
filtro2 = filtro1.copy().loc[cond1,['dt','códIBGE','C_NC_M','D_SD_ND_M_S','V']]
df_variação = filtro2.copy()
df_variação.set_index(['dt','códIBGE'],inplace=True)
df_variação.rename(mapper={'V':'Variação'},axis=1,inplace=True)

cond1 = filtro1['D2N'].str.contains('Peso',case=False)
filtro2 = filtro1.copy().loc[cond1,['dt','códIBGE','V']]
df_peso = filtro2.copy()
df_peso.set_index(['dt','códIBGE'],inplace=True)
df_peso.rename(mapper={'V':'Peso'},axis=1,inplace=True)

df_varPes = df_variação.merge(df_peso,how='left',left_index=True,right_index=True)
df_varPes['Contribuição'] = df_varPes['Variação'] * df_varPes['Peso']


# seleção1 = df_varPes.loc['2011-12-01']
# seleção2 = df_varPes.loc[('2011-12-01','1'), :]
# seleção3 = df_varPes.loc[('2011-12-01','1'), ('Contribuição')]
# seleção4 = df_varPes.loc[(['2011-12-01','2012-01-01'],'1'), ('Contribuição')]
# seleção5 = df_varPes.loc[('2011-12-01',['1','2']), ('Contribuição')]
# seleção6 = df_varPes.loc[(slice(None),['1','2']), ('Contribuição')]
# seleção7 = df_varPes.loc[(['2011-12-01','2012-01-01'],slice(None)), ('Contribuição')]
# del seleção1, seleção2, seleção3, seleção4, seleção5, seleção6, seleção7 
# seleção1 = df_varPes.loc[('2011-12-01',['1','2']), ('Contribuição')]


df_varPes.reset_index(inplace=True)

df_varPes_agregC_NC_M = df_varPes.groupby(['dt','C_NC_M'])['Peso'].sum().to_frame()
seleção1 = df_varPes_agregC_NC_M.loc[('2011-12-01',['C','NC']), ('Peso')].to_frame()

df_varPes_agregC_NC_M = df_varPes.groupby(['dt','C_NC_M'])['Contribuição'].sum().to_frame()
seleção2 = df_varPes_agregC_NC_M.loc[('2011-12-01',['C','NC']), ('Contribuição')].to_frame()

seleção12 = seleção1.merge(seleção2,how='left',left_index=True,right_index=True)
seleção12['cont_planilha'] = seleção12['Contribuição'] /seleção12['Peso']

print(df_varPes.dtypes)













