# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 07:17:52 2020

@author: pedro-salj

Relatórios fiscais do Estado:




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
caminho_wd = caminho_base / 'Dados' / 'Firjan'
os.chdir(caminho_wd)
##########################################################################################################
##########################################################################################################
##########################################################################################################
import numpy as np
import pandas as pd

pasta = caminho_wd = caminho_base / 'Dados'
municipios = pd.read_excel(pasta / 'municipios.xlsx', sheet_name='municipios', skiprows=0, dtype={'capital': np.bool})
capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})


def gera_df(nome_zip, caminho):
    import zipfile
    import io
    import pandas as pd
    
    caminho = Path(caminho) / nome_zip
    
    with zipfile.ZipFile(caminho, 'r') as zf:
        csv_nome = zf.namelist()[0]
        with io.TextIOWrapper(zf.open(csv_nome), encoding="latin") as f:
            f_contents = f.readline()
            lista = [f_contents]
            contador = 0
            while f_contents.find(';') == -1:
                contador += 1
                f_contents = f.readline()
                lista.append(f_contents)
    df = pd.read_csv(caminho, compression='zip', header=0, sep=';', decimal=',', quotechar='"', encoding = 'latin', skiprows=contador)
    
    li_exercicio = lista[0].replace('\n','').split(':')
    li_exercicio = [elemento.strip() for elemento in li_exercicio]
    ano = li_exercicio[1]
    
    df['exercicio'] = int(ano)
    
    bool_RGF = csv_nome.find('RGF')
    bool_RREO = csv_nome.find('RREO')
    
    if bool_RGF > 0 or bool_RREO > 0:
        
        li_periodo = lista[1].replace('\n','').split(':')
        li_periodo = [elemento.strip() for elemento in li_periodo]
        li_periodo = li_periodo[1]
        li_periodo = li_periodo.split('.')
        li_periodo = [elemento.strip() for elemento in li_periodo]
        periodo_num = li_periodo[0][0]
        periodo_unidade = li_periodo[1]
        
        # Adiciona unidade ao DF (ex.: bimestre, quadrimestre)
        df[periodo_unidade] = int(periodo_num)
    else:
        #print('É contas anuais.')
        pass
    # Manipula coluna Instituição
    """ Usando regex """
    df['Instituição'] = df['Instituição'].str.replace('\sdo[\s\w]+', '')
    """ Usando filtro """
    filtro = df['Instituição'].str.contains('Justiça Militar')
    df.loc[filtro, 'Instituição'] = 'Tribunal de Justiça Militar'
    
    return df
    
def processa_arquivos_zip(arquivo, caminho = os.getcwd(), pasta=False):
    
    import zipfile
    import io
    from pathlib import Path
    
    print('Adicionados:')
    
    if pasta == True:
        
        os.chdir(caminho)
        
        import glob
        dicionario = {}
        
        for arq_nome in glob.glob('*.zip'):
            #print(arq_nome)
            pos_ponto = arq_nome.find('.zip')
            df_nome = f'df_{arq_nome[0:pos_ponto]}'
            print(df_nome)
            dicionario[df_nome] = gera_df(arq_nome, caminho)
        
        
        i = 1
        for key in dicionario.keys():
            
            if i == 1:
                novo_df = dicionario[key]
            else:
                novo_df = novo_df.append(dicionario[key])
            i += 1
        
        return novo_df
        
    else:
        novo_df = gera_df(arquivo, caminho)
        print(f'  {arquivo}')
        return novo_df

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

def processa_arquivos_zip(arquivo, caminho = os.getcwd(), pasta=False):
    
    import zipfile
    import io
    from pathlib import Path
    
    print('Adicionados:')
    
    if pasta == True:
        
        os.chdir(caminho)
        
        import glob
        dicionario = {}
        
        for arq_nome in glob.glob('*.zip'):
            #print(arq_nome)
            pos_ponto = arq_nome.find('.zip')
            df_nome = f'df_{arq_nome[0:pos_ponto]}'
            print(df_nome)
            dicionario[df_nome] = gera_df(arq_nome, caminho)
        
        
        i = 1
        for key in dicionario.keys():
            
            if i == 1:
                novo_df = dicionario[key]
            else:
                novo_df = novo_df.append(dicionario[key])
            i += 1
        
        return novo_df
        
    else:
        novo_df = gera_df(arquivo, caminho)
        print(f'  {arquivo}')
        return novo_df
        


############# DESPESAS POR FUNÇÃO
pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Estados' / 'Despesas por Função'
ca_desp_função = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta,
                                           pasta=True)

cond1 = ca_desp_função['exercicio'] >= 2016
filtro = ca_desp_função.loc[cond1, :]



print(np.arange('2020-08-01','2018-06-23', 7, dtype='datetime64[D]'))




















