# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:29:50 2020

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
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)

#import numpy as np
import pandas as pd

#################################################################################################
################################# DOWNLOAD DOS ARQUIVOS #########################################
#################################################################################################
'''
Períodos e tabelas
2938: julho/2006 até dezembro/2011 (link: https://sidra.ibge.gov.br/Tabela/2938)
1419: janeiro/2012 até dezembro/2019 (link: https://sidra.ibge.gov.br/tabela/1419)
7060: a partir de janeiro/2020 (link: https://sidra.ibge.gov.br/tabela/7060)
'''


##################################### TABELA 7060 #####################################

import requests
import pandas as pd

import numpy as np
from datetime import datetime
data1 = datetime(2020, 1, 1)
data2 = datetime(2020, 11, 1) + pd.DateOffset(months=1)
np_meses = np.arange(data1,data2, 1, dtype='datetime64[M]').astype(str)
li_meses = [s.replace('-','') for s in np_meses]
# dic_download = {}

for index, mês in enumerate(li_meses):
    print(mês)

    #mês = '201201'
    url = f'https://apisidra.ibge.gov.br/values/t/7060/n1/all/n6/all/v/63,66/p/{mês}/c315/all/d/v63%202,v66%204'
    r = requests.get(url)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    
    if index == 0:
        df_completo = df.copy()
    else:
        df_completo = df_completo.append(df)

for index_linha, linha in df_completo.iterrows():
    df_completo.loc[index_linha,'código'] = linha['D4N'].split(".")[0]

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = "t7060.csv"
df_completo.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)


##################################### TABELA 1419 #####################################

import requests
import pandas as pd

import numpy as np
from datetime import datetime
data1 = datetime(2012, 1, 1)
data2 = datetime(2019, 12, 1) + pd.DateOffset(months=1)
np_meses = np.arange(data1,data2, 1, dtype='datetime64[M]').astype(str)
li_meses = [s.replace('-','') for s in np_meses]

# dic_download = {}

for index, mês in enumerate(li_meses):
    print(mês)

    #mês = '201201'
    url = f'https://apisidra.ibge.gov.br/values/t/1419/n1/all/n6/all/v/63,66/p/{mês}/c315/all/d/v63%202,v66%204'
    r = requests.get(url)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    
    if index == 0:
        df_completo = df.copy()
    else:
        df_completo = df_completo.append(df)

for index_linha, linha in df_completo.iterrows():
    df_completo.loc[index_linha,'código'] = linha['D4N'].split(".")[0]

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = "t1419.csv"
df_completo.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)

##################################### TABELA 2938 #####################################

import requests
import pandas as pd

import numpy as np
from datetime import datetime
data1 = datetime(2006, 7, 1)
data2 = datetime(2011, 12, 1) + pd.DateOffset(months=1)
np_meses = np.arange(data1,data2, 1, dtype='datetime64[M]').astype(str)
li_meses = [s.replace('-','') for s in np_meses]

# dic_download = {}

for index, mês in enumerate(li_meses):
    print(mês)

    #mês = '201201'
    url = f'https://apisidra.ibge.gov.br/values/t/2938/n1/all/v/63,66/p/{mês}/c315/all/d/v63%202,v66%204'
    r = requests.get(url)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    
    if index == 0:
        df_completo = df.copy()
    else:
        df_completo = df_completo.append(df)

for index_linha, linha in df_completo.iterrows():
    df_completo.loc[index_linha,'código'] = linha['D4N'].split(".")[0]

pasta = caminho_base / 'Dados' / 'Ibge' / 'Tabelas'
arq_nome = "t2938.csv"
df_completo.to_csv(pasta / arq_nome, sep='|', decimal=',', index=False)









