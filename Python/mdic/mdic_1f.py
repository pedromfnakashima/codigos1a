# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:40:44 2020

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


def gs_mdic(tipo, ufs, ncms):
    
    import glob
    import numpy as np
    import pandas as pd
    
    pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
    os.chdir(pasta)
    
    # -----------------------------------------------------------------------------------
    
    np_datas = np.arange('2018-01-01','2022-01-01', 1, dtype='datetime64[M]')
    meses = pd.to_datetime(np_datas).to_frame()
    meses.rename(columns={0:'mês'}, inplace=True)
    meses.set_index('mês',inplace=True)
    meses.index.freq = 'MS'
    
    # -----------------------------------------------------------------------------------
    
    #tipo = 'EXP'
    #uf = 'MS'
    #ufs = ['MS','MT','GO']
    #ncm = 12019000
    #ncms = [12019000,10059010]
    busca = tipo + '_????.csv'
    
    # -----------------------------------------------------------------------------------
    #ncm = 12019000
    
    for index_ncm, ncm in enumerate(ncms):
        
        for index_arq, arq_nome in enumerate(glob.glob(busca)):
            print(arq_nome)
            
            pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
            df = pd.read_csv(pasta / arq_nome,
                                   encoding = 'latin',
                                   delimiter = ';')
            
            df.rename(columns={'CO_ANO':'year','CO_MES':'month'},inplace=True)
            df['day'] = 1
            df['mês'] = pd.to_datetime(df[['year', 'month', 'day']])
            df.drop(['year','month','day'],axis=1,inplace=True)
            
            cond1 = df['CO_NCM'] == ncm
            filtro_ncm = df.loc[cond1,:]
            
            df_soma_por_uf = filtro_ncm.groupby(['mês','SG_UF_NCM'])['VL_FOB'].sum().to_frame()
            
            if index_arq == 0:
                df_bruto = df_soma_por_uf.copy()
            else:
                df_bruto = df_bruto.append(df_soma_por_uf)
        
        
        df_bruto.reset_index(inplace=True)
        df_bruto.set_index('mês',inplace=True)
        
        df_bruto_br = df_bruto.groupby(['mês'])['VL_FOB'].sum().to_frame()
        
        if tipo == 'EXP':
            tipo_sigla = 'X'
        elif tipo == 'IMP':
            tipo_sigla = 'M'
        
        col_nome = tipo_sigla + 'BR' + str(ncm)
        df_bruto_br.rename(columns={'VL_FOB':col_nome},inplace=True)
        
        meses_copia = meses.copy()
        meses_copia = meses_copia.merge(df_bruto_br,how='left',left_index=True,right_index=True)
        
        for uf in ufs:
            cond1 = df_bruto['SG_UF_NCM'] == uf
            df_bruto_uf_i = df_bruto.copy().loc[cond1,['VL_FOB']]
            col_nome = tipo_sigla + uf + str(ncm)
            df_bruto_uf_i.rename(columns={'VL_FOB':col_nome},inplace=True)
            
            meses_copia = meses_copia.merge(df_bruto_uf_i,how='left',left_index=True,right_index=True)
        
        if index_ncm == 0:
            df_final = meses_copia.copy()
        else:
            df_final = df_final.merge(meses_copia, how='left', left_index=True, right_index=True)
    
    df_final.dropna(thresh=1, inplace=True)
    df_final.fillna(0, inplace=True)
    
    return df_final

ufs = ['MS','MT','GO']
ncms = [12019000,10059010]

df_series_exp = gs_mdic(tipo='EXP', ufs=ufs, ncms=ncms)























