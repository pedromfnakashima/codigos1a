# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:54:50 2020

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
    print('\nLogado de casa')
    caminho_base = Path(r'D:\Códigos, Dados, Documentação e Cheat Sheets')
elif getpass.getuser() == "pedro-salj":
    print('\nLogado da salj-alems')
    caminho_base = Path(r'C:\Users\pedro-salj\Desktop\Pedro Nakashima\Códigos, Dados, Documentação e Cheat Sheets')

""" Mudar diretório para dados Stata"""
caminho_wd = caminho_base / 'Dados' / 'Stata' 
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

auto = pd.read_stata('auto.dta')

##################################

X = auto.loc[:, ['mpg', 'weight', 'length']]
y = auto.loc[:, ['price']]
X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()

print(results.summary())

###################################

X = auto.loc[:, ['mpg', 'weight', 'length', 'turn']]
y = auto.loc[:, ['price']]
X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()

print(results.summary())

###################################

print(auto['rep78'].value_counts().sort_values(ascending=False))
print(auto['rep78'].value_counts(normalize=True).sort_values(ascending=False))

print(auto['foreign'].value_counts().sort_values(ascending=False))
print(auto['foreign'].value_counts(normalize=True).sort_values(ascending=False))

###################################

""" Naive inclusion of categorical """

X = auto.loc[:, ['mpg', 'weight', 'length', 'foreign', 'rep78']]
y = auto.loc[:, ['price']]
X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()

print(results.summary())

"""   """
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer

bin_encoder = LabelBinarizer()

lab_encoder = LabelEncoder()

scale_mapper = {'Domestic': 0, 'Foreign': 1}

X['foreign'].replace(scale_mapper, inplace=True)

""" Lidando com missing """


""" Transformando categorias em dummies  """
# Posição 298

data_2 = X.copy()

one_hot = OneHotEncoder()

new_data = one_hot.fit_transform(data_2[['rep78']]).toarray()






