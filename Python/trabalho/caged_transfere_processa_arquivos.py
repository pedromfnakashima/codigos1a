# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:40:44 2020

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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

##########################################################################################################
##########################################################################################################
##########################################################################################################


'''
META 1
Ler um arquivo em uma pasta, csv, e salvar em outra, em csv
'''

def cgd_agrega():
    
    import glob
    import pandas as pd
    from pathlib import Path
    
    caminho_destino = caminho_wd.parent / 'csv_processados'
    
    for arq_num, arq_nome in enumerate(glob.glob('CAGEDMOV2020*.txt')):
        
        print(f'Processando {arq_nome}')
        
        dic_colunas_tipos_0 = {'competência':'string',
                               'município':pd.Int64Dtype(),
                               'cbo2002ocupação':pd.Int64Dtype(),
                               'subclasse':pd.Int64Dtype(),
                               #'classe':pd.Int64Dtype(),
                               'horascontratuais':'float64',
                               'graudeinstrução':pd.Int64Dtype(),
                               'idade':pd.Int64Dtype(),
                               'salário':'float64',
                               'saldomovimentação':pd.Int64Dtype()}
        
        dic_colunas_tipos_1 = {'Competência Declarada':'string',
                               'Município':pd.Int64Dtype(),
                               'CBO 2002 Ocupação':pd.Int64Dtype(),
                               'CNAE 2.0 Subclas':pd.Int64Dtype(),
                               'CNAE 2.0 Classe':pd.Int64Dtype(),
                               'Qtd Hora Contrat':'float64',
                               'Grau Instrução':pd.Int64Dtype(),
                               'Idade':pd.Int64Dtype(),
                               'Salário Mensal':'float64',
                               'Saldo Mov':pd.Int64Dtype()}
        
        data = pd.to_datetime(arq_nome.replace('.txt','')[-6:], format='%Y%m', errors='ignore')
        
        dic_colunas = {'Competência Declarada':'competência',
               'Município':'município',
               'CBO 2002 Ocupação':'cbo2002ocupação',
               'CNAE 2.0 Subclas':'subclasse',
               'CNAE 2.0 Classe':'classe',
               'Qtd Hora Contrat':'horascontratuais',
               'Grau Instrução':'graudeinstrução',
               'Idade':'idade',
               'Salário Mensal':'salário',
               'Saldo Mov':'saldomovimentação'}
        
        # IMPORTA DADOS
        if data.year >= 2020:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal='.', quotechar='"', skiprows=0, dtype=dic_colunas_tipos_0, na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}'])
            del dic_colunas['CNAE 2.0 Classe']
        else:
            df = pd.read_csv(arq_nome, header=0, sep=';', decimal=',', quotechar='"', skiprows=0, encoding = 'latin', dtype=dic_colunas_tipos_1, na_values = ['{ñ', '{ñ c','00000-1', '0000-1', '000-1', '{с class}'])
            df = df.rename(columns = dic_colunas)
        
        li_colunas = list(dic_colunas.values())
        
        if data.year < 2020:
            li_colunas.append('classe')
        
        df = df[li_colunas]
        
        # TRANSFERE
        # -- < ---- colocar aqui o destino
        arq_nome_semExt = arq_nome[0:-4]
        novo_nome = arq_nome_semExt + '.csv'
        df.to_csv(caminho_destino / novo_nome, sep=';', decimal=',', index=False)
        
        
        
cgd_agrega()





def cgd_agrega():
    
    import glob
    import pandas as pd
    from pathlib import Path
    
    caminho_destino = caminho_wd.parent / 'csv_processados'
    
    for arq_num, arq_nome in enumerate(glob.glob('CAGEDMOV2020*.txt')):
        print(arq_nome)

cgd_agrega()













