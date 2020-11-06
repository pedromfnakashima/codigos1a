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

############ RECEITAS ORÇAMENTÁRIAS
pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Municípios' / 'Receitas Orçamentárias'
ca2018_rec_orc = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta)

ca2018_rec_orc.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
ca2018_rec_orc = ca2018_rec_orc.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
ca2018_rec_orc = ca2018_rec_orc[ca2018_rec_orc['capital'] == True]
ca2018_rec_orc.drop(['capital'], axis=1, inplace=True)


############# DESPESAS POR FUNÇÃO
pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Municípios' / 'Despesas por Função'
ca2018_desp_função = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta)

ca2018_desp_função.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
ca2018_desp_função = ca2018_desp_função.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
ca2018_desp_função = ca2018_desp_função[ca2018_desp_função['capital'] == True]
ca2018_desp_função.drop(['capital'], axis=1, inplace=True)


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
######## RECEITAS ORIUNDAS DA ATIVIDADE ECONÔMICA  #########
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

# gd: Gera Dados


def gd_ifgfAutonomiaRec(df_input):
    
    import pandas as pd
    
    df_colunas = pd.DataFrame(columns=['colCod', 'colDesc','dicEntrada'])
    linha1 = {'colCod':'1.1.1.0.00.0.0', 'colDesc':'Impostos', 'dicEntrada':'impostos'}
    linha2 = {'colCod':'1.3.0.0.00.0.0', 'colDesc':'Receita Patrimonial', 'dicEntrada':'recPatr'}
    linha3 = {'colCod':'1.4.0.0.00.0.0', 'colDesc':'Receita Agropecuária', 'dicEntrada':'recAgro'}
    linha4 = {'colCod':'1.6.0.0.00.0.0', 'colDesc':'Receita de Serviços', 'dicEntrada':'recServ'}
    linha5 = {'colCod':'1.7.1.8.01.5.0', 'colDesc':'Cota-Parte do Imposto Sobre a Propriedade Territorial Rural', 'dicEntrada':'recCPipi'}
    linha6 = {'colCod':'1.7.1.8.06.0.0', 'colDesc':'Transferência Financeira do ICMS ¿ Desoneração ¿ L.C. Nº 87/96', 'dicEntrada':'transfCompLeiKandir'}
    linha7 = {'colCod':'1.7.2.8.01.1.0', 'colDesc':'Cota-Parte do ICMS', 'dicEntrada':'recCPicms'}
    linha8 = {'colCod':'1.7.2.8.01.2.0', 'colDesc':'Cota-Parte do IPVA', 'dicEntrada':'recCPipva'}
    linha9 = {'colCod':'1.7.2.8.01.3.0', 'colDesc':'Cota-Parte do IPI - Municípios', 'dicEntrada':'recCPipiMun'}
    
    df_colunas = df_colunas.append(linha1, ignore_index=True)
    df_colunas = df_colunas.append(linha2, ignore_index=True)
    df_colunas = df_colunas.append(linha3, ignore_index=True)
    df_colunas = df_colunas.append(linha4, ignore_index=True)
    df_colunas = df_colunas.append(linha5, ignore_index=True)
    df_colunas = df_colunas.append(linha6, ignore_index=True)
    df_colunas = df_colunas.append(linha7, ignore_index=True)
    df_colunas = df_colunas.append(linha8, ignore_index=True)
    df_colunas = df_colunas.append(linha9, ignore_index=True)
    
    #del linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9
    
    #dic_ifgf_autonomia = {}
    pasta = caminho_wd = caminho_base / 'Dados'
    capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})
    capitais.sort_values(['mun_nome'], inplace=True)
    
    for index, linha in df_colunas.iterrows():
        #print(linha['colCod'])
        #print(linha['dicEntrada'])
        codigo = linha['colCod']
        dicEntrada = linha['dicEntrada']
        
        cond1 = df_input['Conta'].str.contains(codigo, case=False)
        df_filtro = df_input.loc[cond1, ['mun_nome', 'Valor', 'Coluna']]
        
        cond1 = df_filtro['Coluna'].str.contains('Receitas Brutas', case=False)
        df_filtro.loc[cond1,'rb'] = df_filtro['Valor']
        df_rb = df_filtro[['mun_nome', 'rb']]
        df_rb.dropna(inplace=True)
        
        cond1 = df_filtro['Coluna'].str.contains('fundeb', case=False)
        df_filtro.loc[cond1,'ded_fundeb'] = df_filtro['Valor']
        df_ded_fundeb = df_filtro[['mun_nome', 'ded_fundeb']]
        df_ded_fundeb.dropna(inplace=True)
        
        df_rb = df_rb.merge(df_ded_fundeb, how='left', left_on='mun_nome', right_on='mun_nome')
        df_rb.fillna(0, inplace=True)
        df_rb['subtração'] = df_rb['rb'] - df_rb['ded_fundeb']
        
        # Ordena pelo nome do município
        df_rb.sort_values(by=['mun_nome'], inplace=True)
        df_rb = df_rb[['mun_nome', 'subtração']]
        df_rb.rename(columns={'subtração':dicEntrada}, inplace=True)
        
        # ----------------------------------------
        # Adiciona ao df capitais
        # ----------------------------------------
        
        capitais = capitais.merge(df_rb, how='left', left_on='mun_nome', right_on='mun_nome')
   
    capitais.drop(['mun_cod_ibge'], axis=1, inplace=True)
    capitais.set_index('mun_nome', inplace=True)
    capitais.fillna(0, inplace=True)
    capitais['recAtivEcon'] = capitais.sum(axis=1)
    capitais = capitais['recAtivEcon'].to_frame()
   
    return capitais


df_ifgf_autonomia_receitas = gd_ifgfAutonomiaRec(ca2018_rec_orc)


############################################################
############################################################
##################### FAZENDO O LOOPING ####################
######## CUSTOS COM A ESTRUTURA ADMINISTRATIVA  ############
############################################################

'''
Conta:
01 - Legislativa
02 - Judiciária
03 - Essencial à Justiça
04 - Administração

'''

def gd_ifgfAutonomiaDesp(df_input):
    
    import pandas as pd
    import numpy as np
    
    df_colunas = pd.DataFrame(columns=['colCod', 'dicEntrada'])
    linha1 = {'colCod':'01 - Legislativa', 'dicEntrada':'fLeg'}
    linha2 = {'colCod':'02 - Judiciária', 'dicEntrada':'fJud'}
    linha3 = {'colCod':'03 - Essencial à Justiça', 'dicEntrada':'fEssJud'}
    linha4 = {'colCod':'04 - Administração', 'dicEntrada':'fAdmin'}
    
    df_colunas = df_colunas.append(linha1, ignore_index=True)
    df_colunas = df_colunas.append(linha2, ignore_index=True)
    df_colunas = df_colunas.append(linha3, ignore_index=True)
    df_colunas = df_colunas.append(linha4, ignore_index=True)
    
    pasta = caminho_wd = caminho_base / 'Dados'
    capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})
    capitais.sort_values(['mun_nome'], inplace=True)
    
    for index, linha in df_colunas.iterrows():

        codigo = linha['colCod']
        dicEntrada = linha['dicEntrada']
        
        cond1 = df_input['Conta'].str.contains(codigo, case=False)
        cond2 = df_input['Coluna'].str.contains('Despesas Liquidadas', case=False)
        df_filtro = ca2018_desp_função.loc[cond1 & cond2, ['mun_nome', 'Valor']]

        df_filtro.rename(columns={'Valor':codigo}, inplace=True)
        
        # Adiciona ao df capitais
        capitais = capitais.merge(df_filtro, how='left', left_on='mun_nome', right_on='mun_nome')

   
    capitais.drop(['mun_cod_ibge'], axis=1, inplace=True)
    capitais.set_index('mun_nome', inplace=True)
    capitais.fillna(0, inplace=True)
    capitais['despEstAdm'] = capitais.sum(axis=1)
    capitais = capitais['despEstAdm'].to_frame()
   
    return capitais


df_ifgf_autonomia_despesas = gd_ifgfAutonomiaDesp(ca2018_desp_função)

##############################################################
##############################################################
# RECEITA CORRENTE LÍQUIDA ###################################
##############################################################
##############################################################

def df_ifgf_rcl():
    
    import pandas as pd
    import numpy as np
    pasta = caminho_wd = caminho_base / 'Dados'
    municipios = pd.read_excel(pasta / 'municipios.xlsx', sheet_name='municipios', skiprows=0, dtype={'capital': np.bool})
    capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})
    
    
    pasta = caminho_base / 'Dados' / 'Siconfi' / 'RGF - Municípios' / 'Anexo 01 - Demonstrativo da Despesa Com Pessoal' / 'DTP e Apuração do Cumprimento do Limite Legal'
    rgf2018q3_apuracao = processa_arquivos_zip(arquivo='2018q3.zip',
                                               caminho=pasta)
    
    rgf2018q3_apuracao.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
    rgf2018q3_apuracao = rgf2018q3_apuracao.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
    rgf2018q3_apuracao = rgf2018q3_apuracao[rgf2018q3_apuracao['capital'] == True]
    rgf2018q3_apuracao.drop(['capital'], axis=1, inplace=True)
    
    
    cond1 = rgf2018q3_apuracao['Conta'].str.contains('receita corrente líquida', case=False)
    #cond2 = ca2018_desp_função['Coluna'].str.contains('Despesas Liquidadas', case=False)
    df_filtro = rgf2018q3_apuracao.loc[cond1, ['mun_nome', 'Conta', 'Coluna', 'Valor']]
    df_filtro = df_filtro.groupby(['mun_nome']).first()
    df_filtro = df_filtro[['Valor']]
    df_filtro.rename(columns={'Valor':'RCL'}, inplace=True)
    
    
    capitais = capitais.merge(df_filtro, how='left', left_on='mun_nome', right_on='mun_nome')
    capitais.drop(['mun_cod_ibge'], axis=1, inplace=True)
    capitais.set_index('mun_nome', inplace=True)
    
    return capitais


df_ifgf_rcl = df_ifgf_rcl()

############################################################
########################### MERGE ##########################
######## RECEITAS ORIUNDAS DA ATIVIDADE ECONÔMICA  #########
######## CUSTOS COM A ESTRUTURA ADMINISTRATIVA  ############
############# RECEITA CORRENTE LÍQUIDA #####################
############################################################

df_ifgf_autonomia_receitas
df_ifgf_autonomia_despesas

df_ifgf_autonomia = df_ifgf_autonomia_receitas.merge(df_ifgf_autonomia_despesas, how='left', left_index=True, right_index=True)
df_ifgf_autonomia = df_ifgf_autonomia.merge(df_ifgf_rcl, how='left', left_index=True, right_index=True)

print(df_ifgf_autonomia.columns)

df_ifgf_autonomia['indicador'] = (df_ifgf_autonomia['recAtivEcon'] - df_ifgf_autonomia['despEstAdm']) / df_ifgf_autonomia['RCL']

cond1 = df_ifgf_autonomia['indicador'] > 0.25
df_ifgf_autonomia.loc[cond1, 'nota'] = 1

cond1 = df_ifgf_autonomia['indicador'] < 0
df_ifgf_autonomia.loc[cond1, 'nota'] = 0

cond1 = df_ifgf_autonomia['indicador'] < 0.25
cond2 = df_ifgf_autonomia['indicador'] > 0
df_ifgf_autonomia.loc[cond1 & cond2, 'nota'] = df_ifgf_autonomia['indicador'] / 0.25






############################################################
######################## RASCUNHOS #########################
############################################################











##############################################################
# CUSTOS COM A ESTRUTURA ADMINISTRATIVA ######################
##############################################################
import pandas as pd
import numpy as np
pasta = caminho_wd = caminho_base / 'Dados'
municipios = pd.read_excel(pasta / 'municipios.xlsx', sheet_name='municipios', skiprows=0, dtype={'capital': np.bool})


pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Municípios' / 'Despesas por Função'
ca2018_desp_função = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta)

ca2018_desp_função.rename(columns={'Cod.IBGE':'mun_cod_ibge'}, inplace=True)
ca2018_desp_função = ca2018_desp_função.merge(municipios, how='left', left_on='mun_cod_ibge', right_on='mun_cod_ibge')
ca2018_desp_função = ca2018_desp_função[ca2018_desp_função['capital'] == True]
ca2018_desp_função.drop(['capital'], axis=1, inplace=True)

cond1 = ca2018_desp_função['Conta'].str.contains('01 - Legislativa', case=False)
cond2 = ca2018_desp_função['Coluna'].str.contains('Despesas Liquidadas', case=False)
df_filtro = ca2018_desp_função.loc[cond1 & cond2, ['mun_nome', 'Valor']]

df_filtro.rename(columns={'Valor':'fLeg'}, inplace=True)

pasta = caminho_wd = caminho_base / 'Dados'
capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})
capitais.sort_values(['mun_nome'], inplace=True)

capitais = capitais.merge(df_filtro, how='left', left_on='mun_nome', right_on='mun_nome')






'''
Conta:
01 - Legislativa
02 - Judiciária
03 - Essencial à Justiça
04 - Administração

'''














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
df_rb['subtração'] = df_rb['rb'] - df_rb['ded_fundeb']

# Ordena pelo nome do município
df_rb.sort_values(by=['mun_nome'], inplace=True)
df_rb = df_rb[['mun_nome', 'subtração']]
df_rb.rename(columns={'subtração':'impostos'}, inplace=True)

# ----------------------------------------
# Adiciona ao df capitais
# ----------------------------------------

capitais = capitais.merge(df_rb, how='left', left_on='mun_nome', right_on='mun_nome')

# ----------------------------------------
# Adiciona ao dicionário do IFGF
# ----------------------------------------
dic_ifgf_autonomia.update({'Impostos':df_rb[['mun_nome', 'final']]})



pasta = caminho_wd = caminho_base / 'Dados'
capitais = pd.read_excel(pasta / 'capitais.xlsx', sheet_name='capitais', skiprows=0, dtype={'capital': np.bool})


capitais = capitais.merge(df_rb, how='left', left_on='mun_nome', right_on='mun_nome')



































