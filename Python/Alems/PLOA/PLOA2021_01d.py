# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 07:07:09 2020

@author: pedro-salj
"""

'''
Rodar as funções do arquivo junta_siconfi_01b.py
'''
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

##################################################################################################

############# DESPESAS POR FUNÇÃO
pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Estados' / 'Despesas por Função'
ca_desp_função = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta,
                                           pasta=True)

# SAÚDE
cond1 = ca_desp_função['exercicio'] >= 2016
cond2 = ca_desp_função['Conta'].str.contains('saúde', case=False)
cond2 = ca_desp_função['Conta'] == '10 - Saúde'
cond3 = ca_desp_função['Coluna'].str.contains('liquidadas', case=False)
cond4 = ca_desp_função['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = ca_desp_função.loc[cond, :]
filtro.rename(columns={'Valor':'Saúde'}, inplace=True)
desp_funções = filtro.loc[:, ['exercicio', 'Saúde']]

# EDUCAÇÃO
cond1 = ca_desp_função['exercicio'] >= 2016
cond2 = ca_desp_função['Conta'].str.contains('educação', case=False)
cond2 = ca_desp_função['Conta'] == '12 - Educação'
cond3 = ca_desp_função['Coluna'].str.contains('liquidadas', case=False)
cond4 = ca_desp_função['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = ca_desp_função.loc[cond, :]
filtro.rename(columns={'Valor':'Educação'}, inplace=True)
desp_funções = desp_funções.merge(filtro.loc[:,['exercicio','Educação']], how='left', left_on='exercicio', right_on='exercicio')

# SEGURANÇA
cond1 = ca_desp_função['exercicio'] >= 2016
cond2 = ca_desp_função['Conta'].str.contains('segurança', case=False)
cond2 = ca_desp_função['Conta'] == '06 - Segurança Pública'
cond3 = ca_desp_função['Coluna'].str.contains('liquidadas', case=False)
cond4 = ca_desp_função['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = ca_desp_função.loc[cond, :]
filtro.rename(columns={'Valor':'Segurança'}, inplace=True)
desp_funções = desp_funções.merge(filtro.loc[:,['exercicio','Segurança']], how='left', left_on='exercicio', right_on='exercicio')

# TRABALHO
cond1 = ca_desp_função['exercicio'] >= 2016
cond2 = ca_desp_função['Conta'].str.contains('trabalho', case=False)
cond2 = ca_desp_função['Conta'] == '11 - Trabalho'
cond3 = ca_desp_função['Coluna'].str.contains('liquidadas', case=False)
cond4 = ca_desp_função['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = ca_desp_função.loc[cond, :]
filtro.rename(columns={'Valor':'Trabalho'}, inplace=True)
desp_funções = desp_funções.merge(filtro.loc[:,['exercicio','Trabalho']], how='left', left_on='exercicio', right_on='exercicio')

# HABITAÇÃO
cond1 = ca_desp_função['exercicio'] >= 2016
cond2 = ca_desp_função['Conta'].str.contains('habitação', case=False)
cond2 = ca_desp_função['Conta'] == '16 - Habitação'
cond3 = ca_desp_função['Coluna'].str.contains('liquidadas', case=False)
cond4 = ca_desp_função['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = ca_desp_função.loc[cond, :]
filtro.rename(columns={'Valor':'Habitação'}, inplace=True)
desp_funções = desp_funções.merge(filtro.loc[:,['exercicio','Habitação']], how='left', left_on='exercicio', right_on='exercicio')

del cond, cond1, cond2, cond3, cond4
del filtro

########################### IPCA #########################################
import pandas as pd
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
df_ipca['mês'] = df_ipca.index.month
df_ipca['ano'] = df_ipca.index.year
cond = df_ipca['mês'] == 10
df_ipca = df_ipca.loc[cond,:]
df_ipca.drop(['mês'], axis=1, inplace=True)
# Deflator
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['Deflator'] = atual / df_ipca['Índice']
##########################################################################

desp_funções = desp_funções.merge(df_ipca, how='left', left_on='exercicio', right_on='ano')
desp_funções.drop(['ano'], axis=1, inplace=True)

desp_funções['Saúde_d'] = desp_funções['Saúde'] * desp_funções['Deflator']
desp_funções['Educação_d'] = desp_funções['Educação'] * desp_funções['Deflator']
desp_funções['Segurança_d'] = desp_funções['Segurança'] * desp_funções['Deflator']
desp_funções['Trabalho_d'] = desp_funções['Trabalho'] * desp_funções['Deflator']
desp_funções['Habitação_d'] = desp_funções['Habitação'] * desp_funções['Deflator']

desp_funções.drop(['Índice','Deflator','Saúde','Educação','Segurança','Trabalho','Habitação'], axis=1, inplace=True)
#desp_funções.drop(['ano'], axis=1, inplace=True)

desp_funções.set_index(['exercicio'], inplace=True)
#desp_funções.index.freq = 'AS'

desp_funções_M = desp_funções / 1_000_000
desp_funções_B = desp_funções / 1_000_000_000


pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    desp_funções_M.to_excel(writer, sheet_name='desp_funções_M', index=True)

pasta = caminho_base / 'Dados' / 'alems' / 'LOA, LDO - MS'
with pd.ExcelWriter(pasta / 'Dados_para_gráficos.xlsx', mode='a', engine="openpyxl") as writer:  
    desp_funções_B.to_excel(writer, sheet_name='desp_funções_B', index=True)











desp_funções_B['Saúde_d'].plot()

from matplotlib import pyplot as plt

fig1, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=False)

ax1.plot(desp_funções_B['Educação_d'], label='Educação')
ax1.plot(desp_funções_B['Saúde_d'], label='Saúde')
ax1.plot(desp_funções_B['Segurança_d'], label='Segurança')

# Configuração de ax1
import numpy as np
ax1.set_xticks(np.arange(2016,2020,1))
ax1.set_title('Saúde, Educação, Segurança Pública', fontsize=18)
ax1.set_ylabel('Bilhões de Reais')
ax1.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax1.grid(True)

ax2.plot(desp_funções_M['Trabalho_d'], label='Trabalho')
# Configuração de ax2
import numpy as np
ax2.set_xticks(np.arange(2016,2020,1))
ax2.set_title('Trabalho', fontsize=18)
ax2.set_ylabel('Milhões de Reais')
ax2.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax2.grid(True)

ax3.plot(desp_funções_M['Habitação_d'], label='Trabalho')
# Configuração de ax2
import numpy as np
ax3.set_xticks(np.arange(2016,2020,1))
ax3.set_title('Habitação', fontsize=18)
ax3.set_ylabel('Milhões de Reais')
ax3.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax3.grid(True)

# Configurações gerais
#fig1.tight_layout()
cm = 1/2.54  # centimetros para polegadas
fig1.set_size_inches(20*cm, 40*cm)
fig1.show()






