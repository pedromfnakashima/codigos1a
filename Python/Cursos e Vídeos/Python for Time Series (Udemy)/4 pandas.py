# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:48:02 2020

@author: pedro

A diferença entre np.array
e pd.series é que o último
tem index, que são labels
"""

# PANDAS SERIES

globals().clear()

import pandas as pd
import numpy as np

mylist = [10, 20, 30]
labels = ['a', 'b', 'c']

np_arr = np.array(mylist)
pd_series = pd.Series(data = mylist)
pd_series = pd.Series(data = mylist, index = labels)

print(np_arr)
print(pd_series)

print(np_arr + 5)
print(pd_series + 5)

""" Operações com base no index """

ser1 = pd.Series([1,2,3,4], index=['USA', 'Germany', 'USSR', 'Japan'])

print(ser1['USA'])

ser2 = pd.Series([1,4,5,6], index=['USA', 'Germany', 'Italy', 'Japan'])

print(ser2)

print(ser1 + ser2)

# DATA FRAMES
""" pd.Series que compartilham
do mesmo index """
globals().clear()
import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

rand_mat = randn(5,4)
print(rand_mat)

df = pd.DataFrame(data=rand_mat)
print(df)

print('A B C D E'.split())

df = pd.DataFrame(data=rand_mat, index='A B C D E'.split())
print(df)

df = pd.DataFrame(data=rand_mat, index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

""" Cada coluna individual é
um pd.Series """
print(df['W'])
print(type(df['W']))

"""  """
mylist = ['W', 'Y']
print(df[mylist])

print(df[['W', 'Y']])
print(df[['Y', 'W']])

""" Criando uma nova coluna """

df['NEW'] = df['W'] + df['W']
print(df)

""" Removendo uma coluna """
df.drop('NEW', axis=1, inplace=True)

""" Removendo uma linha """
df.drop('A', axis=0, inplace=True)

""" Selecionando linhas """
print(df.loc['B'])
print(df.iloc[0])

print(df.loc[['B', 'C']])
print(df.loc[['B', 'C'],:])
print(df.iloc[[0,2],:])

""" Selecionando colunas """
print(df.loc[:,['Y', 'Z']])

""" Selecionando linhas e colunas """
print(df.loc[['B','C'],['Y', 'Z']])

""" Seleção condicional """
globals().clear()
import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)
rand_mat = randn(5,4)
df = pd.DataFrame(data=rand_mat, index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

print(df>0)

df_bool = df > 0
print(df[df_bool])

print(df[df>0])

""" Filtro onde W > 0 """
print(df['W'] > 0)
print(df[df['W']>0])
print(df[df['W']>0]['Y'])
print(df[df['W']>0]['Y'].loc['A'])

""" Filtro com duas condições
Ao contrário do Python, NÃO
funcionam aqui os operadores
'and' e 'or'.
Ao contrário, funciona '&' e '|'
"""
cond1 = df['W'] > 0
cond2 = df['Y'] > 1

print(df[cond1 & cond2])
print(df[cond1 | cond2])
print(df[(cond1) & (cond2)])
print(df[ (df['W']>0) & (df['Y']>1) ])

""" Resetando o index
Gera uma nova coluna com o index"""
print(df)
print(df.reset_index(inplace=True))
print(df)


""" Fazendo uma coluna virar
o index
ATENÇÃO:
PERDE o index original.
Para não perder o index
original, é necessário usar
antes o reset_index"""
new_ind = 'CA NY WY OR CO'.split()
print(new_ind)

df['States'] = new_ind

df.set_index('States', inplace=True)

""" Informações sobre o DF """
print(df.info())
print(df.dtypes)
print(df.describe())

""" Quantas linhas cumprem
uma condição """
print(df['W'] > 0)
ser_w = df['W'] > 0

print(ser_w.value_counts())
print(sum(ser_w))

""" 16 MISSING DATA """
globals().clear()
import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]})

print(df)

""" Exclui qualquer linha
que tem missing """
print(df.dropna())
""" Exclui qualquer coluna
que tem missing """
print(df.dropna(axis=1))

""" tresh
deletar linha com a partir
de 2 nan"""
print(df.dropna(thresh=2))

""" fillna """
print(df.fillna(value='ALGUM'))

print(df.fillna(value=0))

""" Preenchendo com a média
da coluna"""
print(df.mean())

print(df.fillna(df.mean()))

""" Preenchendo com a média
da linha"""

print(df['A'].fillna(value=df['A'].mean()))

""" 17 Group By Operations """
globals().clear()
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)

print(df.groupby('Company').mean())

print(df.groupby('Company').max())

print(df.groupby('Company').std())

print(df.groupby('Company').describe())

print(df.groupby('Company').describe().transpose())

# De anteriormente (não tá na aula)
def minha_agregacao(x):
    novo = {
        'soma': x['Sales'].sum(),
        'max': x['Sales'].max(),
        'min': x['Sales'].min()
        }
    return pd.Series(novo)

df_resultado = df.groupby(['Company']).apply(minha_agregacao)

""" 18 Common Operations """
globals().clear()
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[444,555,666,444], 'col3':['abc','def','ghi','xyz']})
print(df)

print(df['col2'].unique())
print(df['col2'].nunique())

print(df['col2'].value_counts())

""" col1 > 2, col2 == 444"""
newdf = df[ (df['col1']>2) & (df['col2']==444) ]
print(newdf)

""" Aplicando função a cada
valor da coluna """
def times_two(number):
    return number*2

print(times_two(4))

print(df['col1'].apply(times_two))

df['new'] = df['col1'].apply(times_two)

del df['new']

print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print(df.sort_values(by='col2'))
print(df.sort_values('col2'))

print(df.sort_values(by='col2', ascending=False))

""" read_html
pandas lê todas tabelas do html"""
mylist_of_tables = pd.read_html('https://www.fdic.gov/Bank/individual/failed/banklist.html')

print(type(mylist_of_tables))
print(len(mylist_of_tables))
