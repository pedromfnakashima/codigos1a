# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:23:11 2020

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

""" Mudar diretório"""
caminho_wd = caminho_base / 'Dados'
os.chdir(caminho_wd)
# --------------------------------------------------------------
import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')














# --------------------------------------------------------------

import pandas as pd

series = [('Stranger Things', 3, 'Millie'),
          ('Game of Thrones', 8, 'Emilia'), ('La Casa De Papel', 4, 'Sergio'),
          ('Westworld', 3, 'Evan Rachel'), ('Stranger Things', 3, 'Millie'),
         ('La Casa De Papel', 4, 'Sergio')]

# Create a DataFrame object
dfObj = pd.DataFrame(series, columns=['Name', 'Seasons', 'Actor'])
print(dfObj)

# ----------------------------------------------------------------

import pandas as pd

series = [('Stranger Things', 3, 'Millie'),
          ('Game of Thrones', 8, 'Emilia'), ('La Casa De Papel', 4, 'Sergio'),
          ('Westworld', 3, 'Evan Rachel'), ('Stranger Things', 3, 'Millie'),
         ('La Casa De Papel', 4, 'Sergio')]

# Create a DataFrame object
dfObj = pd.DataFrame(series, columns=['Name', 'Seasons', 'Actor'])

# Find a duplicate rows
duplicados_VF_first = dfObj.duplicated(keep='first')
duplicateDFRow = dfObj[dfObj.duplicated()]
print(duplicateDFRow)

# ----------------------------------------------------------------
import pandas as pd

series = [('Stranger Things', 3, 'Millie'),
          ('Game of Thrones', 8, 'Emilia'), ('La Casa De Papel', 4, 'Sergio'),
          ('Westworld', 3, 'Evan Rachel'), ('Stranger Things', 3, 'Millie'),
         ('La Casa De Papel', 4, 'Sergio')]

# Create a DataFrame object
dfObj = pd.DataFrame(series, columns=['Name', 'Seasons', 'Actor'])

# Find a duplicate rows
duplicados_VF_last = dfObj.duplicated(keep='last')
duplicateDFRow = dfObj[duplicados_VF_last]

print(duplicateDFRow)
















