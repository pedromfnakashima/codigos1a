


#################################################################
####### https://www.pythonprogramming.in/pandas-examples.html ###
#################################################################

###
### Ranking
###

import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame Values--------\n")
print(df)
 
print("\n--------- DataFrame Values by Rank--------\n")
print(df.rank())
    
    import pandas as pd
 
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81]},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
 
 
print(df.loc[df.Age == 30,'Height'].tolist())
    
    
    



###
### 
###




