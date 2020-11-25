# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:00:53 2020

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

def g_topNcms(tipo, ncms, detalhamento='uf'):
    
    import glob
    import numpy as np
    import pandas as pd
    
    #tipo = 'EXP'
    #ncm = 12019000
    busca = tipo + '_????.csv'
    
    if tipo == 'EXP':
        tipo_sigla = 'X'
    elif tipo == 'IMP':
        tipo_sigla = 'M'
    
    pasta = caminho_base / 'Dados' / 'mdic' / 'anos'
    os.chdir(pasta)
    
    # -------------------------------------------------------
    pasta = caminho_base / 'Dados' / 'mdic'
    df_ncm = pd.read_csv(pasta / 'NCM.csv',
                           encoding = 'latin',
                           delimiter = ';')
    df_ncm = df_ncm.loc[:, ['CO_NCM','NO_NCM_POR']]
    # -------------------------------------------------------
    pasta = caminho_base / 'Dados' / 'mdic'
    df_pais = pd.read_csv(pasta / 'PAIS.csv',
                           encoding = 'latin',
                           delimiter = ';')
    df_pais = df_pais.loc[:, ['CO_PAIS','NO_PAIS']]
    # -------------------------------------------------------
    
    print('\n=========================\nNúmero de vezes no Top 5\n=========================\n')
    
    for index_ncm, ncm in enumerate(ncms):

        # -------------------------------------------------
        cond1 = df_ncm['CO_NCM'] == ncm
        filtro = df_ncm.loc[cond1,['NO_NCM_POR']]
        filtro.reset_index(inplace=True)
        nome_ncm = filtro.loc[0,'NO_NCM_POR']
        # -------------------------------------------------
        
        for index_arq, arq_nome in enumerate(glob.glob(busca)):
            
            arq_nome = 'EXP_2018.csv'
            
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
            
            if detalhamento == 'uf':
                df_detalhamento = filtro_ncm.groupby(['mês','SG_UF_NCM'])['VL_FOB'].sum().to_frame()
                df_detalhamento.reset_index(inplace=True)
                df_detalhamento.sort_values(by=['mês','VL_FOB'], ascending=[True,False],inplace=True)
                df_detalhamento['rank'] = df_detalhamento.groupby(['mês']).cumcount()+1
                df_detalhamento = df_detalhamento.loc[df_detalhamento['rank']<=5,:]
                
                col_nome = tipo_sigla + str(ncm)
                df_detalhamento = df_detalhamento.loc[:, ['mês','rank','SG_UF_NCM']]
                df_detalhamento.rename(columns={'SG_UF_NCM':col_nome}, inplace=True)
                df_detalhamento.set_index(['mês','rank'], inplace=True)


            
            elif detalhamento == 'país':
                df_detalhamento = filtro_ncm.groupby(['mês','CO_PAIS'])['VL_FOB'].sum().to_frame()
                df_detalhamento.reset_index(inplace=True)
                df_detalhamento.sort_values(by=['mês','VL_FOB'], ascending=[True,False],inplace=True)
                df_detalhamento['rank'] = df_detalhamento.groupby(['mês']).cumcount()+1
                df_detalhamento = df_detalhamento.loc[df_detalhamento['rank']<=5,:]
            
                col_nome = tipo_sigla + str(ncm)
                df_detalhamento = df_detalhamento.loc[:, ['mês','rank','CO_PAIS']]
                df_detalhamento.rename(columns={'CO_PAIS':col_nome}, inplace=True)

                
                df_detalhamento = df_detalhamento.merge(df_pais,how='left',left_on=col_nome,right_on='CO_PAIS')
                df_detalhamento = df_detalhamento[['mês','rank','NO_PAIS']]

            
            if index_arq == 0:
                df_bruto = df_detalhamento.copy()
            else:
                df_bruto = df_bruto.append(df_detalhamento)
        
        # -------------------------------------------------
        if detalhamento == 'uf':
            print(f'\n-----------------\nCódigo:{ncm}\n{nome_ncm}\n',df_detalhamento[col_nome].value_counts(),sep='\n')
        elif detalhamento == 'país':
            print(f'\n-----------------\nCódigo:{ncm}\n{nome_ncm}\n',df_detalhamento['NO_PAIS'].value_counts(),sep='\n')
        
        if index_ncm == 0:
            df_final = df_bruto.copy()
        else:
            df_final = df_final.merge(df_bruto, how='left', left_index=True, right_index=True)
    
    return df_final


ncms = [12019000,10059010]

series_uf = g_topNcms(tipo='EXP', ncms=ncms, detalhamento='uf')
series_países = g_topNcms(tipo='EXP', ncms=ncms, detalhamento='país')


##########################################################################################################
##########################################################################################################
##########################################################################################################


























































