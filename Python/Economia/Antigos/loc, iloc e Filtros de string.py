"""
https://www.youtube.com/watch?v=2AFGPdNn4FM
How do I filter rows of a pandas DataFrame by column value?
"""
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.head()
movies.shape

is_long = movies.duration >= 200
is_long.head()

movies[is_long]

movies[movies.duration >= 200]

movies[movies.duration >= 200].genre
movies[movies.duration >= 200]['genre']

movies.loc[movies.duration >= 200, 'genre']

"""
https://www.youtube.com/watch?v=xvpNA7bC8cs&t=770s
How do I select multiple rows and columns from a pandas DataFrame?
"""

import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')

ufo.head(3)

ufo.loc[0,:]

ufo.loc[[0,1,2], :]

ufo.loc[0:2, :]

ufo.loc[:, 'City']

ufo.loc[:, ['City', 'State']]

ufo.loc[:, 'City':'State']

ufo.loc[0:2, 'City':'State']

ufo.head(3).drop('Time', axis='columns')
ufo.head(3).drop(['Time', 'State'], axis='columns')
ufo.head(3).drop(['Time', 'State'], axis=1)

"""
DataFrame.drop()
Ver:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
"""

ufo.loc[ufo.City=='Oakland', :]

ufo.loc[ufo.City=='Oakland', 'State']

ufo.iloc[:, [0,3]]

ufo.iloc[:, 0:4]

ufo.iloc[0:3, :]

ufo.loc[:, ['City', 'State']]
ufo.iloc[0:2, :]


"""
FILTROS DE STRING
str.contains:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains
"""

import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')

movies.loc[:,['title', 'genre']]

movies.loc[movies.title.str.contains('Pulp'),['title', 'genre']]

movies.loc[movies.title.str.contains('pulp', case=False),['title', 'genre']]

movies.loc[movies.title.str.contains('star', case=False),['title', 'genre']]

import re
movies.loc[movies.title.str.contains('star', regex=True, flags=re.IGNORECASE),['title', 'genre']]

movies.loc[movies.title.str.contains('\d{4}', regex=True, flags=re.IGNORECASE),['title', 'genre']]

titulo = movies.title.str.contains('\d{4}', regex=True, flags=re.IGNORECASE)
movies.loc[titulo,['title', 'genre']]


"""
Contagem de valores
"""
movies.genre.value_counts()
movies.genre.value_counts(normalize=True)




"""

"""






"""

"""







"""

"""








"""

"""













