# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:39:16 2020

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
caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos' / 'microdados' / 'csv'
#caminho_wd = caminho_base / 'Dados' / 'trabalho' / 'caged_vinculos_2002-2009'# / 'temp1'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())
import numpy as np
import pandas as pd

##########################################################################################################
##########################################################################################################
##########################################################################################################

# Criar datetime a partir dos componentes
df_bruto['mês'] = pd.to_datetime(df_bruto[['year', 'month', 'day']])

import numpy as np
import pandas as pd
print(pd.date_range('2020-01-01', periods=7, freq='M'))

print(np.arange('2018-01-01','2020-12-01', 1, dtype='datetime64[M]'))

import numpy as np
import pandas as pd
np_datas = np.arange('2018-01-01','2021-01-01', 1, dtype='datetime64[M]')
meses = pd.to_datetime(np_datas).to_frame()
meses.rename(columns={0:'mês'}, inplace=True)
meses.set_index('mês',inplace=True)












