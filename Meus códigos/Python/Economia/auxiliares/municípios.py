# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:12:25 2020

@author: pedro
"""

import pandas as pd

arq_nome = 'municípios_e_ufs.xlsx'
pasta = caminho_base / 'Dados'
municípios = pd.read_excel(pasta / arq_nome, sheet_name='municípios', skiprows=0)

arq_nome = 'municípios_e_ufs.xlsx'
pasta = caminho_base / 'Dados'
ufs = pd.read_excel(pasta / arq_nome, sheet_name='ufs', skiprows=0)

municípios = municípios.merge(ufs,how='left',left_on='uf_sigla',right_on='uf_sigla')

print(municípios.columns)

municípios = municípios.loc[:,['mun_cod7_ibge', 'mun_cod_ibge', 'mun_cod_tse', 'mun_nome', 'mun_nome_curto', 'capital', 'uf_cod_ibge', 'uf_sigla', 'uf_nome', 'Região']]

# arq_nome = 'municípios_e_ufs.xlsx'
# pasta = caminho_base / 'Dados'
# capitais = pd.read_excel(pasta / arq_nome, sheet_name='capitais', skiprows=0)
# capitais['capital'] = 1
# capitais.drop(['mun_nome'],axis=1,inplace=True)
# capitais.rename(mapper={'mun_cod_ibge':'mun_cod7_ibge'},axis=1,inplace=True)


# municípios['mun_nome_curto'] = municípios['mun_nome'].str.slice(3,)
# pasta = caminho_base / 'Dados'
# arq_nome = 'municípios_e_ufs.xlsx'
# with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
#     municípios.to_excel(writer, sheet_name='municípios', index=False)

# municípios = municípios.merge(capitais,how='left',left_on='mun_cod7_ibge',right_on='mun_cod7_ibge')
# municípios['capital'].fillna(0,inplace=True)

# cond1 = municípios['capital'] == 1
# filtro = municípios.loc[cond1,:]

pasta = caminho_base / 'Dados'
arq_nome = 'municípios_e_ufs.xlsx'
with pd.ExcelWriter(pasta / arq_nome, mode='a', engine="openpyxl") as writer:  
    municípios.to_excel(writer, sheet_name='municípios', index=False)










