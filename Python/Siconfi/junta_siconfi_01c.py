# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:13:14 2020

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
caminho_wd = caminho_base / 'Dados' / 'Firjan'
os.chdir(caminho_wd)
##########################################################################################################
##########################################################################################################
##########################################################################################################
import numpy as np
import pandas as pd

#pasta = caminho_wd = caminho_base / 'Dados'
#municipios = pd.read_excel(pasta / 'municipios.xlsx', sheet_name='municipios', skiprows=0, dtype={'capital': np.bool})
#capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})


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
        #df[periodo_unidade] = int(periodo_num)
        df['periodo'] = int(periodo_num)
        ########################################
        # ADICIONA O MÊS ONDE, EM Coluna, HÁ MR
        ########################################
        # VERIFICA SE HÁ O TERMO MR EM Coluna
        cond = df['Coluna'].str.contains('MR', case=True)
        soma = cond.sum()
        if soma > 0:
            # SE É RREO (PERIODICIDADE bimestre):
            if periodo_unidade == 'bimestre':
                range_max = 7
                multiplicador = 2
            # SE É RGF (PERIODICIDADE quadrimestre):
            elif periodo_unidade == 'quadrimestre':
                range_max = 4
                multiplicador = 4
            # GERA A COLUNA MÊS (ONDE EM Coluna HÁ O TERMO MR)
            for num_per in list(range(1,range_max)):
                cond = df['periodo'] == num_per
                df.loc[cond, 'mes_final_periodo'] = num_per * multiplicador
            df.rename(columns={'exercicio':'year','mes_final_periodo':'month'}, inplace=True)
            df['day'] = 1
            df['data_inicio_periodo'] = pd.to_datetime(df[['year', 'month', 'day']])
            df.rename(columns={'year':'exercicio'}, inplace=True)
            df.drop(['month','day'],axis=1,inplace=True)
            cond = df['Coluna'] == '<MR>'
            df.loc[cond, 'mês'] = df['data_inicio_periodo']
            for num in list(range(1,12)):
                str1 = f'<MR-{num}>'
                cond = df['Coluna'] == str1
                df.loc[cond, 'mês'] = df['data_inicio_periodo'] - pd.DateOffset(months=num)
            del df['data_inicio_periodo']
            # fim
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
