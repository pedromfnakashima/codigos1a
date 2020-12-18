# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:00:23 2020

@author: pedro
"""
import pandas as pd

df_teste1 = pd.DataFrame({'a':[2,3],'b':[2,5]})
df_teste2 = pd.DataFrame({'a':[3,4],'b':[5,6]})

df_mult = (df_teste1 * df_teste2) / 100


