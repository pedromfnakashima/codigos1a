# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:45:51 2020

@author: pedro-salj
"""

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

########################### IPCA #########################################
pasta = caminho_base / 'Dados' / 'Ibge' / 'Ipca'
df_ipca = pd.read_excel(pasta / 'tabela1737.xlsx', sheet_name='Tabela_com_datas', skiprows=0, index_col='data')
df_ipca.index.freq = 'MS'
df_ipca['mês'] = df_ipca.index.month
df_ipca['ano'] = df_ipca.index.year
cond = df_ipca['mês'] == 10
df_ipca = df_ipca.loc[cond,:]
df_ipca.drop(['mês'], axis=1, inplace=True)
atual = df_ipca.loc[df_ipca.index.max(), 'Índice']
df_ipca['deflator'] = atual / df_ipca['Índice']
##########################################################################


############# DESPESAS: PESSOAL e JUROS - DEFLACIONADO

# Rodar antes o arquivo junta_siconfi_01c.py

pasta = caminho_base / 'Dados' / 'Siconfi' / 'Contas Anuais - Estados' / 'Despesas Orçamentárias'
df = processa_arquivos_zip(arquivo='2018.zip',
                                           caminho=pasta,
                                           pasta=True)



# PESSOAL E ENCARGOS SOCIAIS

cond1 = df['exercicio'] >= 2016
cond2 = df['Conta'].str.contains('pessoal e encargos', case=False)
#cond2 = df['Conta'] == '3.1.00.00.00.00'
cond3 = df['Coluna'].str.contains('liquidadas', case=False)
cond4 = df['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = df.loc[cond, :]
filtro = df.loc[cond, ['exercicio', 'Valor']]

filtro = filtro.merge(df_ipca, how='left', left_on='exercicio', right_on='ano')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
filtro = filtro.loc[:, ['exercicio','Valor_d']]

filtro.rename(columns={'Valor_d':'Pessoal e Encargos Sociais'}, inplace=True)

despesas_correntes = filtro.copy()

# PESSOAL E ENCARGOS SOCIAIS

cond1 = df['exercicio'] >= 2016
cond2 = df['Conta'].str.contains('juros e encargos', case=False)
#cond2 = df['Conta'] == '3.1.00.00.00.00'
cond3 = df['Coluna'].str.contains('liquidadas', case=False)
cond4 = df['UF'] == 'MS'
cond = cond1 & cond2 & cond3 & cond4
filtro = df.loc[cond, :]
filtro = df.loc[cond, ['exercicio', 'Valor']]

filtro = filtro.merge(df_ipca, how='left', left_on='exercicio', right_on='ano')
filtro['Valor_d'] = filtro['Valor'] * filtro['deflator']
filtro = filtro.loc[:, ['exercicio','Valor_d']]

filtro.rename(columns={'Valor_d':'Juros e Encargos da Dívida'}, inplace=True)

despesas_correntes = despesas_correntes.merge(filtro, how='left', left_on='exercicio', right_on='exercicio')

despesas_correntes.set_index('exercicio', inplace=True)

despesas_correntes_M = despesas_correntes / 1_000_000
despesas_correntes_B = despesas_correntes / 1_000_000_000


# GRÁFICOS

from matplotlib import pyplot as plt

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=False)

ax1.plot(despesas_correntes_B['Pessoal e Encargos Sociais'], label='Pessoal e Encargos Sociais')
ax2.plot(despesas_correntes_M['Juros e Encargos da Dívida'], label='Juros e Encargos da Dívida')


# Configuração de ax1
import numpy as np
ax1.set_xticks(np.arange(2016,2020,1))
ax1.set_title('Pessoal e Encargos Sociais', fontsize=18)
ax1.set_ylabel('Bilhões de Reais')
ax1.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax1.grid(True)


# Configuração de ax2
import numpy as np
ax2.set_xticks(np.arange(2016,2020,1))
ax2.set_title('Juros e Encargos da Dívida', fontsize=18)
ax2.set_ylabel('Milhões de Reais')
ax2.legend(loc = (1.03,-0.1),
           ncol=1,
           fontsize=8,
    )
ax2.grid(True)


# Configurações gerais
#fig1.tight_layout()
cm = 1/2.54  # centimetros para polegadas
fig1.set_size_inches(20*cm, 40*cm)
fig1.show()





























