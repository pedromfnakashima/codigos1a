# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:38:01 2020

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
    
def processa_arquivos_zip(arquivo = 'todos', caminho = os.getcwd()):
    
    import zipfile
    import io
    from pathlib import Path
    
    print('Adicionados:')
    
    if arquivo == 'todos':
        import glob
        dicionario = {}
        
        for arq_nome in glob.glob('*.zip'):
            pos_ponto = arq_nome.find('.zip')
            df_nome = f'df_{arq_nome[0:pos_ponto]}'
            
            print(f'  {arq_nome}')
            
            dicionario[df_nome] = gera_df(arq_nome)
        
        i = 1
        for key in dicionario.keys():
            
            if i == 1:
                novo_df = dicionario[key]
            else:
                novo_df = novo_df.append(dicionario[key])
            i += 1
    else:
        novo_df = gera_df(arquivo, caminho)
        print(f'  {arquivo}')
        
    return novo_df

pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Municípios' / 'Receitas Orçamentárias'
ca2018_rec_orc = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta)

ca2018_rec_orc.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
ca2018_rec_orc = ca2018_rec_orc.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
ca2018_rec_orc = ca2018_rec_orc[ca2018_rec_orc['capital'] == True]
ca2018_rec_orc.drop(['capital'], axis=1, inplace=True)

######################################
# RECEITA LOCAL ######################
######################################

'''

RECEITAS ORIUNDAS DA ATIVIDADE ECONÔMICA

Despesa LIQUIDADA
Valor na coluna :

Valores na coluna Conta:
1.1.1.0.00.0.0 - Impostos
1.3.0.0.00.0.0 - Receita Patrimonial
1.4.0.0.00.0.0 - Receita Agropecuária
1.5.0.0.00.0.0 - Receita Industrial
1.6.0.0.00.0.0 - Receita de Serviços
1.7.1.8.01.5.0 Cota-Parte do Imposto Sobre a Propriedade Territorial Rural
1.7.1.8.06.0.0 Transferência Financeira do ICMS ¿ Desoneração ¿ L.C. Nº 87/96
1.7.2.8.01.1.0 Cota-Parte do ICMS
1.7.2.8.01.2.0 Cota-Parte do IPVA
1.7.2.8.01.3.0 Cota-Parte do IPI - Municípios
'''

dic_ifgf_autonomia = {}

########################################
# 1.1.1.0.00.0.0 - Impostos e deduções #
########################################
'''
Valores nas colunas:
Conta: 1.1.1.0.00.0.0 - Impostos
Colunas: Receitas Brutas Realizadas
Variável: imp
'''

cond1 = ca2018_rec_orc['Conta'].str.contains('1.1.1.0.00.0.0 - Impostos', case=False)
df_filtro = ca2018_rec_orc.loc[cond1, ['mun_nome', 'Valor', 'Coluna']]

#----------------------
# Receita Bruta
#----------------------

cond1 = df_filtro['Coluna'].str.contains('Receitas Brutas', case=False)
df_filtro.loc[cond1,'rb'] = df_filtro['Valor']
df_rb = df_filtro[['mun_nome', 'rb']]
df_rb.dropna(inplace=True)

#----------------------
# Deduções do Fundeb
#----------------------

cond1 = df_filtro['Coluna'].str.contains('fundeb', case=False)
df_filtro.loc[cond1,'ded_fundeb'] = df_filtro['Valor']
df_ded_fundeb = df_filtro[['mun_nome', 'ded_fundeb']]
df_ded_fundeb.dropna(inplace=True)

#---------------------------------------------
# Merge Receita Bruta com Deduções do Fundeb
#---------------------------------------------
df_rb = df_rb.merge(df_ded_fundeb, how='left', left_on='mun_nome', right_on='mun_nome')
df_rb.fillna(0, inplace=True)
df_rb['final'] = df_rb['rb'] - df_rb['ded_fundeb']

# Ordena pelo nome do município
df_rb.sort_values(by=['mun_nome'], inplace=True)

# ----------------------------------------
# Adiciona ao dicionário do IFGF
# ----------------------------------------
dic_ifgf_autonomia.update({'Impostos':df_rb[['mun_nome', 'final']]})

########################################
# 1.3.0.0.00.0.0 - Receita Patrimonial #
########################################

'''
Valores nas colunas:
Conta: 1.3.0.0.00.0.0 - Receita Patrimonial
Colunas: Receitas Brutas Realizadas
Variável: imp
'''

cond1 = ca2018_rec_orc['Conta'].str.contains('1.3.0.0.00.0.0 - Receita Patrimonial', case=False)
df_filtro = ca2018_rec_orc.loc[cond1, ['mun_nome', 'Valor', 'Coluna']]

#----------------------
# Receita Bruta
#----------------------

cond1 = df_filtro['Coluna'].str.contains('Receitas Brutas', case=False)
df_filtro.loc[cond1,'rb'] = df_filtro['Valor']
df_rb = df_filtro[['mun_nome', 'rb']]
df_rb.dropna(inplace=True)

#----------------------
# Deduções do Fundeb
#----------------------

cond1 = df_filtro['Coluna'].str.contains('fundeb', case=False)
df_filtro.loc[cond1,'ded_fundeb'] = df_filtro['Valor']
df_ded_fundeb = df_filtro[['mun_nome', 'ded_fundeb']]
df_ded_fundeb.dropna(inplace=True)

#---------------------------------------------
# Merge Receita Bruta com Deduções do Fundeb
#---------------------------------------------
df_rb = df_rb.merge(df_ded_fundeb, how='left', left_on='mun_nome', right_on='mun_nome')
df_rb.fillna(0, inplace=True)
df_rb['final'] = df_rb['rb'] - df_rb['ded_fundeb']

# Ordena pelo nome do município
df_rb.sort_values(by=['mun_nome'], inplace=True)

# ----------------------------------------
# Adiciona ao dicionário do IFGF
# ----------------------------------------
dic_ifgf_autonomia.update({'Receita Patrimonial':df_rb[['mun_nome', 'final']]})


############################################################
############################################################
##################### FAZENDO O LOOPING ####################
############################################################
############################################################

'''
RECEITAS ORIUNDAS DA ATIVIDADE ECONÔMICA

Despesa LIQUIDADA
Valor na coluna :

Valores na coluna Conta:
1.1.1.0.00.0.0 - Impostos
1.3.0.0.00.0.0 - Receita Patrimonial
1.4.0.0.00.0.0 - Receita Agropecuária
1.5.0.0.00.0.0 - Receita Industrial
1.6.0.0.00.0.0 - Receita de Serviços
1.7.1.8.01.5.0 Cota-Parte do Imposto Sobre a Propriedade Territorial Rural
1.7.1.8.06.0.0 Transferência Financeira do ICMS ¿ Desoneração ¿ L.C. Nº 87/96
1.7.2.8.01.1.0 Cota-Parte do ICMS
1.7.2.8.01.2.0 Cota-Parte do IPVA
1.7.2.8.01.3.0 Cota-Parte do IPI - Municípios
'''

import pandas as pd

df_colunas = pd.DataFrame(columns=['Coluna','DicEntrada'])


nova_linha = {'Coluna':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}


linha1 = pd.Series({'Coluna':'1.1.1.0.00.0.0 - Impostos', 'DicEntrada':'impostos'}).to_frame()
linha2 = pd.Series({'Coluna':'1.3.0.0.00.0.0 - Receita Patrimonial', 'DicEntrada':'recPat'}).to_frame()


df_colunas = pd.DataFrame(linha1, linha1)







import pandas as pd

data = {'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
	'physics': [68, 74, 77, 78],
	'chemistry': [84, 56, 73, 69],
	'algebra': [78, 88, 82, 87]}

	
#create dataframe
df_marks = pd.DataFrame(data)
print('Original DataFrame\n------------------')
print(df_marks)

new_row = {'name':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}
#append row to the dataframe






















cond1 = ca2018_rec_orc['Conta'].str.contains('1.1.1.0.00.0.0 - Impostos', case=False)
str1 = '1.1.1.0.00.0.0 - Impostos'
str_entrada_dic = str1[str1.find('-') + 2:]











# gd: Gera Dados
def gd_ifgfAutonomia():
    










dic_ifgf_autonomia = {}

########################################
# 1.1.1.0.00.0.0 - Impostos e deduções #
########################################
'''
Valores nas colunas:
Conta: 1.1.1.0.00.0.0 - Impostos
Colunas: Receitas Brutas Realizadas
Variável: imp
'''

cond1 = ca2018_rec_orc['Conta'].str.contains('1.1.1.0.00.0.0 - Impostos', case=False)
df_filtro = ca2018_rec_orc.loc[cond1, ['mun_nome', 'Valor', 'Coluna']]

#----------------------
# Receita Bruta
#----------------------

cond1 = df_filtro['Coluna'].str.contains('Receitas Brutas', case=False)
df_filtro.loc[cond1,'rb'] = df_filtro['Valor']
df_rb = df_filtro[['mun_nome', 'rb']]
df_rb.dropna(inplace=True)

#----------------------
# Deduções do Fundeb
#----------------------

cond1 = df_filtro['Coluna'].str.contains('fundeb', case=False)
df_filtro.loc[cond1,'ded_fundeb'] = df_filtro['Valor']
df_ded_fundeb = df_filtro[['mun_nome', 'ded_fundeb']]
df_ded_fundeb.dropna(inplace=True)

#---------------------------------------------
# Merge Receita Bruta com Deduções do Fundeb
#---------------------------------------------
df_rb = df_rb.merge(df_ded_fundeb, how='left', left_on='mun_nome', right_on='mun_nome')
df_rb.fillna(0, inplace=True)
df_rb['final'] = df_rb['rb'] - df_rb['ded_fundeb']

# Ordena pelo nome do município
df_rb.sort_values(by=['mun_nome'], inplace=True)

# ----------------------------------------
# Adiciona ao dicionário do IFGF
# ----------------------------------------
dic_ifgf_autonomia.update({'Impostos':df_rb[['mun_nome', 'final']]})






































