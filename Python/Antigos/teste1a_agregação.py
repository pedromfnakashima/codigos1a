
# https://github.com/pandas-dev/pandas/issues/18366

import pandas as pd
import numpy as np
from pandas.compat import StringIO

csv = r'''Alguma linha inútil
Outra linha inútil
"cat";"distance";"energy"
"A";"1,20";"1,80"
"A";"1,50";"1,95"
"A";"1,74";"2,04"
"B";"0,82";"1,25"
"B";"1,01";"1,60"
"C";"0,60";"1,01"
Linha final inútil
Outra linha final inútil
'''

mydf = pd.read_csv(StringIO(csv),
                 header=2,
                 skipfooter=2,
                 delimiter = ';',
                 decimal = ",",
                 engine = "python")

mydf.dtypes


################################################################
########### Antes era assim (deprecado) ########################
################################################################
import numpy as np
import statsmodels.robust as smrb
from functools import partial
 
# median absolute deviation as a partial function
# in order to demonstrate the issue with partial functions as aggregators
mad_c1 = partial(smrb.mad, c=1)

# renaming and specifying the aggregators at the same time
# note that I want to choose the resulting column names myself
# for example "total_xxxx" instead of just "sum"
mydf_agg = mydf.groupby('cat').agg({
    'energy': {
        'total_energy': 'sum',
        'energy_p98': lambda x: np.percentile(x, 98),  # lambda
        'energy_p17': lambda x: np.percentile(x, 17),  # lambda
    },
    'distance': {
        'total_distance': 'sum',
        'average_distance': 'mean',
        'distance_mad': smrb.mad,   # original function
        'distance_mad_c1': mad_c1,  # partial function wrapping the original function
    },
})

mydf_agg
mydf_agg.columns = mydf_agg.columns.droplevel(level=0) # as colunas deixam de ser tuplas

################################################################
########### Agora vai ser assim ################################
########### Resulta em erro ####################################

del mydf_agg

import numpy as np
import statsmodels.robust as smrb
from functools import partial

# median absolute deviation as a partial function
# in order to demonstrate the issue with partial functions as aggregators
mad_c1 = partial(smrb.mad, c=1)

# no way of choosing the destination's column names...
mydf_agg = mydf.groupby('cat').agg({
    'energy': [
    	'sum',
    	lambda x: np.percentile(x, 98), # lambda
    	lambda x: np.percentile(x, 17), # lambda
    ],
    'distance': [
    	'sum',
    	'mean',
    	smrb.mad, # original function
    	mad_c1,   # partial function wrapping the original function
    ],
})

"""
The above breaks because the lambda functions will all result
in columns named <lambda> which results in
SpecificationError: Function names must be unique, found multiple named <lambda>
Backward incompatible regression: one cannot apply two different
lambdas to the same original column anymore.
"""

def my_agg(x):
    data = {'energy_sum': x.energy.sum(),
            'energy_p98': np.percentile(x.energy, 98),
            'energy_p17': np.percentile(x.energy, 17),
            'distance sum' : x.distance.sum(),
            'distance mean': x.distance.mean(),
            'distance MAD': smrb.mad(x.distance),
            'distance MAD C1': mad_c1(x.distance)}
    return pd.Series(data, index=list_of_column_order)
    
mydf.groupby('cat').apply(my_agg)

################################################################
########### Outra solução       ################################
###########                 ####################################

df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': range(3), 'C': [.1, .2, .3]})

gr = df.groupby('A')

gr.agg({'B': {'b_sum': 'sum'}, 'C': {'c_mean': 'mean', 'c_count': 'count'}})

################################################################
########### Outra solução       ################################
###########                 ####################################

df = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'],
                   'height': [9.1, 6.0, 9.5, 34.0],
                   'weight': [7.9, 7.5, 9.9, 198.0]})

df

df.groupby('kind').agg(min_height=('height', 'min'), max_weight=('weight', 'max'))

df = pd.DataFrame({"A": ['a', 'a'], 'B': [1, 2], 'C': [3, 4]})

def aggfunc(x, myarg=None):
    print(myarg)
    return sum(x)

df.groupby("A").agg({'B': {'foo': aggfunc}}, myarg='bar')

########################################################################
########################################################################
########################################################################

# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/


from pathlib import Path
import pandas as pd
import dateutil

caminho = Path(r'C:\Users\pedro\OneDrive\Códigos\Estudos - Python\Pandas\phone_data.csv')

data = pd.DataFrame.from_csv(caminho)
data = data.sort_values(['date'], ascending=[True])

data.dtypes
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)

data['item'].count()
data['duration'].max()
data['duration'][data['item'] == 'call'].sum() # 92321.0
data['month'].value_counts()
data['month'].value_counts(normalize=True)
data['network'].nunique()
data['duration'].std()

data.groupby(['month']).groups.keys()
len(data.groupby(['month']).groups['2014-11'])

# Pega a primeira entrada de cada month
data.groupby('month').first()

# Pega a primeira entrada de cada month
data.groupby('month').nth(0)

data\
.sort_values(['date'], ascending=[True])\
.groupby('month')\
.nth(0)

data\
.groupby('month')\
.nth(1)


# Pega a segunda entrada de cada month
data.groupby('month').nth(1)

data\
.sort_values(['date'], ascending=[True])\
.groupby('month')\
.nth(5)



# Pega a terceira entrada de cada month
data.groupby('month').nth(2)

# Pega a soma dasw durações por month
data.groupby('month')['duration'].sum()






# g.nlargest(3)







