# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:52:50 2020

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


df = junta_arqs(arqs_csv=arqs_csv, pasta=pasta)


##########################################################################################################
################################# Importa categorias IBGE ######################################
##########################################################################################################

def gs_catBCipca(df):
    
    # Filtra para dados do BRASIL
    cond1 = df['D1C'] == '1'
    df = df.copy().loc[cond1,['dt','códIBGE','D2N','C_NC_M','D_SD_ND_M_S','V']]
    
    # Ordena com base: data, código do IBGE, e tipo(variação ou peso)
    df.sort_values(by=['dt','códIBGE','D2N'],ascending=[True,True,False],inplace=True)
    
    # Cria dfVP, com colunas separadas para variação e peso, por subitem
    li_variação_peso = ['Variação', 'Peso']
    for index_vp, VP in enumerate(li_variação_peso):
        cond1 = df['D2N'].str.contains(VP,case=False)
        dfVP_i = df.copy().loc[cond1,['dt','códIBGE','C_NC_M','D_SD_ND_M_S','V']]
        dfVP_i.set_index(['dt','códIBGE'],inplace=True)
        dfVP_i.rename(mapper={'V':VP},axis=1,inplace=True)
        if index_vp == 0:
            dfVP = dfVP_i.copy()
        else:
            dfVP_i.drop(['C_NC_M','D_SD_ND_M_S'],axis=1,inplace=True)
            dfVP = dfVP.merge(dfVP_i,how='left',left_index=True,right_index=True)
    
    dfVP['Contribuição'] = dfVP['Variação'] * dfVP['Peso']
    
    # Reseta index para que possa ser feito o groupby
    dfVP.reset_index(inplace=True)
    
    dicionário1 = {}
    li_classificações = ['C_NC_M', 'D_SD_ND_M_S']
    for classi in li_classificações:
        # print(classi)
        df_SP = dfVP.groupby(['dt',classi])['Peso'].sum().to_frame() # SP: Soma dos Pesos
        df_SC = dfVP.groupby(['dt',classi])['Contribuição'].sum().to_frame() # SC: Soma das Contribuições
        df_SPSC = df_SP.merge(df_SC,how='left',left_index=True,right_index=True)
        df_SPSC['Variação'] = df_SPSC['Contribuição'] / df_SPSC['Peso']
        df_SPSC.reset_index(inplace=True)
        dicionário1[classi] = df_SPSC
    
    # Montar as séries
    
    print(df.dtypes)
    
    ############################################################
    #################### C_NC_M ################################
    ############################################################
    
    dicionário2 = {}
    
    li_variação_peso = ['Peso', 'Variação']
    for VP in li_variação_peso:
        
        # VP = 'Peso'
        
    
        cond1 = df['códIBGE'] == '0'
        cond2 = df['D2N'].str.contains(VP,case=False)
        df_ipca = df.loc[cond1 & cond2, ['dt','V']]
        df_ipca.rename(mapper={'V':'ipca'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['C_NC_M']['C_NC_M'] == 'NC'
        df_nãoComercializáveis = dicionário1['C_NC_M'].loc[cond1,['dt',VP]]
        df_nãoComercializáveis.rename(mapper={VP:'nãoComercializáveis'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['C_NC_M']['C_NC_M'] == 'M'
        df_monitorados = dicionário1['C_NC_M'].loc[cond1,['dt',VP]]
        df_monitorados.rename(mapper={VP:'monitorados'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['C_NC_M']['C_NC_M'] == 'C'
        df_comercializáveis = dicionário1['C_NC_M'].loc[cond1,['dt',VP]]
        df_comercializáveis.rename(mapper={VP:'comercializáveis'},axis=1,inplace=True)
        #---------------------------------
        df_class1 = df_ipca.copy()
        df_class1 = df_class1.merge(df_comercializáveis,how='left',left_on='dt',right_on='dt')
        df_class1 = df_class1.merge(df_nãoComercializáveis,how='left',left_on='dt',right_on='dt')
        df_class1 = df_class1.merge(df_monitorados,how='left',left_on='dt',right_on='dt')
        
        dicionário2[VP] = df_class1
    
    # ----
    dicionário2['Peso']['livres'] = dicionário2['Peso']['ipca'] - dicionário2['Peso']['monitorados']
    dicionário2['Variação']['livres'] = (dicionário2['Variação']['ipca'] * 100 - dicionário2['Variação']['monitorados'] * dicionário2['Peso']['monitorados']) / dicionário2['Peso']['livres']
    # ----
    dicionário2['Peso'].set_index('dt',inplace=True)
    dicionário2['Variação'].set_index('dt',inplace=True)
    # ----
    dicionário2['Contribuição'] = (dicionário2['Peso'] * dicionário2['Variação']) / 100
    
    ############################################################
    #################### D_SD_ND_M_S ###########################
    ############################################################
    
    dicionário3 = {}
    
    li_variação_peso = ['Peso', 'Variação']
    for VP in li_variação_peso:
        
        # VP = 'Peso'
        
        cond1 = df['códIBGE'] == '0'
        cond2 = df['D2N'].str.contains(VP,case=False)
        df_ipca = df.loc[cond1 & cond2, ['dt','V']]
        df_ipca.rename(mapper={'V':'ipca'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['D_SD_ND_M_S']['D_SD_ND_M_S'] == 'D'
        df_duráveis = dicionário1['D_SD_ND_M_S'].loc[cond1,['dt',VP]]
        df_duráveis.rename(mapper={VP:'duráveis'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['D_SD_ND_M_S']['D_SD_ND_M_S'] == 'SD'
        df_semiDuráveis = dicionário1['D_SD_ND_M_S'].loc[cond1,['dt',VP]]
        df_semiDuráveis.rename(mapper={VP:'semiDuráveis'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['D_SD_ND_M_S']['D_SD_ND_M_S'] == 'ND'
        df_nãoDuráveis = dicionário1['D_SD_ND_M_S'].loc[cond1,['dt',VP]]
        df_nãoDuráveis.rename(mapper={VP:'nãoDuráveis'},axis=1,inplace=True)
        #---------------------------------
        cond1 = dicionário1['D_SD_ND_M_S']['D_SD_ND_M_S'] == 'S'
        df_serviços = dicionário1['D_SD_ND_M_S'].loc[cond1,['dt',VP]]
        df_serviços.rename(mapper={VP:'serviços'},axis=1,inplace=True)
        #---------------------------------
        df_class1 = df_ipca.copy()
        df_class1 = df_class1.merge(df_nãoDuráveis,how='left',left_on='dt',right_on='dt')
        df_class1 = df_class1.merge(df_semiDuráveis,how='left',left_on='dt',right_on='dt')
        df_class1 = df_class1.merge(df_duráveis,how='left',left_on='dt',right_on='dt')
        df_class1 = df_class1.merge(df_serviços,how='left',left_on='dt',right_on='dt')
        dicionário3[VP] = df_class1
    
    # ----
    dicionário3['Peso'].set_index('dt',inplace=True)
    dicionário3['Variação'].set_index('dt',inplace=True)
    # ----
    dicionário3['Contribuição'] = (dicionário3['Peso'] * dicionário3['Variação']) / 100
    
    ############################################################
    ########### C_NC_M + D_SD_ND_M_S ###########################
    ############################################################
    dicionário3['Peso'].drop(['ipca'],axis=1,inplace=True)
    dicionário3['Variação'].drop(['ipca'],axis=1,inplace=True)
    dicionário3['Contribuição'].drop(['ipca'],axis=1,inplace=True)
    # --------------
    dicionário4 = dicionário2.copy()
    # --------------
    dicionário4['Peso'] = dicionário4['Peso'].merge(dicionário3['Peso'],how='left',left_index=True,right_index=True)
    dicionário4['Variação'] = dicionário4['Variação'].merge(dicionário3['Variação'],how='left',left_index=True,right_index=True)
    dicionário4['Contribuição'] = dicionário4['Contribuição'].merge(dicionário3['Contribuição'],how='left',left_index=True,right_index=True)
    # --------------
    dicionário4['Peso'].index.freq='MS'
    dicionário4['Variação'].index.freq='MS'
    dicionário4['Contribuição'].index.freq='MS'
    # --------------
    return dicionário4
    # --------------

dicCatBC = gs_catBCipca(df)








