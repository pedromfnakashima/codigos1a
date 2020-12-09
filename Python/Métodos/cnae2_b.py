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
cnae23 = pd.read_excel('CNAE23_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

cnae23.rename(mapper={'Unnamed: 5':'Descrição'},axis=1,inplace=True)

# Cria coluna com a versão
cnae23['Versão'] = '2.3'

'''
# Preenche para baixo
cnae23['Seção'].fillna(method='ffill', inplace=True)
cnae23['Divisão'].fillna(method='ffill', inplace=True)
cnae23['Grupo'].fillna(method='ffill', inplace=True)
cnae23['Classe'].fillna(method='ffill', inplace=True)
'''

######################################################################################
# CNAE 2.2 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae22 = pd.read_excel('CNAE22_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

#print(cnae.dtypes)
cnae22.drop(['Unnamed: 0'],axis=1,inplace=True)
cnae22.rename(mapper={'Unnamed: 1':'Seção','Unnamed: 2':'Divisão','Unnamed: 3':'Grupo','Unnamed: 4':'Classe','Unnamed: 5':'Subclasse','Denominação':'Descrição'},axis=1,inplace=True)
cnae22.drop([0],axis=0,inplace=True)

# Deleta linhas lixo
cond1 = ~ cnae22['Seção'].str.contains('continuação', regex=False, na=False)
cnae22 = cnae22.loc[cond1,:]
cond1 = ~ cnae22['Seção'].str.contains('2.2', regex=False, na=False)
cnae22= cnae22.loc[cond1,:]
cond1 = ~ cnae22['Seção'].str.contains('2.0', regex=False, na=False)
cnae22 = cnae22.loc[cond1,:]
cond1 = ~ cnae22['Seção'].str.contains('Seção', regex=False, na=False)
cnae22 = cnae22.loc[cond1,:]
cond1 = ~ cnae22['Seção'].str.contains('conclusão', regex=False, na=False)
cnae22 = cnae22.loc[cond1,:]
cnae22 = cnae22.iloc[:-2] # deleta últimas duas linhas

# Cria coluna com a versão
cnae22['Versão'] = '2.2'

######################################################################################
# CNAE 2.1 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae21 = pd.read_excel('CNAE21_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

#print(cnae.dtypes)
cnae21.drop(['Unnamed: 0'],axis=1,inplace=True)
cnae21.rename(mapper={'código CNAE 2.0':'Seção','Unnamed: 2':'Divisão','Unnamed: 3':'Grupo','Unnamed: 4':'Classe','Unnamed: 5':'Subclasse','Denominação':'Descrição'},axis=1,inplace=True)
cnae21.drop([0],axis=0,inplace=True)

# Deleta linhas lixo
cond1 = ~ cnae21['Seção'].str.contains('continuação', regex=False, na=False)
cnae21 = cnae21.loc[cond1,:]
cond1 = ~ cnae21['Seção'].str.contains('2.2', regex=False, na=False)
cnae21 = cnae21.loc[cond1,:]
cond1 = ~ cnae21['Seção'].str.contains('2.0', regex=False, na=False)
cnae21 = cnae21.loc[cond1,:]
cond1 = ~ cnae21['Seção'].str.contains('Seção', regex=False, na=False)
cnae21 = cnae21.loc[cond1,:]
cond1 = ~ cnae21['Seção'].str.contains('conclusão', regex=False, na=False)
cnae21 = cnae21.loc[cond1,:]
cnae21 = cnae21.iloc[:-2] # deleta últimas duas linhas

# Cria coluna com a versão
cnae21['Versão'] = '2.1'

######################################################################################
# CNAE 2.0 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae20 = pd.read_excel('CNAE20_Subclasses_EstruturaDetalhada.xlsx',
                       sheet_name='estrutura',
                       skiprows=3,
                       dtype='str')

#print(cnae.dtypes)
cnae20.drop(['Unnamed: 0'],axis=1,inplace=True)
cnae20.rename(mapper={'código CNAE 2.0':'Seção','Unnamed: 2':'Divisão','Unnamed: 3':'Grupo','Unnamed: 4':'Classe','Unnamed: 5':'Subclasse','Denominação':'Descrição'},axis=1,inplace=True)
cnae20.drop([0],axis=0,inplace=True)

# Deleta linhas lixo
cond1 = ~ cnae20['Seção'].str.contains('continuação', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]
cond1 = ~ cnae20['Seção'].str.contains('2.2', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]
cond1 = ~ cnae20['Seção'].str.contains('2.0', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]
cond1 = ~ cnae20['Seção'].str.contains('Seção', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]
cond1 = ~ cnae20['Seção'].str.contains('conclusão', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]
cnae20 = cnae20.iloc[:-2] # deleta últimas duas linhas

# Cria coluna com a versão
cnae20['Versão'] = '2.0'

######################################################################################
# CNAE  ##############################################################################
######################################################################################
'''
CAGEDMOV202010.csv
cnae_classe_cod
394989
395017
28
'''


cnae = cnae23.append(cnae22)
cnae = cnae.append(cnae21)
cnae = cnae.append(cnae20)
cnae['Descrição'] = cnae['Descrição'].str.replace('\n',' ')

# Tira espaços das colunas
for coluna in cnae.columns:
    print(coluna)
    cnae[coluna] = cnae[coluna].str.strip()


# Preenche para baixo
cnae['Seção'].fillna(method='ffill', inplace=True)
cnae['Divisão'].fillna(method='ffill', inplace=True)
cnae['Grupo'].fillna(method='ffill', inplace=True)
cnae['Classe'].fillna(method='ffill', inplace=True)

cnae_corresp = cnae.copy()
cond1 = ~ cnae_corresp['Subclasse'].isnull()
cnae_corresp = cnae_corresp.loc[cond1,:]
cnae_corresp = cnae_corresp.groupby(['Subclasse']).head(1)

# Tira pontuação
cnae_corresp['Subclasse'] = cnae_corresp['Subclasse'].str.replace('-','').str.replace('/','')
cnae_corresp['Classe'] = cnae_corresp['Classe'].str.replace('.','').str.replace('-','')
cnae_corresp['Grupo'] = cnae_corresp['Grupo'].str.replace('.','')

cnae_corresp.index = range(len(cnae_corresp))

print(cnae_corresp.shape)
print(cnae_corresp.nunique())

cond1 = cnae_corresp['Descrição'].duplicated(keep=False)
print(cond1.sum())
filtro = cnae_corresp.loc[cond1,:]





# Renomeia
mapper = {'Seção':'cnae_seção_cod','Divisão':'cnae_divisão_cod','Grupo':'cnae_grupo_cod','Classe':'cnae_classe_cod','Subclasse':'cnae_subclasse_cod'}
cnae_corresp.rename(mapper=mapper,axis=1,inplace=True)


print(cnae_corresp.nunique())

cond1 = cnae_corresp['Descrição'].duplicated(keep='first')
print(cond1.sum())
filtro = cnae_corresp.loc[cond1,:]

cnae_corresp2 = cnae_corresp.groupby(['Descrição']).head(1)
cnae_corresp2['match'] = 'SIM'
cnae_corresp2 = cnae_corresp2[['Subclasse','match']]

cnae_corresp = cnae_corresp.merge(cnae_corresp2,how='left',left_on='Subclasse',right_on='Subclasse')



cnae_corresp.to_csv('cnae_corresp.csv', sep='|', decimal=',', index=False)

















cnae_seção = cnae.groupby(['Seção']).head(1)
cnae_seção = cnae_seção[['Seção','Descrição','Versão']]
cnae_seção.index = range(len(cnae_seção))

cnae_divisão = cnae.groupby(['Divisão']).head(1)
cnae_divisão = cnae_divisão[['Divisão','Descrição','Versão']]
cnae_divisão.dropna(inplace=True)
cnae_divisão.index = range(len(cnae_divisão))

cnae_grupo = cnae.groupby(['Grupo']).head(1)
cnae_grupo = cnae_grupo[['Grupo','Descrição','Versão']]
cnae_grupo.dropna(inplace=True)
cnae_grupo.index = range(len(cnae_grupo))

cnae_classe = cnae.groupby(['Classe']).head(1)
cnae_classe = cnae_classe[['Classe','Descrição','Versão']]
cnae_classe.dropna(inplace=True)
cnae_classe.index = range(len(cnae_classe))

cnae_subclasse = cnae.groupby(['Subclasse']).head(1)
cnae_subclasse = cnae_subclasse[['Subclasse','Descrição','Versão']]
cnae_subclasse.dropna(inplace=True)
cnae_subclasse.index = range(len(cnae_subclasse))

cnae_subclasse.sort_values(by=['Subclasse'],ascending=[True],inplace=True)


cnae_corresp = cnae.copy()
cnae_corresp = cnae_corresp.groupby(['Subclasse']).head(1)
cnae_corresp.dropna(inplace=True)
cnae_corresp.index = range(len(cnae_corresp))

print(cnae_corresp.nunique())


cnae_corresp = cnae_corresp.merge(cnae_grupo,how='outer',left_on='Grupo',right_on='Grupo')
cnae_corresp.sort_values(by=['Grupo'],ascending=[True],inplace=True)




print(cnae_classe['Classe'].nunique())




cnae_subclasse = cnae.dropna(axis=0,thresh=7)




cnae = cnae.groupby(['Versão','Subclasse']).head(1)














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
















