
import pandas as pd
import numpy as np


df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': range(3), 'C': [.1, .2, .3]})

gr = df.groupby('A')

gr.agg({'B': {'b_sum': 'sum'}, 'C': {'c_mean': 'mean', 'c_count': 'count'}})

##################################################
# Como eveitar a mensagem de warning (abaixo)
"""
"using a dict with renaming is deprecated and will be removed in a future version" groupby agg
"""
# https://stackoverflow.com/questions/44635626/rename-result-columns-from-pandas-aggregation-futurewarning-using-a-dict-with

df = pd.DataFrame({"User": ["user1", "user2", "user2", "user3", "user2", "user1", "user3"],
                   "Amount": [10.0, 5.0, 8.0, 10.5, 7.5, 8.0, 9],
                   'Score': [9, 1, 8, 7, 7, 6, 9]})

"""
create custom function that returns a Series
The variable x inside of my_agg is a DataFrame
"""
def my_agg(x):
    names = {
        'Amount mean': x['Amount'].mean(),
        'Amount std':  x['Amount'].std(),
        'Amount range': x['Amount'].max() - x['Amount'].min(),
        'Score Max':  x['Score'].max(),
        'Score Sum': x['Score'].sum(),
        'Amount Score Sum': (x['Amount'] * x['Score']).sum()}

    return pd.Series(names)

"""
Pass this custom function to the groupby apply method
"""
df.groupby('User').apply(my_agg)


agregado = df.groupby('User').apply(my_agg)

"""
The big downside is that this function will be much slower
than agg for the cythonized aggregations
"""




##################################################
# Filter
# 

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
                   'B' : [1, 2, 3, 4, 5, 6],
                   'C' : [2.0, 5., 8., 1., 2., 9.]})
grouped = df.groupby('A')
grouped.filter(lambda x: x['B'].mean() > 3.)

##################################################
# Groupby, datas e agregações
#####################################

import pandas as pd
import numpy as np


df = pd.DataFrame({
        'datas': pd.date_range(start='2018-01-01', end='2019-12-31', periods=72),
        'numeros1': np.random.randint(low=1, high=100, size=72),
        'numeros2': np.random.randint(low=1, high=100, size=72)
        })
df['ano'] = datas.year
df['mes'] = datas.month

def minha_agregacao(x):
    names = {
        'numeros1_maximo': x['numeros1'].max(),
        'numeros1_minimo': x['numeros1'].min(),
        'numeros1_soma': x['numeros1'].sum(),
        'numeros1_contagem': x['numeros1'].count(),
        'numeros1_media': x['numeros1'].mean(),
        'numeros1_dp': x['numeros1'].std(),
        'numeros2_maximo': x['numeros2'].max(),
        'numeros2_minimo': x['numeros2'].min(),
        'numeros2_soma': x['numeros2'].sum(),
        'numeros2_contagem': x['numeros2'].count(),
        'numeros2_media': x['numeros2'].mean(),
        'numeros2_dp': x['numeros2'].std()
        }

    return pd.Series(names)

"""
Pass this custom function to the groupby apply method
"""
minha_agregacao = df.groupby(['ano', 'mes']).apply(minha_agregacao)

"""
SELEÇÃO DE MULTIINDEX
ver arquivo pandas_index.py
"""
minha_agregacao.loc[(2018,2)]
minha_agregacao.loc[(2018,1)]

minha_agregacao.loc[(2018,3), ['numeros1_maximo', 'numeros2_maximo']]

"""
PASSAR DADOS DO INDEX PARA AS COLUNAS
ver arquivo pandas_index.py
"""
minha_agregacao.head() # nomes dos index: ano e mes
minha_agregacao.index

minha_agregacao_sem_index = minha_agregacao.reset_index() # nomes dos index (ano e mes) viram colunas. index passa a ser range()

minha_agregacao_sem_index.loc[(minha_agregacao_sem_index.ano==2018) & (minha_agregacao_sem_index.mes==1), :]
# Sem o parenteses dá erro!!!

filtro = (minha_agregacao_sem_index.ano==2018)\
    & (minha_agregacao_sem_index.mes.isin([1,2]))

minha_agregacao_sem_index.loc[filtro, :]

"""
Para o exemplo das eleiçoes. Eleito por QP ou ou maioria

df.resultado.isin(['eleito por QP', 'eleitor por outra forma'])

"""


