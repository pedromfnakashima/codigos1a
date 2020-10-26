import pandas as pd

df = pd.DataFrame({
        'count': [2,4,6,3,7,5,3,2,4,1],
        'job': ['sales','sales','sales','sales','sales','market','market','market','market','market'],
        'source': ['A','B','C','D','E','A','B','C','D','E']
        })

df_agg = df.groupby(['job','source']).agg({'count':sum})
df_agg

g = df_agg['count'].groupby(level=0, group_keys=False)

res = g.apply(lambda x: x.order(ascending=False).head(3))

g.nlargest(3)








