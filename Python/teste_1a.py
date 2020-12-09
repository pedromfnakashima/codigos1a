# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:52:03 2020

@author: pedro
"""
print(df['saldomovimentação'].sum())


print(df_agregado['saldomovimentação'].sum())

print(df_agregado['saldomovimentação'].sum() - df['saldomovimentação'].sum())



cond1 = df['dt'].dt.year == 2020
filtro = df.loc[cond1,:]
print(filtro['saldomovimentação'].sum())


df_agregado2 = df_agregado.merge(df_Classe,how='inner',left_on='cnae_classe_cod',right_on='cnae_classe_cod')
print(df_agregado2['saldomovimentação'].sum())

df_Classe2 = df_Classe.groupby(['cnae_classe_cod']).head(1)


'''
Número de linhas em df_agregado: 666

'''







