
import pandas as pd
import numpy as np



# nth
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.nth.html

df = pd.DataFrame({'A': [1, 1, 2, 1, 2],
                   'B': [np.nan, 2, 3, 4, 5]}, columns=['A', 'B'])

g = df.groupby('A')
g.nth(0)

g.nth(1)

g.nth(-1)

g.nth([0, 1])

g.nth(0, dropna='any')

g.nth(3, dropna='any')

df.groupby('A', as_index=False).nth(1)

# nlargest
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.SeriesGroupBy.nlargest.html?highlight=nlargest#pandas.core.groupby.SeriesGroupBy.nlargest

countries_population = {"Italy": 59000000, "France": 65000000,
                        "Malta": 434000, "Maldives": 434000,
                        "Brunei": 434000, "Iceland": 337000,
                        "Nauru": 11300, "Tuvalu": 11300,
                        "Anguilla": 11300, "Monserat": 5200}
s = pd.Series(countries_population)

s

s.nlargest()

s.nlargest(3)

s.nlargest(3, keep='first')

s.nlargest(3, keep='last')

s.nlargest(3, keep='all') # é o maisa adequado para a maior parte dos propósitos

# Ranking
s
s.rank(ascending=False)

s.count()









