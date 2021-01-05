# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:14:42 2020

@author: pedro

TICK LOCATORS

######################################################################
Arquivo 6 Time series.py (curso udemy):

from matplotlib import dates

ax = df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60], figsize=(12,5))
ax.set(xlabel='')

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b')) #\n representa uma nova linha

######################################################################
https://stackoverflow.com/questions/28810403/how-can-i-set-the-location-of-minor-ticks-in-matplotlib

######################################################################
https://www.geeksforgeeks.org/matplotlib-ticker-fixedlocator-class-in-python/#:~:text=FixedLocator%20class%20is%20a%20subclass,or%20equal%20to%20nbins%20%2B%201.



"""

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib 
import seaborn as sns
   
  
np.arange(0, 15, 5) 
plt.figure(figsize = [6,4]) 
   
x = np.array([1, 2, 3, 4, 5, 
              6, 7, 8, 9, 10, 
              11, 12, 13, 14, 15]) 
  
y = np.array([15, 16, 17, 18,  
              19, 20, 40, 50,  
              60, 70, 80, 90,  
              100, 110, 120]) 
  
ax = sns.pointplot(x, y, 
                   color = 'k', 
                   markers = ["."],  
                   scale = 2) 
  
ax.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([1,5,8])) 
  
plt.show() 

###############################################################
# https://stackoverflow.com/questions/21281322/how-to-plot-a-pandas-multiindex-dataframe-with-all-xticks

idx = pd.date_range("2013-01-01", periods=1000)
val = np.random.rand(1000)
s = pd.Series(val, idx)

g = s.groupby([s.index.year, s.index.month]).mean()

ax = g.plot()
ax.set_xticks(range(len(g)));
ax.set_xticklabels(["%s-%02d" % item for item in g.index.tolist()], rotation=90);


















