# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:38:18 2020

@author: pedro-salj
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:25:03 2020

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
caminho_wd = caminho_base / 'Dados' / 'cnae e ncm'
os.chdir(caminho_wd)

######################################################################################
# CNAE 2.3 ###########################################################################
######################################################################################



import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae = pd.read_excel('CNAE23_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

cnae.rename(mapper={'Unnamed: 5':'Descrição'},axis=1,inplace=True)

# Cria coluna com a versão
cnae['Versão'] = '2.3'

# Preenche para baixo
cnae['Seção'].fillna(method='ffill', inplace=True)
cnae['Divisão'].fillna(method='ffill', inplace=True)
cnae['Grupo'].fillna(method='ffill', inplace=True)
cnae['Classe'].fillna(method='ffill', inplace=True)

# Tira pontuação dos códigos
cnae['Subclasse'] = cnae['Subclasse'].str.replace('-','').str.replace('/','')
cnae['Classe'] = cnae['Classe'].str.replace('.','').str.replace('-','')
cnae['Grupo'] = cnae['Grupo'].str.replace('.','')
cnae['Descrição'] = cnae['Descrição'].str.replace('\n',' ')

# Tira os espaços antes e depois dos códigos
cnae['Seção'] = cnae['Seção'].str.strip()
cnae['Divisão'] = cnae['Divisão'].str.strip()
cnae['Grupo'] = cnae['Grupo'].str.strip()
cnae['Classe'] = cnae['Classe'].str.strip()
cnae['Subclasse'] = cnae['Subclasse'].str.strip()

# CORRESPONDÊNCIA
cnae_corresp = cnae.copy()
cond1 = ~ cnae_corresp['Subclasse'].isnull()
cnae_corresp = cnae_corresp.loc[cond1,:]
# Adiciona linha: Subclasse 9999999 - "Não identificado"
dic_novalinha = {'Seção': ['Z'], 'Divisão': ['99'], 'Grupo':['999'], 'Classe':['99999'], 'Subclasse':['9999999'], 'Descrição':['Não Identificado']}
nova_linha = pd.DataFrame.from_dict(dic_novalinha)
cnae_corresp = cnae_corresp.append(nova_linha)

# SUBCLASSE - DESCRIÇÃO
cnae_Subclasse = cnae_corresp.copy()
cnae_corresp.drop(['Descrição'],axis=1,inplace=True)
cnae_Subclasse = cnae_Subclasse.loc[:,['Subclasse','Descrição','Versão']]

# CLASSE - DESCRIÇÃO
cnae_Classe = cnae[['Classe', 'Descrição', 'Versão']]
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').head(1)
# Adiciona linha: Subclasse 9999999 - "Não identificado"
dic_novalinha = {'Classe': ['99999'], 'Descrição': ['Não Identificado']}
nova_linha = pd.DataFrame.from_dict(dic_novalinha)
cnae_Classe = cnae_Classe.append(nova_linha)

# GRUPO - DESCRIÇÃO
cnae_Grupo = cnae[['Grupo', 'Descrição', 'Versão']]
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').head(1)
# Adiciona linha: Subclasse 9999999 - "Não identificado"
dic_novalinha = {'Grupo': ['999'], 'Descrição': ['Não Identificado']}
nova_linha = pd.DataFrame.from_dict(dic_novalinha)
cnae_Grupo = cnae_Grupo.append(nova_linha)

# DIVISÃO - DESCRIÇÃO
cnae_Divisão = cnae[['Divisão', 'Descrição', 'Versão']]
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').head(1)
# Adiciona linha: Subclasse 9999999 - "Não identificado"
dic_novalinha = {'Divisão': ['99'], 'Descrição': ['NÃO IDENTIFICADO']}
nova_linha = pd.DataFrame.from_dict(dic_novalinha)
cnae_Divisão = cnae_Divisão.append(nova_linha)

# SEÇÃO - DESCRIÇÃO
cnae_Seção = cnae[['Seção', 'Descrição', 'Versão']]
cnae_Seção = cnae_Seção.groupby('Seção').head(1)
# Adiciona linha: Subclasse 9999999 - "Não identificado"
dic_novalinha = {'Seção': ['Z'], 'Descrição': ['NÃO IDENTIFICADO']}
nova_linha = pd.DataFrame.from_dict(dic_novalinha)
cnae_Seção = cnae_Seção.append(nova_linha)

# Coloca nos DFs completos
cnae_corresp_completo = cnae_corresp.copy()
cnae_Subclasse_completo = cnae_Subclasse.copy()
cnae_Classe_completo = cnae_Classe.copy()
cnae_Grupo_completo = cnae_Grupo.copy()
cnae_Divisão_completo = cnae_Divisão.copy()
cnae_Seção_completo = cnae_Seção.copy()

######################################################################################
# CNAE 2.2 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae = pd.read_excel('CNAE22_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

#print(cnae.dtypes)
cnae.drop(['Unnamed: 0'],axis=1,inplace=True)
cnae.rename(mapper={'Unnamed: 1':'Seção','Unnamed: 2':'Divisão','Unnamed: 3':'Grupo','Unnamed: 4':'Classe','Unnamed: 5':'Subclasse','Denominação':'Descrição'},axis=1,inplace=True)
cnae.drop([0],axis=0,inplace=True)

# Deleta linhas lixo
cond1 = ~ cnae['Seção'].str.contains('continuação', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('2.2', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('2.0', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('Seção', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('conclusão', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cnae = cnae.iloc[:-2] # deleta últimas duas linhas

# Cria coluna com a versão
cnae['Versão'] = '2.2'

# Preenche para baixo
cnae['Seção'].fillna(method='ffill', inplace=True)
cnae['Divisão'].fillna(method='ffill', inplace=True)
cnae['Grupo'].fillna(method='ffill', inplace=True)
cnae['Classe'].fillna(method='ffill', inplace=True)

# Tira pontuação dos códigos
cnae['Subclasse'] = cnae['Subclasse'].str.replace('-','').str.replace('/','')
cnae['Classe'] = cnae['Classe'].str.replace('.','').str.replace('-','')
cnae['Grupo'] = cnae['Grupo'].str.replace('.','')
cnae['Descrição'] = cnae['Descrição'].str.replace('\n',' ')

# Tira os espaços antes e depois dos códigos
cnae['Seção'] = cnae['Seção'].str.strip()
cnae['Divisão'] = cnae['Divisão'].str.strip()
cnae['Grupo'] = cnae['Grupo'].str.strip()
cnae['Classe'] = cnae['Classe'].str.strip()
cnae['Subclasse'] = cnae['Subclasse'].str.strip()

# CORRESPONDÊNCIA
cnae_corresp = cnae.copy()
cond1 = ~ cnae_corresp['Subclasse'].isnull()
cnae_corresp = cnae_corresp.loc[cond1,:]

# SUBCLASSE - DESCRIÇÃO
cnae_Subclasse = cnae_corresp.copy()
cnae_corresp.drop(['Descrição'],axis=1,inplace=True)
cnae_Subclasse = cnae_Subclasse.loc[:,['Subclasse','Descrição','Versão']]

# CLASSE - DESCRIÇÃO
cnae_Classe = cnae[['Classe', 'Descrição', 'Versão']]
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').head(1)

# GRUPO - DESCRIÇÃO
cnae_Grupo = cnae[['Grupo', 'Descrição', 'Versão']]
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').head(1)

# DIVISÃO - DESCRIÇÃO
cnae_Divisão = cnae[['Divisão', 'Descrição', 'Versão']]
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').head(1)

# SEÇÃO - DESCRIÇÃO
cnae_Seção = cnae[['Seção', 'Descrição', 'Versão']]
cnae_Seção = cnae_Seção.groupby('Seção').head(1)

# Coloca nos DFs completos
cnae_corresp_completo = cnae_corresp_completo.append(cnae_corresp)
cnae_Subclasse_completo = cnae_Subclasse_completo.append(cnae_Subclasse)
cnae_Classe_completo = cnae_Classe_completo.append(cnae_Classe)
cnae_Grupo_completo = cnae_Grupo_completo.append(cnae_Grupo)
cnae_Divisão_completo = cnae_Divisão_completo.append(cnae_Divisão)
cnae_Seção_completo = cnae_Seção_completo.append(cnae_Seção)


######################################################################################
# CNAE 2.1 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae = pd.read_excel('CNAE21_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

#print(cnae.dtypes)
cnae.drop(['Unnamed: 0'],axis=1,inplace=True)
cnae.rename(mapper={'código CNAE 2.0':'Seção','Unnamed: 2':'Divisão','Unnamed: 3':'Grupo','Unnamed: 4':'Classe','Unnamed: 5':'Subclasse','Denominação':'Descrição'},axis=1,inplace=True)
cnae.drop([0],axis=0,inplace=True)

# Deleta linhas lixo
cond1 = ~ cnae['Seção'].str.contains('continuação', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('2.2', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('2.0', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('Seção', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('conclusão', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cnae = cnae.iloc[:-2] # deleta últimas duas linhas

# Cria coluna com a versão
cnae['Versão'] = '2.1'

# Preenche para baixo
cnae['Seção'].fillna(method='ffill', inplace=True)
cnae['Divisão'].fillna(method='ffill', inplace=True)
cnae['Grupo'].fillna(method='ffill', inplace=True)
cnae['Classe'].fillna(method='ffill', inplace=True)

# Tira pontuação dos códigos
cnae['Subclasse'] = cnae['Subclasse'].str.replace('-','').str.replace('/','')
cnae['Classe'] = cnae['Classe'].str.replace('.','').str.replace('-','')
cnae['Grupo'] = cnae['Grupo'].str.replace('.','')
cnae['Descrição'] = cnae['Descrição'].str.replace('\n',' ')

# Tira os espaços antes e depois dos códigos
cnae['Seção'] = cnae['Seção'].str.strip()
cnae['Divisão'] = cnae['Divisão'].str.strip()
cnae['Grupo'] = cnae['Grupo'].str.strip()
cnae['Classe'] = cnae['Classe'].str.strip()
cnae['Subclasse'] = cnae['Subclasse'].str.strip()

# CORRESPONDÊNCIA
cnae_corresp = cnae.copy()
cond1 = ~ cnae_corresp['Subclasse'].isnull()
cnae_corresp = cnae_corresp.loc[cond1,:]

# SUBCLASSE - DESCRIÇÃO
cnae_Subclasse = cnae_corresp.copy()
cnae_corresp.drop(['Descrição'],axis=1,inplace=True)
cnae_Subclasse = cnae_Subclasse.loc[:,['Subclasse','Descrição','Versão']]

# CLASSE - DESCRIÇÃO
cnae_Classe = cnae[['Classe', 'Descrição', 'Versão']]
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').head(1)

# GRUPO - DESCRIÇÃO
cnae_Grupo = cnae[['Grupo', 'Descrição', 'Versão']]
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').head(1)

# DIVISÃO - DESCRIÇÃO
cnae_Divisão = cnae[['Divisão', 'Descrição', 'Versão']]
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').head(1)

# SEÇÃO - DESCRIÇÃO
cnae_Seção = cnae[['Seção', 'Descrição', 'Versão']]
cnae_Seção = cnae_Seção.groupby('Seção').head(1)

# Coloca nos DFs completos
cnae_corresp_completo = cnae_corresp_completo.append(cnae_corresp)
cnae_Subclasse_completo = cnae_Subclasse_completo.append(cnae_Subclasse)
cnae_Classe_completo = cnae_Classe_completo.append(cnae_Classe)
cnae_Grupo_completo = cnae_Grupo_completo.append(cnae_Grupo)
cnae_Divisão_completo = cnae_Divisão_completo.append(cnae_Divisão)
cnae_Seção_completo = cnae_Seção_completo.append(cnae_Seção)

######################################################################################
# CNAE 2.0 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae = pd.read_excel('CNAE20_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

#print(cnae.dtypes)
cnae.drop(['Unnamed: 0'],axis=1,inplace=True)
cnae.rename(mapper={'código CNAE 2.0':'Seção','Unnamed: 2':'Divisão','Unnamed: 3':'Grupo','Unnamed: 4':'Classe','Unnamed: 5':'Subclasse','Denominação':'Descrição'},axis=1,inplace=True)
cnae.drop([0],axis=0,inplace=True)

# Deleta linhas lixo
cond1 = ~ cnae['Seção'].str.contains('continuação', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('2.2', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('2.0', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('Seção', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cond1 = ~ cnae['Seção'].str.contains('conclusão', regex=False, na=False)
cnae = cnae.loc[cond1,:]
cnae = cnae.iloc[:-2] # deleta últimas duas linhas

# Cria coluna com a versão
cnae['Versão'] = '2.0'

# Preenche para baixo
cnae['Seção'].fillna(method='ffill', inplace=True)
cnae['Divisão'].fillna(method='ffill', inplace=True)
cnae['Grupo'].fillna(method='ffill', inplace=True)
cnae['Classe'].fillna(method='ffill', inplace=True)

# Tira pontuação dos códigos
cnae['Subclasse'] = cnae['Subclasse'].str.replace('-','').str.replace('/','')
cnae['Classe'] = cnae['Classe'].str.replace('.','').str.replace('-','')
cnae['Grupo'] = cnae['Grupo'].str.replace('.','')
cnae['Descrição'] = cnae['Descrição'].str.replace('\n',' ')

# Tira os espaços antes e depois dos códigos
cnae['Seção'] = cnae['Seção'].str.strip()
cnae['Divisão'] = cnae['Divisão'].str.strip()
cnae['Grupo'] = cnae['Grupo'].str.strip()
cnae['Classe'] = cnae['Classe'].str.strip()
cnae['Subclasse'] = cnae['Subclasse'].str.strip()

# CORRESPONDÊNCIA
cnae_corresp = cnae.copy()
cond1 = ~ cnae_corresp['Subclasse'].isnull()
cnae_corresp = cnae_corresp.loc[cond1,:]

# SUBCLASSE - DESCRIÇÃO
cnae_Subclasse = cnae_corresp.copy()
cnae_corresp.drop(['Descrição'],axis=1,inplace=True)
cnae_Subclasse = cnae_Subclasse.loc[:,['Subclasse','Descrição','Versão']]

# CLASSE - DESCRIÇÃO
cnae_Classe = cnae[['Classe', 'Descrição', 'Versão']]
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').head(1)

# GRUPO - DESCRIÇÃO
cnae_Grupo = cnae[['Grupo', 'Descrição', 'Versão']]
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').head(1)

# DIVISÃO - DESCRIÇÃO
cnae_Divisão = cnae[['Divisão', 'Descrição', 'Versão']]
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').head(1)

# SEÇÃO - DESCRIÇÃO
cnae_Seção = cnae[['Seção', 'Descrição', 'Versão']]
cnae_Seção = cnae_Seção.groupby('Seção').head(1)

# Coloca nos DFs completos
cnae_corresp_completo = cnae_corresp_completo.append(cnae_corresp)
cnae_Subclasse_completo = cnae_Subclasse_completo.append(cnae_Subclasse)
cnae_Classe_completo = cnae_Classe_completo.append(cnae_Classe)
cnae_Grupo_completo = cnae_Grupo_completo.append(cnae_Grupo)
cnae_Divisão_completo = cnae_Divisão_completo.append(cnae_Divisão)
cnae_Seção_completo = cnae_Seção_completo.append(cnae_Seção)

## --------------------------------------------------------------- ##
## ------------------ PEGA A PRIMEIRA SUBCLASSE ------------------ ##
## --------------------------------------------------------------- ##

cnae_corresp_completo = cnae_corresp_completo.groupby(['Subclasse']).head(1)
cnae_Subclasse_completo = cnae_Subclasse_completo.groupby(['Subclasse']).head(1)
cnae_Classe_completo = cnae_Classe_completo.groupby(['Classe']).head(1)
cnae_Grupo_completo = cnae_Grupo_completo.groupby(['Grupo']).head(1)
cnae_Divisão_completo = cnae_Divisão_completo.groupby(['Divisão']).head(1)
cnae_Seção_completo = cnae_Seção_completo.groupby(['Seção']).head(1)

## --------------------------------------------------------------- ##
## -------------------------- RENOMEIA --------------------------- ##
## --------------------------------------------------------------- ##
mapper = {'Seção':'cnae_seção_cod','Divisão':'cnae_divisão_cod','Grupo':'cnae_grupo_cod','Classe':'cnae_classe_cod','Subclasse':'cnae_subclasse_cod'}
cnae_corresp_completo.rename(mapper=mapper,axis=1,inplace=True)
cnae_Subclasse_completo.rename(mapper=mapper,axis=1,inplace=True)
cnae_Classe_completo.rename(mapper=mapper,axis=1,inplace=True)
cnae_Grupo_completo.rename(mapper=mapper,axis=1,inplace=True)
cnae_Divisão_completo.rename(mapper=mapper,axis=1,inplace=True)
cnae_Seção_completo.rename(mapper=mapper,axis=1,inplace=True)

mapperSubclasse = {'Descrição':'cnae_subclasse_desc'}
mapperClasse = {'Descrição':'cnae_classe_desc'}
mapperGrupo = {'Descrição':'cnae_grupo_desc'}
mapperDivisão = {'Descrição':'cnae_divisão_desc'}
mapperSeção = {'Descrição':'cnae_seção_desc'}
cnae_Subclasse_completo.rename(mapper=mapperSubclasse,axis=1,inplace=True)
cnae_Classe_completo.rename(mapper=mapperClasse,axis=1,inplace=True)
cnae_Grupo_completo.rename(mapper=mapperGrupo,axis=1,inplace=True)
cnae_Divisão_completo.rename(mapper=mapperDivisão,axis=1,inplace=True)
cnae_Seção_completo.rename(mapper=mapperSeção,axis=1,inplace=True)

## --------------------------------------------------------------- ##
## --------------------- EXPORTA PARA CSV ------------------------ ##
## --------------------------------------------------------------- ##

cnae_corresp_completo.to_csv('cnae_corresp.csv', sep='|', decimal=',', index=False)
cnae_Subclasse_completo.to_csv('cnae_subclasse_desc.csv', sep='|', decimal=',', index=False)
cnae_Classe_completo.to_csv('cnae_classe_desc.csv', sep='|', decimal=',', index=False)
cnae_Grupo_completo.to_csv('cnae_grupo_desc.csv', sep='|', decimal=',', index=False)
cnae_Divisão_completo.to_csv('cnae_divisão_desc.csv', sep='|', decimal=',', index=False)
cnae_Seção_completo.to_csv('cnae_seção_desc.csv', sep='|', decimal=',', index=False)





## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##



mapper = {'Seção':'cnae_seção_cod','Divisão':'cnae_divisão_cod','Grupo':'cnae_grupo_cod','Classe':'cnae_classe_cod', 'Subclasse':'cnae_subclasse_cod'}


cnae_corresp = cnae_corresp23.copy()
#cnae_corresp = cnae_corresp.append(cnae_corresp22)
#cnae_corresp = cnae_corresp.append(cnae_corresp21)
#cnae_corresp = cnae_corresp.append(cnae_corresp20)
cnae_corresp.reset_index(inplace=True)
cnae_corresp = cnae_corresp.groupby(['Subclasse']).head(1)

cnae_corresp.rename(mapper=mapper,axis=1,inplace=True)
# Exporta para csv
cnae_corresp.to_csv('cnae_corresp_curto.csv', sep=';', decimal=',', index=False)

## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##

cnae_corresp = cnae_corresp23.copy()
cnae_corresp = cnae_corresp.append(cnae_corresp22)
cnae_corresp = cnae_corresp.append(cnae_corresp21)
cnae_corresp = cnae_corresp.append(cnae_corresp20)
cnae_corresp.reset_index(inplace=True)
cnae_corresp = cnae_corresp.groupby(['Subclasse']).head(1)

cnae_corresp.rename(mapper=mapper,axis=1,inplace=True)
# Exporta para csv
cnae_corresp.to_csv('cnae_corresp_longo.csv', sep=';', decimal=',', index=False)



## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##

cnae_corresp20_cp = cnae_corresp20.copy()
cnae_corresp21_cp = cnae_corresp21.copy()
cnae_corresp22_cp = cnae_corresp22.copy()
cnae_corresp23_cp = cnae_corresp23.copy()

cnae_corresp = cnae_corresp20_cp.copy()
cnae_corresp.update(cnae_corresp21_cp)
cnae_corresp.update(cnae_corresp22_cp)
cnae_corresp.update(cnae_corresp23_cp)









cnae_Subclasse = cnae_Subclasse20.copy()
cnae_Subclasse.update(cnae_Subclasse21)
cnae_Subclasse.update(cnae_Subclasse22)
cnae_Subclasse.update(cnae_Subclasse23)


## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##
## --------------------------------------------------------------- ##


# Renomeia colunas
todas_Seção.rename(mapper={'Seção':'cnae_seção_cod','Descrição':'cnae_seção_desc'},axis=1,inplace=True)
todas_Divisão.rename(mapper={'Divisão':'cnae_divisão_cod','Descrição':'cnae_divisão_desc'},axis=1,inplace=True)
todas_Grupo.rename(mapper={'Grupo':'cnae_grupo_cod','Descrição':'cnae_grupo_desc'},axis=1,inplace=True)
todas_Classe.rename(mapper={'Classe':'cnae_classe_cod','Descrição':'cnae_classe_desc'},axis=1,inplace=True)
todas_Subclasse.rename(mapper={'Subclasse':'cnae_subclasse_cod','Descrição':'cnae_subclasse_desc'},axis=1,inplace=True)

# Gera DF de correspondências
df_corresp = todas_Subclasse.copy()
df_corresp.drop(['Versão','cnae_subclasse_desc'],axis=1,inplace=True)
df_corresp['cnae_classe_cod'] = df_corresp['cnae_subclasse_cod'].str.slice(0,5)
df_corresp['cnae_grupo_cod'] = df_corresp['cnae_subclasse_cod'].str.slice(0,3)
df_corresp['cnae_divisão_cod'] = df_corresp['cnae_subclasse_cod'].str.slice(0,2)
df_corresp = df_corresp.merge(cnae_seção_corresp,how='left',left_on='cnae_divisão_cod',right_on='Divisão')
df_corresp.drop(['Divisão'],axis=1,inplace=True)
df_corresp.rename(mapper={'Seção':'cnae_seção_cod'},axis=1,inplace=True)
    