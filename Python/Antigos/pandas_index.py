########################################################################
# Pandas .reindex ######################################################
########################################################################

"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex.html
"""
import pandas as pd
import numpy as np

index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
df = pd.DataFrame({
        'http_status': [200,200,404,404,301],
        'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]},
index=index)

"""
Create a new index and reindex the dataframe.
By default values in the new index that do not have
corresponding records in the dataframe are assigned NaN.
"""

new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']
df.reindex(new_index)

"""
We can fill in the missing values by passing a value
to the keyword fill_value. Because the index is not
monotonically increasing or decreasing, we cannot use
arguments to the keyword method to fill the NaN values.
"""

df.reindex(new_index, fill_value=0)

df.reindex(new_index, fill_value='missing')

"""
We can also reindex the columns.
"""

df.reindex(columns=['http_status', 'user_agent'])

"""
Or we can use “axis-style” keyword arguments
"""

df.reindex(['http_status', 'user_agent'], axis="columns")
df.reindex(new_index, axis="rows")

"""
To further illustrate the filling functionality in reindex,
we will create a dataframe with a monotonically increasing
index (for example, a sequence of dates).
"""

import pandas as pd
import numpy as np

date_index = pd.date_range('1/1/2010', periods=6, freq='D')
df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
                    index=date_index)
df2

"""
Suppose we decide to expand the dataframe to cover a wider date range.
"""

date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
df2.reindex(date_index2)

"""
The index entries that did not have a value in the original
data frame (for example, ‘2009-12-29’) are by default filled
with NaN. If desired, we can fill in the missing values using
one of several options.

For example, to back-propagate the last valid value to fill
the NaN values, pass bfill as an argument to the method keyword.
"""

df2.reindex(date_index2, method='bfill')

"""
Please note that the NaN value present in the original
dataframe (at index value 2010-01-03) will not be filled
by any of the value propagation schemes. This is because
filling while reindexing does not look at dataframe values,
but only compares the original and desired indexes. If you
do want to fill in the NaN values present in the original
dataframe, use the fillna() method.
"""

########################################################################
# Pandas index #########################################################
########################################################################

# What do I need to know about the pandas index? (Part 1)
# https://www.youtube.com/watch?v=OYZNk7Z9s6I&t=2s

import pandas as pd
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

drinks.index
drinks.columns

drinks.shape

drinks[drinks.continent == 'South America']

drinks.loc[23, 'beer_servings']

drinks.set_index('country', inplace=True)

drinks.head()

drinks.index
drinks.columns

drinks.shape

drinks.loc['Brazil'] # Procura pelo índice Brazil

drinks.loc['Brazil', 'beer_servings']

drinks.index.name = None # deleta o nome do index
drinks.head()

drinks.index.name = 'country' # muda o nome do index para country
drinks.head()

drinks.reset_index(inplace=True) # o que era index, vira variável. Novo index = range(0,n)
drinks.head()

"""
IMPORTANTE!
Antes de fazer df.reset_index(inplace=True),
o index precisa ter um nome, ou seja, tem que
fazer df.index.name = 'Algum nome'
"""

drinks.describe()
drinks.describe().index
drinks.describe().columns

drinks.describe().loc['25%', 'beer_servings']

# What do I need to know about the pandas index? (Part 2)
# https://www.youtube.com/watch?v=15q-is8P_H4

drinks.head()
drinks.continent.head()

drinks.set_index('country', inplace=True)
drinks.head()

drinks.continent.head()

drinks.continent.value_counts() # é uma series -> tem index e values

drinks.continent.value_counts().index
drinks.continent.value_counts().values


drinks.continent.value_counts()['Africa']
"""
Quantas vezes Africa aparece?
Naquela série, encontre o index Africa, e me mostre
o valor.
"""

# Ordena pelos values
drinks.continent.value_counts().sort_values()
drinks.continent.value_counts().sort_values(ascending=False)

# Ordena pelo index
drinks.continent.value_counts().sort_index()
drinks.continent.value_counts().sort_index(ascending=False)

people = pd.Series([3000000,85000], index=['Albania', 'Andorra'], name='population')
people

"""
Total de beer_servings para cada país 
"""

drinks.beer_servings

drinks.beer_servings * people

"""
Adicionar essa nova series ao dataframe:
"""
pd.concat([drinks,people], axis='columns')

pd.concat([drinks,people], axis='columns').head()

########################################################################
# Pandas multiindex ####################################################
########################################################################

# How do I use the MultiIndex in pandas?
# https://www.youtube.com/watch?v=tcRGa2soc-c

import pandas as pd

stocks = pd.read_csv('http://bit.ly/smallstocks')

stocks
stocks.dtypes
stocks.index

stocks.groupby('Symbol').Close.mean()

stocks.groupby(['Symbol', 'Date']).Close.mean()

serie = stocks.groupby(['Symbol', 'Date']).Close.mean()
serie # é uma series com multiindex

serie.index

"""
Para transformar um multindex em dataframe,
basta usar o comando unstack()
"""

df = serie.unstack()

"""
Outra forma:
"""
df = stocks.pivot_table(values='Close', index='Symbol', columns='Date')

serie

"""
Selecionar um nível de FORA
Selecionar todos Symbol = 'AAPL'
o nível externo
"""

serie.loc['AAPL']
serie.loc['AAPL', '2016-10-03']


"""
Selecionar um nível de DENTRO
Selecionar todas as Date = '2016-10-03'
"""
serie.loc[:, '2016-10-03']

serie

"""
Depois de transformar a series multiindex em
dataframe, a forma de acessar um elemento é a
mesma.
"""

df.loc['AAPL']
df.loc['AAPL', '2016-10-03']
df.loc[:, '2016-10-03']


"""
Criando um multiindex
"""

stocks
stocks.set_index(['Symbol', 'Date'], inplace=True)

stocks.index


"""
Ordenar.
Primeiro pelo index externo e depois pelo index
interno.
"""

stocks.sort_index(inplace=True)
stocks

"""
Fazendo seleções com um df multiindex
"""

stocks.loc['AAPL']

stocks.loc['AAPL', '2016-10-03']

stocks.loc[('AAPL', '2016-10-03'),:]

stocks.loc[('AAPL', '2016-10-03'),'Close']

"""
Pegando dados de:
    - várias ações, AAPL e MSFT (nível externo)
    - 1 dia (nível interno)
"""

stocks.loc[(['AAPL', 'MSFT'], '2016-10-03'), :]

stocks.loc[(['AAPL', 'MSFT'], '2016-10-03'), 'Close']

"""
Pegando dados de:
    - 1 ação, AAPL (nível externo)
    - vários dias (nível interno)
"""

stocks.loc[('AAPL', ['2016-10-03', '2016-10-04']), :]

stocks.loc[('AAPL', ['2016-10-03', '2016-10-04']), 'Close']

"""
Pegando dados de:
    - várias ações, AAPL e MSFT (nível externo)
    - vários dias (nível interno)
"""

stocks.loc[(['AAPL', 'MSFT'], ['2016-10-03', '2016-10-04']), :]


"""
Pegando dados de:
    - Várias ações (nível externo)
    - TODOS os dias (nível interno)
Pela forma tradicional, dá ERRO!
Ver sites:
    https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
"""

stocks.loc[(:, ['2016-10-03', '2016-10-04']), :]
# Dá ERRO!

stocks.loc[(slice(None), ['2016-10-03', '2016-10-04']), :]
# Dá ERRO!



"""
Juntar DF's com multindex com o MERGE
Ver sites:
    https://www.datacamp.com/community/tutorials/joining-dataframes-pandas
    https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
Merge com:
    - Dois df com o mesmo index (multindex)
    - Colunas diferentes
"""

import pandas as pd
close = pd.read_csv('http://bit.ly/smallstocks', usecols=[0,1,3], index_col=['Symbol', 'Date'])
volume = pd.read_csv('http://bit.ly/smallstocks', usecols=[0,2,3], index_col=['Symbol', 'Date'])

close
volume

ambos = pd.merge(close, volume, left_index=True, right_index=True)
ambos

"""
Tidy data
Os index tem que ter NOMES
"""
ambos.reset_index()

# EXCLUINDO NÍVEIS

# excluir o primeiro nível do MultiIndex (df)
df.columns = df.columns.droplevel(level=0)

# excluir o primeiro nível do MultiIndex (series)
series = series.droplevel(level=0)

serie
serie.droplevel(level=0) # exclui o primeiro nível
serie.droplevel(level=1) # exclui o segundo nível

"""
Ver: pandas.MultiIndex.remove_unused_levels
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels
"""

#############################################
#############################################
#############################################

"""
pandas Time Series Basics
https://chrisalbon.com/python/data_wrangling/pandas_time_series_basics/
"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as pyplot


data = {'date': ['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'], 
        'battle_deaths': [34, 25, 26, 15, 15, 14, 26, 25, 62, 41]}
df = pd.DataFrame(data, columns = ['date', 'battle_deaths'])
print(df)
df.dtypes

"""
Converter df['date'] de string para datetime
"""

df['date'] = pd.to_datetime(df['date'])
df.dtypes

"""
Fazer df['date'] de index e deletar a coluna
"""

# FORMA 1 (melhor)
df.set_index('date', inplace=True)
"""
# Operação inversa
df.reset_index(inplace=True)

# FORMA 2
df = pd.DataFrame(data, columns = ['date', 'battle_deaths'])
df['date'] = pd.to_datetime(df['date'])

df.index = df['date']
del df['date']
df

# Operação inversa
df['date'] = df.index
df.index = range(len(df))
"""
df.dtypes
df
"""
Continuando a partir da FORMA 1 (ida)
Observações que ocorreram em 2014
"""
df['2014']

df.loc['2014']

"""
Observações que ocorreram em Maio de 2014
"""
df['2014-05']

df.loc['2014-05']

"""
Observações após 3 de maio de 2014
(INCLUSIVO)
"""
df[datetime(2014, 5, 3):]

df.loc[datetime(2014, 5, 3):]
df.loc[datetime(2014, 5, 3):,:]

"""
Observações entre 3 de maio de 2014 e 4 de maio de 2014
(INCLUSIVO DOS DOIS LADOS)
"""
df['5/3/2014':'5/4/2014']

df.loc['5/3/2014':'5/4/2014']
df.loc['5/3/2014':'5/4/2014',:]

"""
Excluir observações após 2 de maio de 2014
"""
df
df.truncate(after='5/3/2014')

"""
Observações de maio de 2014
"""
df['5-2014']

"""
Contar o número de observações por datetime
"""
df.groupby(level=0).count()
"""
Média de battle_deaths por dia
"""
df
df.resample('D').mean()
"""
Soma de battle_deaths por dia
"""
df
df.resample('D').sum()
"""
Plotar o total de battle_deaths por dia
"""

df.resample('D').sum().plot()

"""

"""


from pandas_datareader import data

goog = data.DataReader('GOOG', start='2004', end='2016',
                       data_source='google')



"""

"""
