
"""
https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm
"""

#import the pandas library
import pandas as pd
import numpy as np

df = pd.DataFrame({'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]})

print(df.groupby('Team').groups)
print(df.groupby(['Team','Year']).groups)

grouped = df.groupby('Year')

for name,group in grouped:
   print(name)
   print(group)

print(grouped.get_group(2014))

print(grouped['Points'].agg(np.mean))


grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))


df
print(df.groupby('Team').filter(lambda x: len(x) >= 3)) # x é o df pequeno


df.groupby('Team').first()

df = df.sort_values(['Team', 'Points'], ascending=[True,False])

segundo_maior = df.groupby('Team').nth(1)

dois_elementos = df.groupby('Team').head(2)



#######################################
#######################################
#######################################








































