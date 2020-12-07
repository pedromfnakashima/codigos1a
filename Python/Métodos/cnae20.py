# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:44:12 2020

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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Siconfi"""
caminho_wd = caminho_base / 'Dados' / 'cnae e ncm'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

######################################################################################
# CNAE 2.3 ###########################################################################
######################################################################################

import pandas as pd
dtype = {'Seção':'str','Divisão':'str','Grupo':'str','Classe':'str','subclasse':'str'}
cnae23 = pd.read_excel('CNAE_Subclasses_2_3_Estrutura_Detalhada.xlsx',
                       sheet_name='Estrutura Det. CNAE Subclass2.3',
                       skiprows=3,
                       dtype=dtype)



cnae23.rename(mapper={'Unnamed: 5':'Descrição'},axis=1,inplace=True)

# Renomeia colunas
cnae23.rename(mapper={'Subclasse':'cnae23_Subclasse_cod7'},axis=1,inplace=True)
cnae23.rename(mapper={'Classe':'cnae23_Classe_cod5'},axis=1,inplace=True)
cnae23.rename(mapper={'Grupo':'cnae23_Grupo_cod3'},axis=1,inplace=True)
cnae23.rename(mapper={'Divisão':'cnae23_Divisão_cod2'},axis=1,inplace=True)
cnae23.rename(mapper={'Seção':'cnae23_Seção_cod1'},axis=1,inplace=True)

cnae23['cnae23_Seção_cod1'].fillna(method='ffill', inplace=True)
cnae23['cnae23_Divisão_cod2'].fillna(method='ffill', inplace=True)
cnae23['cnae23_Grupo_cod3'].fillna(method='ffill', inplace=True)
cnae23['cnae23_Classe_cod5'].fillna(method='ffill', inplace=True)
cnae23['cnae23_Subclasse_cod7'].fillna(method='ffill', inplace=True)
cnae23['cnae23_Subclasse_cod7'] = cnae23['cnae23_Subclasse_cod7'].str.replace('-','').str.replace('/','')
cnae23['cnae23_Classe_cod5'] = cnae23['cnae23_Classe_cod5'].str.replace('.','').str.replace('-','')
cnae23['cnae23_Grupo_cod3'] = cnae23['cnae23_Grupo_cod3'].str.replace('.','')

cnae23_Seção = cnae23[['cnae23_Seção_cod1', 'Descrição']]
cnae23_Divisão = cnae23[['cnae23_Divisão_cod2', 'Descrição']]
cnae23_Grupo = cnae23[['cnae23_Grupo_cod3', 'Descrição']]
cnae23_Classe = cnae23[['cnae23_Classe_cod5', 'Descrição']]
cnae23_Subclasse = cnae23[['cnae23_Subclasse_cod7', 'Descrição']]

# Renomeia colunas
cnae23_Subclasse.rename(mapper={'Descrição':'cnae23_Subclasse_desc'},axis=1,inplace=True)
cnae23_Classe.rename(mapper={'Descrição':'cnae23_Classe_desc'},axis=1,inplace=True)
cnae23_Grupo.rename(mapper={'Descrição':'cnae23_Grupo_desc'},axis=1,inplace=True)
cnae23_Divisão.rename(mapper={'Descrição':'cnae23_Divisão_desc'},axis=1,inplace=True)
cnae23_Seção.rename(mapper={'Descrição':'cnae23_Seção_desc'},axis=1,inplace=True)


cnae23_Seção = cnae23_Seção.groupby('cnae23_Seção_cod1').first()
cnae23_Divisão = cnae23_Divisão.dropna()
cnae23_Divisão = cnae23_Divisão.groupby('cnae23_Divisão_cod2').first()
cnae23_Grupo = cnae23_Grupo.dropna()
cnae23_Grupo = cnae23_Grupo.groupby('cnae23_Grupo_cod3').first()
cnae23_Classe = cnae23_Classe.dropna()
cnae23_Classe = cnae23_Classe.groupby('cnae23_Classe_cod5').first()
cnae23_Subclasse = cnae23_Subclasse.dropna()
cnae23_Subclasse = cnae23_Subclasse.groupby('cnae23_Subclasse_cod7').first()

cnae23_Seção.reset_index(inplace=True)
cnae23_Divisão.reset_index(inplace=True)
cnae23_Grupo.reset_index(inplace=True)
cnae23_Classe.reset_index(inplace=True)
cnae23_Subclasse.reset_index(inplace=True)


# Exporta para csv
cnae23_Seção.to_csv('cnae23_Seção_desc.csv', sep=';', decimal=',', index=False)
cnae23_Divisão.to_csv('cnae23_Divisão_desc.csv', sep=';', decimal=',', index=False)
cnae23_Grupo.to_csv('cnae23_Grupo_desc.csv', sep=';', decimal=',', index=False)
cnae23_Classe.to_csv('cnae23_Classe_desc.csv', sep=';', decimal=',', index=False)
cnae23_Subclasse.to_csv('cnae23_Subclasse_desc.csv', sep=';', decimal=',', index=False)
del cnae23_Seção, cnae23_Divisão, cnae23_Grupo, cnae23_Classe, cnae23_Subclasse


cnae23_subclasses = cnae23[['cnae23_Subclasse_cod7', 'cnae23_Classe_cod5', 'cnae23_Grupo_cod3', 'cnae23_Divisão_cod2', 'cnae23_Seção_cod1']]


cnae23_subclasses.dropna(inplace=True)
cnae23_subclasses = cnae23_subclasses.groupby('cnae23_Subclasse_cod7').first()
cnae23_subclasses.reset_index(inplace=True)
cnae23_subclasses.sort_values(by='cnae23_Subclasse_cod7', inplace=True)

cnae23_classes = cnae23[['cnae23_Classe_cod5', 'cnae23_Grupo_cod3', 'cnae23_Divisão_cod2', 'cnae23_Seção_cod1']]
cnae23_classes.dropna(inplace=True)
cnae23_classes = cnae23_classes.groupby('cnae23_Classe_cod5').first()
cnae23_classes.reset_index(inplace=True)
cnae23_classes.sort_values(by='cnae23_Classe_cod5', inplace=True)


cnae23_grupos = cnae23[['cnae23_Grupo_cod3', 'cnae23_Divisão_cod2', 'cnae23_Seção_cod1']]
cnae23_grupos.dropna(inplace=True)
cnae23_grupos = cnae23_grupos.groupby('cnae23_Grupo_cod3').first()
cnae23_grupos.reset_index(inplace=True)
cnae23_grupos.sort_values(by='cnae23_Grupo_cod3', inplace=True)

cnae23_divisões = cnae23[['cnae23_Divisão_cod2', 'cnae23_Seção_cod1']]
cnae23_divisões.dropna(inplace=True)
cnae23_divisões = cnae23_divisões.groupby('cnae23_Divisão_cod2').first()
cnae23_divisões.reset_index(inplace=True)
cnae23_divisões.sort_values(by='cnae23_Divisão_cod2', inplace=True)

cnae23_subclasses.to_csv('cnae23_Subclasse_corresp.csv', sep=';', decimal=',', index=False)
cnae23_classes.to_csv('cnae23_Classe_corresp.csv', sep=';', decimal=',', index=False)
cnae23_grupos.to_csv('cnae23_Grupo_corresp.csv', sep=';', decimal=',', index=False)
cnae23_divisões.to_csv('cnae23_Divisão_corresp.csv', sep=';', decimal=',', index=False)



######################################################################################
# CNAE 2.0 ###########################################################################
######################################################################################

import pandas as pd
cnae20 = pd.read_excel('CNAE20_Subclasses_EstruturaDetalhada.xlsx', sheet_name='Est. Detalhada CNAE 2.0 - subcl')

print(cnae20.columns)

cnae20 = cnae20.drop(['Unnamed: 0'], axis=1)

cnae20 = cnae20.rename(columns={'2.2 Estrutura detalhada da CNAE 2.0: seções, divisões, grupos, classes e subclasses':'seção',
                                'Unnamed: 2':'divisão',
                                'Unnamed: 3':'grupo',
                                'Unnamed: 4':'classe',
                                'Unnamed: 5':'subclasse',
                                'Unnamed: 6':'descrição'})

cnae20 = cnae20.iloc[4:,]

cnae20.index = range(len(cnae20))

cond1 = ~ cnae20['seção'].str.contains('continuação', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('2.2', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('2.0', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('Seção', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

cond1 = ~ cnae20['seção'].str.contains('conclusão', regex=False, na=False)
cnae20 = cnae20.loc[cond1,:]

del cond1

print(cnae20.dtypes)
cnae20['seção'].fillna(method='ffill', inplace=True)
cnae20['divisão'].fillna(method='ffill', inplace=True)
cnae20['grupo'].fillna(method='ffill', inplace=True)
cnae20['classe'].fillna(method='ffill', inplace=True)
cnae20['subclasse'].fillna(method='ffill', inplace=True)


cnae20['subclasse'] = cnae20['subclasse'].str.replace('-','').str.replace('/','')
cnae20['classe'] = cnae20['classe'].str.replace('.','').str.replace('-','')
cnae20['grupo'] = cnae20['grupo'].str.replace('.','')

cnae20 = cnae20.iloc[:-2]

cnae20 = cnae20.astype('str')


cnae20_seção = cnae20[['seção', 'descrição']]
cnae20_divisão = cnae20[['divisão', 'descrição']]
cnae20_grupo = cnae20[['grupo', 'descrição']]
cnae20_classe = cnae20[['classe', 'descrição']]
cnae20_subclasse = cnae20[['subclasse', 'descrição']]

cnae20_seção = cnae20_seção.groupby('seção').first()

cnae20_divisão = cnae20_divisão.dropna()
cnae20_divisão = cnae20_divisão.groupby('divisão').first()

cnae20_grupo = cnae20_grupo.dropna()
cnae20_grupo = cnae20_grupo.groupby('grupo').first()

cnae20_classe = cnae20_classe.dropna()
cnae20_classe = cnae20_classe.groupby('classe').first()

cnae20_subclasse = cnae20_subclasse.dropna()
cnae20_subclasse = cnae20_subclasse.groupby('subclasse').first()

cnae20_seção.reset_index(inplace=True)
cnae20_divisão.reset_index(inplace=True)
cnae20_grupo.reset_index(inplace=True)
cnae20_classe.reset_index(inplace=True)
cnae20_subclasse.reset_index(inplace=True)

# Renomeia colunas
cnae20_subclasse.rename(mapper={'subclasse':'cnae2_subclasse_cod7','descrição':'cnae2_subclasse_desc'},axis=1,inplace=True)
cnae20_classe.rename(mapper={'classe':'cnae2_classe_cod5','descrição':'cnae2_classe_desc'},axis=1,inplace=True)
cnae20_grupo.rename(mapper={'grupo':'cnae2_grupo_cod3','descrição':'cnae2_grupo_desc'},axis=1,inplace=True)
cnae20_divisão.rename(mapper={'divisão':'cnae2_divisão_cod2','descrição':'cnae2_divisão_desc'},axis=1,inplace=True)
cnae20_seção.rename(mapper={'seção':'cnae2_seção_cod1','descrição':'cnae2_seção_desc'},axis=1,inplace=True)


# Exporta para csv
cnae20_seção.to_csv('cnae20_seção_desc.csv', sep=';', decimal=',', index=False)
cnae20_divisão.to_csv('cnae20_divisão_desc.csv', sep=';', decimal=',', index=False)
cnae20_grupo.to_csv('cnae20_grupo_desc.csv', sep=';', decimal=',', index=False)
cnae20_classe.to_csv('cnae20_classe_desc.csv', sep=';', decimal=',', index=False)
cnae20_subclasse.to_csv('cnae20_subclasse_desc.csv', sep=';', decimal=',', index=False)





del cnae20_seção, cnae20_divisão, cnae20_grupo, cnae20_classe, cnae20_subclasse

cnae20_subclasses = cnae20[['subclasse', 'classe', 'grupo', 'divisão', 'seção']]
cnae20_subclasses.dropna(inplace=True)
cnae20_subclasses = cnae20_subclasses.groupby('subclasse').first()
cnae20_subclasses.reset_index(inplace=True)
cnae20_subclasses.sort_values(by='subclasse', inplace=True)

cnae20_classes = cnae20[['classe', 'grupo', 'divisão', 'seção']]
cnae20_classes.dropna(inplace=True)
cnae20_classes = cnae20_classes.groupby('classe').first()
cnae20_classes.reset_index(inplace=True)
cnae20_classes.sort_values(by='classe', inplace=True)

cnae20_grupos = cnae20[['grupo', 'divisão', 'seção']]
cnae20_grupos.dropna(inplace=True)
cnae20_grupos = cnae20_grupos.groupby('grupo').first()
cnae20_grupos.reset_index(inplace=True)
cnae20_grupos.sort_values(by='grupo', inplace=True)

cnae20_divisões = cnae20[['divisão', 'seção']]
cnae20_divisões.dropna(inplace=True)
cnae20_divisões = cnae20_divisões.groupby('divisão').first()
cnae20_divisões.reset_index(inplace=True)
cnae20_divisões.sort_values(by='divisão', inplace=True)

cnae20_subclasses.to_csv('cnae20_subclasse_corresp.csv', sep=';', decimal=',', index=False)
cnae20_classes.to_csv('cnae20_classe_corresp.csv', sep=';', decimal=',', index=False)
cnae20_grupos.to_csv('cnae20_grupo_corresp.csv', sep=';', decimal=',', index=False)
cnae20_divisões.to_csv('cnae20_divisão_corresp.csv', sep=';', decimal=',', index=False)


print(cnae20_divisões.dtypes)



print(cnae20_divisões.dtypes)




