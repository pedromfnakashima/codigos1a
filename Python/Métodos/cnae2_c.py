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
cnae_corresp23 = cnae.copy()
cond1 = ~ cnae_corresp23['Subclasse'].isnull()
cnae_corresp23 = cnae_corresp23.loc[cond1,:]
cnae_corresp23.drop(['Descrição'],axis=1,inplace=True)
cnae_corresp23.set_index('Subclasse',inplace=True)

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção23 = cnae_Seção.groupby('Seção').first()
cnae_Divisão23 = cnae_Divisão.dropna()
cnae_Divisão23 = cnae_Divisão23.groupby('Divisão').first()
cnae_Grupo23 = cnae_Grupo.dropna()
cnae_Grupo23 = cnae_Grupo23.groupby('Grupo').first()
cnae_Classe23 = cnae_Classe.dropna()
cnae_Classe23 = cnae_Classe23.groupby('Classe').first()
cnae_Subclasse23 = cnae_Subclasse.dropna()
cnae_Subclasse23 = cnae_Subclasse23.groupby('Subclasse').first()


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

# Correspondência
cnae_corresp22 = cnae.copy()
cond1 = ~ cnae_corresp22['Subclasse'].isnull()
cnae_corresp22 = cnae_corresp22.loc[cond1,:]
cnae_corresp22.drop(['Descrição'],axis=1,inplace=True)
cnae_corresp22.set_index('Subclasse',inplace=True)

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção22 = cnae_Seção.groupby('Seção').first()
cnae_Divisão22 = cnae_Divisão.dropna()
cnae_Divisão22 = cnae_Divisão22.groupby('Divisão').first()
cnae_Grupo22 = cnae_Grupo.dropna()
cnae_Grupo22 = cnae_Grupo22.groupby('Grupo').first()
cnae_Classe22 = cnae_Classe.dropna()
cnae_Classe22 = cnae_Classe22.groupby('Classe').first()
cnae_Subclasse22 = cnae_Subclasse.dropna()
cnae_Subclasse22 = cnae_Subclasse22.groupby('Subclasse').first()


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

# Correspondência
cnae_corresp21 = cnae.copy()
cond1 = ~ cnae_corresp21['Subclasse'].isnull()
cnae_corresp21 = cnae_corresp21.loc[cond1,:]
cnae_corresp21.drop(['Descrição'],axis=1,inplace=True)
cnae_corresp21.set_index('Subclasse',inplace=True)

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção21 = cnae_Seção.groupby('Seção').first()
cnae_Divisão21 = cnae_Divisão.dropna()
cnae_Divisão = cnae_Divisão21.groupby('Divisão').first()
cnae_Grupo21 = cnae_Grupo.dropna()
cnae_Grupo21 = cnae_Grupo21.groupby('Grupo').first()
cnae_Classe21 = cnae_Classe.dropna()
cnae_Classe21 = cnae_Classe21.groupby('Classe').first()
cnae_Subclasse21 = cnae_Subclasse.dropna()
cnae_Subclasse21 = cnae_Subclasse21.groupby('Subclasse').first()

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

# Correspondência
cnae_corresp20 = cnae.copy()
cond1 = ~ cnae_corresp20['Subclasse'].isnull()
cnae_corresp20 = cnae_corresp20.loc[cond1,:]
cnae_corresp20.drop(['Descrição'],axis=1,inplace=True)
cnae_corresp20.set_index('Subclasse',inplace=True)

# Seleciona colunas
cnae_Seção = cnae[['Versão', 'Seção', 'Descrição']]
cnae_Divisão = cnae[['Versão', 'Divisão', 'Descrição']]
cnae_Grupo = cnae[['Versão', 'Grupo', 'Descrição']]
cnae_Classe = cnae[['Versão', 'Classe', 'Descrição']]
cnae_Subclasse = cnae[['Versão', 'Subclasse', 'Descrição']]

# Pega o primeiro
cnae_Seção20 = cnae_Seção.groupby('Seção').first()
cnae_Divisão20 = cnae_Divisão.dropna()
cnae_Divisão20 = cnae_Divisão20.groupby('Divisão').first()
cnae_Grupo20 = cnae_Grupo.dropna()
cnae_Grupo20 = cnae_Grupo20.groupby('Grupo').first()
cnae_Classe20 = cnae_Classe.dropna()
cnae_Classe20 = cnae_Classe20.groupby('Classe').first()
cnae_Subclasse20 = cnae_Subclasse.dropna()
cnae_Subclasse20 = cnae_Subclasse20.groupby('Subclasse').first()

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
    