# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:50:44 2020

@author: pedro

Sites/tutoriais:
https://www.youtube.com/watch?v=YQf23JYX3Zw
https://datatofish.com/multiple-linear-regression-python/
https://medium.com/@hsrinivasan2/linear-regression-in-scikit-learn-vs-statsmodels-568b60792991
https://www.kaggle.com/agailloty/linear-regression-with-sklearn-and-statsmodel
http://marcharper.codes/2016-06-14/Linear+Regression+with+Statsmodels+and+Scikit-Learn.html
"""
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
caminho_wd = caminho_base / 'Dados' / 'Stata'
print('\nDiretório anterior:\n', os.getcwd())
os.chdir(caminho_wd)
print('\nDiretório atual:\n', os.getcwd())

import pandas as pd
import numpy as np

df = pd.read_stata('auto.dta')
print(df.shape)
df = df.dropna()
print(df.shape)

dummies = pd.get_dummies(df['foreign'])

df = df.merge(dummies, left_index=True, right_index=True)

y = df[['price']]
X = df[['mpg', 'weight', 'length', 'Foreign', 'rep78']]

# Com sklearn

from sklearn import linear_model as lm

model = lm.LinearRegression()
results = model.fit(X,y)

print(model.intercept_, model.coef_)

# Com statsmodels

import statsmodels.api as sm

X = sm.add_constant(X)

model = sm.OLS(y,X).fit()

print(model.summary())


################################
################################
################################
import pandas as pd
import numpy as np

df = pd.read_stata('auto.dta')
df = df.dropna()

d_foreign = pd.get_dummies(df['foreign'])
d_rep78 = pd.get_dummies(df['rep78'], prefix='rep', drop_first=True)

df = pd.concat([df, d_foreign, d_rep78], axis=1)

y = df[['price']]
X = df[['mpg', 'weight', 'length', 'Foreign', 'rep_2.0', 'rep_3.0', 'rep_4.0', 'rep_5.0']]


import statsmodels.api as sm

X = sm.add_constant(X)

model = sm.OLS(y,X).fit()

print(model.summary())




