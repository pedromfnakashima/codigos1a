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

'''
NCMs (CO_NCM):
Soja: 12019000
Celulose: 47032900
Carne desossada: 2023000
Açúcar de cana: 17011400
Milho em grão: 10059010
Gás natural: 27112100

Países (CO_PAIS):
China: 160
Argentina: 63
Paquistão: 576
Taiwan (Formosa): 161
Tailândia: 776
Estados Unidos: 249
Bolívia: 97
'''

import pandas as pd

pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
df = pd.read_csv(pasta / 'EXP_2020.csv',
                       encoding = 'latin',
                       delimiter = ';')

cond1 = df['SG_UF_NCM'] == 'MS'
filtro = df.loc[cond1, ['CO_NCM','VL_FOB']]
soma_por_ncm = filtro.groupby(['CO_NCM'])['VL_FOB'].sum().to_frame()
soma_por_ncm.reset_index(inplace=True)
soma_por_ncm.sort_values(by=['VL_FOB'], ascending=[False], inplace=True)
soma_por_ncm = soma_por_ncm.merge(df_ncm, how='left', left_on='CO_NCM', right_on='CO_NCM')

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

import glob
import pandas as pd

pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
os.chdir(pasta)

tipo = 'IMP'
busca = tipo + '_????.csv'
for index_arq, arq_nome in enumerate(glob.glob(busca)):
    print(arq_nome)
    
    pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
    df = pd.read_csv(pasta / arq_nome,
                           encoding = 'latin',
                           delimiter = ';')
    
    cond1 = df['SG_UF_NCM'] == 'MS'
    filtro = df.loc[cond1, ['CO_ANO','CO_MES','CO_NCM','CO_PAIS','VL_FOB']]
    
    if index_arq == 0:
        df_bruto = filtro.copy()
    else:
        df_bruto = df_bruto.append(filtro)
    
df_bruto.rename(columns={'CO_ANO':'year','CO_MES':'month'},inplace=True)
df_bruto['day'] = 1
df_bruto['mês'] = pd.to_datetime(df_bruto[['year', 'month', 'day']])
df_bruto.drop(['year','month','day'],axis=1,inplace=True)

meses = df_bruto.copy().groupby('mês').head(1)
meses.sort_values(by=['mês'],ascending=[True],inplace=True)
meses = meses.loc[:,'mês'].to_frame()
meses.set_index('mês',inplace=True)

dicionário = {}
# ====================================================================================

cond1 = df_bruto['CO_NCM'] == 27112100

# -----------------------------------------------------------------------------------
pasta = caminho_base / 'Dados' / 'mdic'
df_pais = pd.read_csv(pasta / 'PAIS.csv',
                       encoding = 'latin',
                       delimiter = ';')
# -----------------------------------------------------------------------------------
pais_nome = df_pais.loc[df_pais['CO_PAIS'] == 63, 'NO_PAIS']
pais_nome.index = range(len(pais_nome))
pais_nome = pais_nome.loc[0]
# ------------------
cond2 = df_bruto['CO_PAIS'] == 63
filtro = df_bruto.loc[cond1 & cond2, :]

soma_por_mes = filtro.groupby(['mês'])['VL_FOB'].sum().to_frame()
soma_por_mes.rename(columns={'VL_FOB':pais_nome},inplace=True)

meses = meses.merge(soma_por_mes,how='left',left_index=True,right_index=True)
# -----------------------------------------------------------------------------------
pais_nome = df_pais.loc[df_pais['CO_PAIS'] == 97, 'NO_PAIS']
pais_nome.index = range(len(pais_nome))
pais_nome = pais_nome.loc[0]
# ------------------
cond2 = df_bruto['CO_PAIS'] == 97
filtro = df_bruto.loc[cond1 & cond2, :]

soma_por_mes = filtro.groupby(['mês'])['VL_FOB'].sum().to_frame()
soma_por_mes.rename(columns={'VL_FOB':pais_nome},inplace=True)

meses = meses.merge(soma_por_mes,how='left',left_index=True,right_index=True)

dicionário[27112100] = meses
# ====================================================================================

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
###################################### LOOPING #######################################
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def gs_países_ncms(tipo, uf, ncms, países):
    
    import glob
    import pandas as pd
    
    pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
    os.chdir(pasta)
    
    #tipo = 'EXP'
    busca = tipo + '_????.csv'
    for index_arq, arq_nome in enumerate(glob.glob(busca)):
        print(arq_nome)
        
        pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
        df = pd.read_csv(pasta / arq_nome,
                               encoding = 'latin',
                               delimiter = ';')
        
        cond1 = df['SG_UF_NCM'] == uf
        filtro = df.loc[cond1, ['CO_ANO','CO_MES','CO_NCM','CO_PAIS','VL_FOB']]
        
        if index_arq == 0:
            df_bruto = filtro.copy()
        else:
            df_bruto = df_bruto.append(filtro)
        
    df_bruto.rename(columns={'CO_ANO':'year','CO_MES':'month'},inplace=True)
    df_bruto['day'] = 1
    df_bruto['mês'] = pd.to_datetime(df_bruto[['year', 'month', 'day']])
    df_bruto.drop(['year','month','day'],axis=1,inplace=True)
    # ---------------
    meses = df_bruto.copy().groupby('mês').head(1)
    meses.sort_values(by=['mês'],ascending=[True],inplace=True)
    meses = meses.loc[:,'mês'].to_frame()
    meses.set_index('mês',inplace=True)
    
    # -----------------------------------------------------------------------------------
    pasta = caminho_base / 'Dados' / 'mdic'
    df_pais = pd.read_csv(pasta / 'PAIS.csv',
                           encoding = 'latin',
                           delimiter = ';')
    # -----------------------------------------------------------------------------------
    dicionário = {}
    # ====================================================================================
    #ncms = [47032900,12019000]
    #países = [63,249]
    #ncms = [27112100]
    #países = [63]
    
    for ncm in ncms:
        # ====================================================================================
        cond1 = df_bruto['CO_NCM'] == ncm
        meses_cópia = meses.copy()
        for país in países:
            # -----------------------------------------------------------------------------------
            pais_nome = df_pais.loc[df_pais['CO_PAIS'] == país, 'NO_PAIS']
            pais_nome.index = range(len(pais_nome))
            pais_nome = pais_nome.loc[0]
            # ------------------
            cond2 = df_bruto['CO_PAIS'] == país
            filtro = df_bruto.loc[cond1 & cond2, :]
            
            soma_por_mes = filtro.groupby(['mês'])['VL_FOB'].sum().to_frame()
            soma_por_mes.rename(columns={'VL_FOB':pais_nome},inplace=True)
            
            meses_cópia = meses_cópia.merge(soma_por_mes,how='left',left_index=True,right_index=True)
            meses_cópia.fillna(0, inplace=True)
            meses_cópia.index.freq = 'MS'
        # -----------------------------------------------------------------------------------
        dicionário[ncm] = meses_cópia
        # -----------------------------------------------------------------------------------
    return dicionário
    # -----------------------------------------------------------------------------------

ncms = [47032900,12019000]
países = [63,249]

expMS_ncmsPaíses = gs_países_ncms(tipo='EXP', uf='MS', ncms=ncms, países=países)













