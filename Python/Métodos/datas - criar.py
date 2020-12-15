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
pd_datas = pd.to_datetime(np_datas)
df_1 = pd.DataFrame(pd_datas)
df_1.rename(mapper={0:'novo_nome'},axis=1,inplace=True)

# Adiciona uma nova linha
nova_linha = pd.DataFrame({'novo_nome': pd.date_range(start=df_1['novo_nome'].iloc[-1], periods=2, freq='MS', closed='right')})
df_1 = df_1.append(nova_linha)





df_1.loc[df_1.index[-1],'novo_nome'] = 5

df_1.loc[df_1.index[-1],'novo_nome'] = df_1['novo_nome'] - pd.DateOffset(months=1)




# Como adicionar um mês???

print(pd_datas.columns)


df['data_inicio_periodo'] - pd.DateOffset(months=num)


##########################################################################################################
##########################################################################################################
##########################################################################################################


df['dt'] = pd.to_datetime(df[['year', 'month', 'day']])



df['dt'] = df['Data'].astype('datetime64[ns]')
# https://stackoverflow.com/questions/17134716/convert-dataframe-column-type-from-string-to-datetime-dd-mm-yyyy-format#:~:text=If%20your%20date%20column%20is,to%20convert%20it%20to%20datetime.&text=You%20can%20try%20it%20with,but%20at%20least%20this%20works.&text=More%20details%20on%20format%20here,html%23strftime%2Dstrptime%2Dbehavior















