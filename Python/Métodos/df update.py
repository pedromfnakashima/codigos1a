# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:12:05 2020

@author: pedro
"""

import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.array([[np.nan, 1], [np.nan, 1], [3, 1]]),
                   columns=['a', 'b'])

df1.drop([0], axis=0, inplace=True)

df2 = pd.DataFrame(np.array([[2, 1, 0], [2, 1, 1], [3, 2, 0], [5,5,2]]),
                   columns=['a', 'b', 'c'])

df1.update(df2, overwrite=True)


print(np.arange('2020-01-01','2020-07-01', 1, dtype='datetime64[M]'))



dfx1 = pd.DataFrame(np.arange('2020-01-01','2021-01-01', 1, dtype='datetime64[M]'))
dfx1.set_index(0, inplace=True)
dfx1['var1'] = np.nan


dfx2 = pd.DataFrame(np.arange('2015-01-01','2020-12-01', 1, dtype='datetime64[M]'))
dfx2.set_index(0, inplace=True)
dfx2['var1'] = np.nan

dfx2.loc['2020-10-01', 'var1'] = 5

dfx1.update(dfx2)


dfx1 = pd.DataFrame(np.arange('2015-01-01','2020-12-01', 1, dtype='datetime64[M]'))


del df1, df2, dfx1, dfx2









