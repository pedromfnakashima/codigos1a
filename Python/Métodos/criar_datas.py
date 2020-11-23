# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:39:16 2020

@author: pedro-salj
"""
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












