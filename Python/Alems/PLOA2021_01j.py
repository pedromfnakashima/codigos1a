# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:55:19 2020

@author: pedro
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

import pandas as pd

# PEGAR O DEFLATOR MENSAL
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
df_ipca = df_ipca.loc[:,['deflator']]
df_ipca.reset_index(inplace=True)

uf = 'MS'

##### 2019
pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2019q2.zip',
                           caminho=pasta,
                           pasta=False)

df['year'] = df['mês'].dt.year
cond1 = df['UF'] == uf
cond2 = df['year'] == 2019
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond = cond1 & cond2 & cond3
filtro = df.loc[cond,:]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2019 = filtro['Valor_d'].sum()

##### 2020
pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2020q2.zip',
                           caminho=pasta,
                           pasta=False)

df['year'] = df['mês'].dt.year
cond1 = df['UF'] == uf
cond2 = df['year'] == 2020
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond = cond1 & cond2 & cond3
filtro = df.loc[cond,:]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2020 = filtro['Valor_d'].sum()





####################################################################
##################### MONTAR O LOOPING #############################
####################################################################

def variacao_g_pessoal():
    
    # PEGAR O DEFLATOR MENSAL
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
    df_ipca.index.freq = 'MS'
    atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
    df_ipca['deflator'] = atual / df_ipca['Índice']
    df_ipca = df_ipca.loc[:,['deflator']]
    df_ipca.reset_index(inplace=True)
    
    ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
     'SE', 'PB', 'MA', 'CE', 'AL', 'RJ', 'PI', 'AC', 'RS', 'DF', 'RR', 'MG', 'RN']
    
    df_somas = pd.DataFrame(columns=['UF','soma_2019', 'soma_2020'])
    
    for index, uf in enumerate(ufs):
        #print(index, uf)
        ##### 2019
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
        df = processa_arquivos_zip(arquivo='2019q2.zip',
                                   caminho=pasta,
                                   pasta=False)
        
        df['year'] = df['mês'].dt.year
        cond1 = df['UF'] == uf
        cond2 = df['year'] == 2019
        cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
        cond = cond1 & cond2 & cond3
        filtro = df.loc[cond,:]
        filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
        filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
        soma_2019 = filtro['Valor_d'].sum()
        
        ##### 2020
        pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
        df = processa_arquivos_zip(arquivo='2020q2.zip',
                                   caminho=pasta,
                                   pasta=False)
        
        df['year'] = df['mês'].dt.year
        cond1 = df['UF'] == uf
        cond2 = df['year'] == 2020
        cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
        cond = cond1 & cond2 & cond3
        filtro = df.loc[cond,:]
        filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
        filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
        soma_2020 = filtro['Valor_d'].sum()
        
        df_somas.loc[index,'UF'] = uf
        df_somas.loc[index,'soma_2019'] = soma_2019
        df_somas.loc[index,'soma_2020'] = soma_2020
        
        
        df_somas['mult'] = df_somas['soma_2020'] / df_somas['soma_2019']
        df_somas.sort_values(by=['mult'], inplace=True)
        df_somas['var_percent'] = ((df_somas['soma_2020'] - df_somas['soma_2019']) / df_somas['soma_2019']) * 100
        
    return df_somas


df_somas = variacao_g_pessoal()

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    df_somas.to_excel(writer, sheet_name='var_g_pessoal', index=False)

######################################################################################################
######################################################################################################
######################################################################################################

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2020q1.zip',
                           caminho=pasta,
                           pasta=False)


uf = 'DF'
instituicao = 'Câmara Legislativa'

df['year'] = df['mês'].dt.year
cond1 = df['UF'] == uf
cond1a = df['Instituição'] == instituicao
cond2 = df['year'] == 2020
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
#cond = cond1 & cond1a & cond2 & cond3
cond = cond1 & cond1a & cond2 & cond3
filtro = df.loc[cond,:]





######################################################################################################
######################################################################################################
######################################################################################################

pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
df_ipca = df_ipca.loc[:,['deflator']]
df_ipca.reset_index(inplace=True)


uf = 'MS'
instituicao = 'Governo'

pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
df = processa_arquivos_zip(arquivo='2019q2.zip',
                           caminho=pasta,
                           pasta=False)

df['year'] = df['mês'].dt.year
cond1 = df['UF'] == uf
cond1a = df['Instituição'] == instituicao
cond2 = df['year'] == 2019
cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
cond = cond1 & cond1a & cond2 & cond3
filtro = df.loc[cond,:]
filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
soma_2019 = filtro['Valor_d'].sum()


######################################################################################################
######################################################################################################
######################################################################################################

def variacao_g_pessoal_orgaos():
    
    # PEGAR O DEFLATOR MENSAL
    pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
    df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
    df_ipca.index.freq = 'MS'
    atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
    df_ipca['deflator'] = atual / df_ipca['Índice']
    df_ipca = df_ipca.loc[:,['deflator']]
    df_ipca.reset_index(inplace=True)
    
    ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
     'SE', 'PB', 'MA', 'CE', 'RJ', 'PI', 'AC', 'RS', 'RR', 'MG', 'RN', 'AL', 'DF']
    
    instituicoes = ['Governo', 'Tribunal de Contas', 'Tribunal de Justiça', 'Ministério Público', 'Defensoria Pública', 'Assembleia Legislativa', 'Câmara Legislativa']
    
    dicionario = {}
    
    for instituicao in instituicoes:
        
        if instituicao == 'Assembleia Legislativa':
            ufs = ['MT', 'AM', 'RO', 'BA', 'SP', 'MS', 'SC', 'GO', 'ES', 'PA', 'TO', 'PR', 'PE', 'AP',
                   'SE', 'PB', 'MA', 'CE', 'RJ', 'PI', 'AC', 'RS', 'RR', 'MG', 'RN']
        if instituicao == 'Câmara Legislativa':
            ufs = ['DF']
        
        print(f'Processando {instituicao}')
        
        df_somas = pd.DataFrame(columns=['UF','soma_2019', 'soma_2020'])
        
        for index, uf in enumerate(ufs):
            #print(index, uf)
            ##### 2019
            pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
            df = processa_arquivos_zip(arquivo='2019q2.zip',
                                       caminho=pasta,
                                       pasta=False)
            
            df['year'] = df['mês'].dt.year
            cond1 = df['UF'] == uf
            cond1a = df['Instituição'] == instituicao
            cond2 = df['year'] == 2019
            cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
            cond = cond1 & cond1a & cond2 & cond3
            filtro = df.loc[cond,:]
            filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
            filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
            soma_2019 = filtro['Valor_d'].sum()
            
            ##### 2020
            pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Estados' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'Despesas com pessoal'
            df = processa_arquivos_zip(arquivo='2020q2.zip',
                                       caminho=pasta,
                                       pasta=False)
            
            df['year'] = df['mês'].dt.year
            cond1 = df['UF'] == uf
            cond1a = df['Instituição'] == instituicao
            cond2 = df['year'] == 2020
            cond3 = df['Conta'].str.contains('líquida com pessoal', case=False)
            cond = cond1 & cond1a & cond2 & cond3
            filtro = df.loc[cond,:]
            filtro = filtro.merge(df_ipca, how='left', left_on='mês', right_on='data')
            filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
            soma_2020 = filtro['Valor_d'].sum()
            
            df_somas.loc[index,'UF'] = uf
            df_somas.loc[index,'soma_2019'] = soma_2019
            df_somas.loc[index,'soma_2020'] = soma_2020
            
            
            df_somas['mult'] = df_somas['soma_2020'] / df_somas['soma_2019']
            df_somas.sort_values(by=['mult'], inplace=True)
            df_somas['var_percent'] = ((df_somas['soma_2020'] - df_somas['soma_2019']) / df_somas['soma_2019']) * 100
        
        dicionario[instituicao] = df_somas    
        
    return dicionario


dic_somas_orgaos = variacao_g_pessoal_orgaos()


p_org_UFs_AL = dic_somas_orgaos['Assembleia Legislativa']
p_org_UFs_CL = dic_somas_orgaos['Câmara Legislativa']
p_org_UFs_DP = dic_somas_orgaos['Defensoria Pública']
p_org_UFs_Gov = dic_somas_orgaos['Governo']
p_org_UFs_MP = dic_somas_orgaos['Ministério Público']
p_org_UFs_TC = dic_somas_orgaos['Tribunal de Contas']
p_org_UFs_TJ = dic_somas_orgaos['Tribunal de Justiça']

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_AL.to_excel(writer, sheet_name='p_org_UFs_AL', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_CL.to_excel(writer, sheet_name='p_org_UFs_CL', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_DP.to_excel(writer, sheet_name='p_org_UFs_DP', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_Gov.to_excel(writer, sheet_name='p_org_UFs_Gov', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_MP.to_excel(writer, sheet_name='p_org_UFs_MP', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_TC.to_excel(writer, sheet_name='p_org_UFs_TC', index=False)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    p_org_UFs_TJ.to_excel(writer, sheet_name='p_org_UFs_TJ', index=False)



