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

# Correspondência
cnae_corresp = cnae.copy()
cond1 = ~ cnae_corresp['Subclasse'].isnull()
cnae_corresp = cnae_corresp.loc[cond1,:]

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção = cnae_Seção.groupby('Seção').first()
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').first()
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').first()
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').first()
cnae_Subclasse = cnae_Subclasse.dropna()
cnae_Subclasse = cnae_Subclasse.groupby('Subclasse').first()

# Reseta index
cnae_Seção.reset_index(inplace=True)
cnae_Divisão.reset_index(inplace=True)
cnae_Grupo.reset_index(inplace=True)
cnae_Classe.reset_index(inplace=True)
cnae_Subclasse.reset_index(inplace=True)

# Pega a correspondência: Divisão -> Seção (passo somente na versão 2.3)
cnae_seção_corresp= cnae[['Subclasse', 'Classe', 'Grupo', 'Divisão', 'Seção']]
cnae_seção_corresp.dropna(inplace=True)
cnae_seção_corresp = cnae_seção_corresp.groupby('Divisão').head(1)
cnae_seção_corresp = cnae_seção_corresp[['Divisão','Seção']]

# Cria o DF maior
todas_Seção = cnae_Seção.copy()
todas_Divisão = cnae_Divisão.copy()
todas_Grupo = cnae_Grupo.copy()
todas_Classe = cnae_Classe.copy()
todas_Subclasse = cnae_Subclasse.copy()

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

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção = cnae_Seção.groupby('Seção').first()
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').first()
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').first()
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').first()
cnae_Subclasse = cnae_Subclasse.dropna()
cnae_Subclasse = cnae_Subclasse.groupby('Subclasse').first()

# Reseta index
cnae_Seção.reset_index(inplace=True)
cnae_Divisão.reset_index(inplace=True)
cnae_Grupo.reset_index(inplace=True)
cnae_Classe.reset_index(inplace=True)
cnae_Subclasse.reset_index(inplace=True)

#cnae_Subclasse['len'] = cnae_Subclasse['Subclasse'].str.len()
#print(cnae_Subclasse['len'].value_counts())

# Adiciona ao DF maior
todas_Seção = todas_Seção.append(cnae_Seção)
todas_Divisão = todas_Divisão.append(cnae_Divisão)
todas_Grupo = todas_Grupo.append(cnae_Grupo)
todas_Classe = todas_Classe.append(cnae_Classe)
todas_Subclasse = todas_Subclasse.append(cnae_Subclasse)

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

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção = cnae_Seção.groupby('Seção').first()
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').first()
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').first()
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').first()
cnae_Subclasse = cnae_Subclasse.dropna()
cnae_Subclasse = cnae_Subclasse.groupby('Subclasse').first()

# Reseta index
cnae_Seção.reset_index(inplace=True)
cnae_Divisão.reset_index(inplace=True)
cnae_Grupo.reset_index(inplace=True)
cnae_Classe.reset_index(inplace=True)
cnae_Subclasse.reset_index(inplace=True)

# Adiciona ao DF maior
todas_Seção = todas_Seção.append(cnae_Seção)
todas_Divisão = todas_Divisão.append(cnae_Divisão)
todas_Grupo = todas_Grupo.append(cnae_Grupo)
todas_Classe = todas_Classe.append(cnae_Classe)
todas_Subclasse = todas_Subclasse.append(cnae_Subclasse)

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

   #cnae['len'] = cnae['Subclasse'].str.len()
   #print(cnae['len'].value_counts())

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção = cnae_Seção.groupby('Seção').first()
cnae_Divisão = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão.groupby('Divisão').first()
cnae_Grupo = cnae_Grupo.dropna()
cnae_Grupo = cnae_Grupo.groupby('Grupo').first()
cnae_Classe = cnae_Classe.dropna()
cnae_Classe = cnae_Classe.groupby('Classe').first()
cnae_Subclasse = cnae_Subclasse.dropna()
cnae_Subclasse = cnae_Subclasse.groupby('Subclasse').first()

# Reseta index
cnae_Seção.reset_index(inplace=True)
cnae_Divisão.reset_index(inplace=True)
cnae_Grupo.reset_index(inplace=True)
cnae_Classe.reset_index(inplace=True)
cnae_Subclasse.reset_index(inplace=True)

#cnae_Subclasse['len'] = cnae_Subclasse['Subclasse'].str.len()
#print(cnae_Subclasse['len'].value_counts())

# Adiciona ao DF maior
todas_Seção = todas_Seção.append(cnae_Seção)
todas_Divisão = todas_Divisão.append(cnae_Divisão)
todas_Grupo = todas_Grupo.append(cnae_Grupo)
todas_Classe = todas_Classe.append(cnae_Classe)
todas_Subclasse = todas_Subclasse.append(cnae_Subclasse)

#todas_Subclasse['len'] = todas_Subclasse['Subclasse'].str.len()
#print(todas_Subclasse['len'].value_counts())


# Pega a útlima versão
todas_Seção.sort_values(by=['Seção','Versão'],ascending=[True,False],inplace=True)
todas_Seção = todas_Seção.groupby(['Seção']).head(1)

todas_Divisão.sort_values(by=['Divisão','Versão'],ascending=[True,False],inplace=True)
todas_Divisão = todas_Divisão.groupby(['Divisão']).head(1)

todas_Grupo.sort_values(by=['Grupo','Versão'],ascending=[True,False],inplace=True)
todas_Grupo = todas_Grupo.groupby(['Grupo']).head(1)

todas_Classe.sort_values(by=['Classe','Versão'],ascending=[True,False],inplace=True)
todas_Classe = todas_Classe.groupby(['Classe']).head(1)

todas_Subclasse.sort_values(by=['Subclasse','Versão'],ascending=[True,False],inplace=True)
todas_Subclasse = todas_Subclasse.groupby(['Subclasse']).head(1)

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
    