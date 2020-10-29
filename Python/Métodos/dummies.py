# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
"""
globals().clear()

import pandas as pd

s = pd.Series(list('abca')).to_frame()

print(pd.get_dummies(s))

dummies = pd.get_dummies(s)

s = s.merge(dummies, left_index=True, right_index=True)
