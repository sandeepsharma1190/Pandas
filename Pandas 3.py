# Pandas Python bootcamp 2
# Series is 1-d
# dataframe is 2-d
# panal date for 3-d and so on
import numpy as np
import pandas as pd
x = ['a','b','c','d']
y = [1,2,3,4]

# to convert into panda series
a = pd.Series(y)

# to change index name
aa = pd.Series(y, index = x)
print (aa)

aa = pd.Series(y, x)
print (aa)
# giving 'index' name is not needed, but you need to mention the same in actual order
# Definition : Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

# using dictionary, we dont need to mention index name
x = ['a','b','c','d']
y = [1,2,3,4]
z = dict(zip(x,y)) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
a1 = pd.Series(z)
print (a1)

# addition
aa+a1   # it will add values, a with a, b with b etc.

# to find index
aa['c']
aa[3]
aa['c':]    # every value after c
aa['c':'d']     #slicing
aa[:'d'] # every value before d

# ====Creating dataframe fram from 5 different list
A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]
# Rows -> ['a','b','c','d','e'], Columns: ->['w','x','y','z']
df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'], ['w','x','y','z'])
print (df)

# how to create a new row
df['aa'] = df['y'] + df['z']
print (df)

df['ab'] = [4,5,6,1,2]
print (df)

# How to delete a row
df.drop('e')
print (df)  # e is not deleted here

# to permanently delete a row
df.drop('e', inplace = True)

# How to delete a column
df.drop('aa', axis = 1)

# to delete a column permanently
df.drop('aa', axis = 1, inplace = True)

df.loc['d','y']

#====== Conditional acessing
df[df>3] # to see grater value than 3
df [df['w']>3] # to see grater value than 3 column wise

# to get only one row
df [df['w']>3][['w']]

# to get more than one row
df [df['w']>3][['w', 'x']]

# & and or (|)

# & both conditions should meet
df [(df['w']>3) & (df['z']>4)]

# or
df [(df['w']>3) | (df['z']>4)]

# Missing data
dict2 = {'a' :[1,2,3,4,5], 'b':[6,7,8,9,np.nan], 'c':[0,1,2,np.nan, np.nan],
         'd': [3,4,np.nan,np.nan,np.nan], 'e':[5,np.nan,np.nan,np.nan,np.nan]}

df1 = pd.DataFrame(dict2)
print (df1)

df1.dropna(axis = 0)
df1.fillna(1)

# to fill na values with mean value of that particular column
df1['b'].fillna(value = df1['b'].mean())

# ============= Analyzing data by group by
shop_keeper = {'items': ['milk', 'milk', 'eggs', 'eggs', 'tofu' ,'tofu'],
               'days' : ['mon', 'tue', 'wed', 'thu', 'fri','sat'],
               'sales': [100, 80, 200, 100, 5, 10]}
df2 = pd.DataFrame(shop_keeper)

x = df2.groupby('items')
x.mean() # groupby is items, so mean is related to items only
x.std()
x.count()
x.max() # days can be different
x.min() # days can be different
x.describe()
x.describe().transpose()




































