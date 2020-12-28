# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:55:11 2020

@author: pedro
"""

nova_linha = pd.DataFrame({'col_data': pd.date_range(start=df_datas['col_data'].iloc[-1], periods=2, freq='MS', closed='right')})
df_datas = df_datas.append(nova_linha)


