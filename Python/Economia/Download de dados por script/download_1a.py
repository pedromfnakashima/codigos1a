# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:13:57 2020

@author: pedro
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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
os.chdir(caminho_wd)
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

import requests
import pandas as pd
url = "https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63,66/p/all/c315/all/d/v63%202,v66%204"
r = requests.get(url)
j = r.json()
df = pd.DataFrame.from_dict(j)

# ---------------------------------------

cond1 = df['D4N'] == 'Índice geral'
filtro = df.loc[cond1,:]

##########################################################################################################
##########################################################################################################
##########################################################################################################



















# ipeadatapy
# https://github.com/luanborelli/ipeadatapy
pip install ipeadatapy

import ipeadatapy

ipeadatapy.list_series()

igpdi = ipeadatapy.timeseries('IGP12_IGPDI12')

# sidrapy
# https://pypi.org/project/sidrapy/
# https://github.com/AlanTaranti/Sidrapy

#pip install sidrapy

import sidrapy

print(dir(sidrapy.get_table))

#data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="last 12")

#data = sidrapy.get_table(table_code="1419", territorial_level="1", ibge_territorial_code="all", period="all")

data = sidrapy.get_table(table_code="7060", territorial_level="1", ibge_territorial_code="all", period="all")

data = sidrapy.get_table(table_code="7060", variable="63", territorial_level="1", ibge_territorial_code="all", period="all")


data = sidrapy.get_table(table_code="7060", classification='all', variable="63", territorial_level="1", ibge_territorial_code="all", period="all")



import inspect
inspect.getargspec(sidrapy.get_table)


sidrapy.get_table.__code__.co_varnames


import inspect
inspect.getargspec(sidrapy.get_table)

inspect.signature(sidrapy.get_table)













