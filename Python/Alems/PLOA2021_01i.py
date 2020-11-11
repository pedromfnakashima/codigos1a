# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:19:40 2020

@author: pedro-salj
"""

globals().clear()
""" Mudar diretório """
import os
from pathlib import Path
import getpass
if getpass.getuser() == "pedro":
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

##################################################################################################

########################### IPCA #########################################
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
df_ipca['mês'] = df_ipca.index.month
df_ipca['ano'] = df_ipca.index.year
cond = df_ipca['mês'] == 10
df_ipca = df_ipca.loc[cond,:]
df_ipca.drop(['mês'], axis=1, inplace=True)
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
##########################################################################

# Rodar antes o arquivo junta_siconfi_01c.py

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                                           caminho=pasta,
                                           pasta=False)

# ----------------------------------------------------------------------
# DESPESAS COM PESSOAL DE MS, SOMADAS DE TODOS OS PODERES, POR ANO
# ----------------------------------------------------------------------

cond1 = df['UF'] == 'MS'
cond1a = df['PODER'] == 'Legislativo'
#cond2 = df['exercicio'] == 2020
#cond2a = df['periodo'] == 2
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
#cond3 = df['Conta'] == '3.1.00.00.00.00'
cond4 = df['Coluna'].str.contains('12 meses', case=False)
#cond = cond1 & cond2 & cond2a & cond3 & cond4
cond = cond1 & cond3 & cond4
filtro = df.loc[cond, :]
soma_desp_pessoal = filtro['Valor'].sum()

# ----------------------------------------------------------------------

cond1 = df['UF'] == 'BA'
cond1a = df['Instituição'] == 'Tribunal de Contas'
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond4 = df['Coluna'].str.contains('12 meses', case=False)
cond = cond1 & cond1a & cond3 & cond4
filtro = df.loc[cond, :]
filtro = filtro.groupby(['Instituição'])['Valor'].sum().to_frame()
filtro.reset_index(inplace=True)
Valor = filtro.loc[0,'Valor']

# ----------------------------------------------------------------------

cond1 = df['UF'] == 'MS'
cond1a = df['Instituição'] == 'Governo'
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond4 = df['Coluna'].str.contains('12 meses', case=False)
cond = cond1 & cond1a & cond3 & cond4
filtro = df.loc[cond, :]
filtro = filtro.groupby(['Instituição'])['Valor'].sum().to_frame()
filtro.reset_index(inplace=True)
Valor = filtro.loc[0,'Valor']
print(Valor)

# ----------------------------------------------------------------------

cond1 = df['UF'] == 'AL' # <-------------------------------------------- Alagoas não mandou da Assembleia Legislativa!!!!
cond1a = df['Instituição'] == 'Assembleia Legislativa'
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond4 = df['Coluna'].str.contains('12 meses', case=False)
cond = cond1 & cond1a & cond3 & cond4
filtro = df.loc[cond, :]
filtro = filtro.groupby(['Instituição'])['Valor'].sum().to_frame()
filtro.reset_index(inplace=True)
Valor = filtro.loc[0,'Valor']

print(Valor)

dicionario = {}

dicionario['entrada1'] = filtro


soma_desp_pessoal = filtro['Valor'].sum()

instituicoes = ['Assembleia Legislativa', 'Governo', 'Tribunal de Contas', 'Tribunal de Justiça', 'Ministério Público', 'Defensoria Pública']


# ------------------------------------------
# RCL DE CADA ESTADO
# ------------------------------------------

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                                           caminho=pasta,
                                           pasta=False)
cond1 = df['UF'] == 'MS'
cond1a = df['PODER'] == 'Executivo'
cond3 = df['Conta'].str.contains('receita corrente líquida', case=False)
cond = cond1 & cond1a & cond3
filtro = df.loc[cond, :]
filtro.reset_index(inplace=True)
rcl = filtro.loc[0,'Valor']

####################################################################
##################### MONTAR O LOOPING #############################
##################### Soma dos Órgãos ##############################
####################################################################

def receita_pessoal_ufs():
   
    import pandas as pd
   
    ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
           'SE', 'PB', 'MA', 'CE', 'AL', 'RJ', 'PI', 'AC', 'RS', 'DF', 'RR', 'MG', 'RN']
        
    df_somas = pd.DataFrame(columns=['UF','soma_desp_pessoal', 'RCL'])
    
    for index, uf in enumerate(ufs):
        #print(index, uf)
        
        # SOMA DAS DESPESAS COM PESSOAL DE TODOS OS PODERES
        
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
        df = processa_arquivos_zip(arquivo='2020q2.zip',
                                   caminho=pasta,
                                   pasta=False)
            
            
        cond1 = df['UF'] == uf
        cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
        cond4 = df['Coluna'].str.contains('12 meses', case=False)
        cond = cond1 & cond3 & cond4
        filtro = df.loc[cond, :]
        soma_desp_pessoal = filtro['Valor'].sum()
        
        
        # RECEITA CORRENTE LÍQUIDA
        
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
        df = processa_arquivos_zip(arquivo='2020q2.zip',
                                                   caminho=pasta,
                                                   pasta=False)
        cond1 = df['UF'] == uf
        cond1a = df['PODER'] == 'Executivo'
        cond3 = df['Conta'].str.contains('receita corrente líquida', case=False)
        cond = cond1 & cond1a & cond3
        filtro = df.loc[cond, :]
        filtro.reset_index(inplace=True)
        rcl = filtro.loc[0,'Valor']
        
        df_somas.loc[index,'UF'] = uf
        df_somas.loc[index,'soma_desp_pessoal'] = soma_desp_pessoal
        df_somas.loc[index,'RCL'] = rcl
    
    df_somas['pessoal_rcl'] = (df_somas['soma_desp_pessoal'] / df_somas['RCL']) * 100
    df_somas.sort_values(by=['pessoal_rcl'], ascending=[False],inplace=True)
    
    return df_somas


df_somas = receita_pessoal_ufs()

df_somas.sort_values(by=['pessoal_rcl'], ascending=[False],inplace=True)

####################################################################
##################### MONTAR O LOOPING #############################
######################## Por Órgão #################################
####################################################################

def receita_pessoal_ufs_orgaos():
   
    import pandas as pd
   

   #Exclusões de UFs (faltam dados): AL, DF

   
    ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP', 'SE', 'PB', 'MA', 'CE', 'RJ', 'PI', 'AC', 'RS', 'RR', 'MG', 'RN']
    instituicoes = ['Assembleia Legislativa', 'Governo', 'Tribunal de Contas', 'Tribunal de Justiça', 'Ministério Público', 'Defensoria Pública']
    
    #ufs = ['MS']
    #instituicoes = ['Assembleia Legislativa', 'Governo']
    
    
    #df_somas = pd.DataFrame(columns=['UF','desp_pessoal', 'RCL'])
    
    dicionario = {}
    
    for instituicao in instituicoes:
        
        print(f'Processando {instituicao}')
        
        df_somas = pd.DataFrame(columns=['UF','desp_pessoal', 'RCL'])
    
        for index, uf in enumerate(ufs):
            print(f'Processando {uf}')
            #print(index, uf)
            
            # SOMA DAS DESPESAS COM PESSOAL DE TODOS OS PODERES
            
            pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
            df = processa_arquivos_zip(arquivo='2020q2.zip',
                                       caminho=pasta,
                                       pasta=False)
            
            cond1 = df['UF'] == uf
            cond1a = df['Instituição'] == instituicao
            cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
            cond4 = df['Coluna'].str.contains('12 meses', case=False)
            cond = cond1 & cond1a & cond3 & cond4
            filtro = df.loc[cond, :]
            filtro = filtro.groupby(['Instituição'])['Valor'].sum().to_frame()
            filtro.reset_index(inplace=True)
            Valor = filtro.loc[0,'Valor']
            
            # RECEITA CORRENTE LÍQUIDA
            
            pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
            df = processa_arquivos_zip(arquivo='2020q2.zip',
                                                       caminho=pasta,
                                                       pasta=False)
            cond1 = df['UF'] == uf
            cond1a = df['PODER'] == 'Executivo'
            cond3 = df['Conta'].str.contains('receita corrente líquida', case=False)
            cond = cond1 & cond1a & cond3
            filtro = df.loc[cond, :]
            filtro.reset_index(inplace=True)
            rcl = filtro.loc[0,'Valor']
            
            # ---------------------------------------------------------------------------------------------------------------
            
            df_somas.loc[index,'UF'] = uf
            df_somas.loc[index,'desp_pessoal'] = Valor
            df_somas.loc[index,'RCL'] = rcl
            
        df_somas['pessoal_rcl'] = (df_somas['desp_pessoal'] / df_somas['RCL']) * 100
        df_somas.sort_values(by=['pessoal_rcl'], ascending=[False],inplace=True)
        
        print(f'Adicionando {instituicao} ao dicionário.')
        dicionario[instituicao] = df_somas
        print(f'{instituicao} adicionado ao dicionário.')
    
    #df_somas['pessoal_rcl'] = (df_somas['soma_desp_pessoal'] / df_somas['RCL']) * 100
    #df_somas.sort_values(by=['pessoal_rcl'], ascending=[False],inplace=True)
    
    return dicionario


df_orgaos = receita_pessoal_ufs_orgaos()






















