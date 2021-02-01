# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:00:10 2020

@author: pedro-salj

https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
"""



import pandas as pd

df = pd.DataFrame({'coluna_1': [10, 11, 12], 'coluna_2': [100, 110, 120]})

for index_linha, linha in df.iterrows():
    print(linha['coluna_1'], linha['coluna_2'])













