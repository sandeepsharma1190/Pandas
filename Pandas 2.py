# Pandas in Data Science bootcamp
# Series is 1-d
# dataframe is 2-d
# panal date for 3-d and so on

# series
import pandas as pd

df_1 = [1,2,3,4]
df1 = pd.Series(df_1)
print (df1)

type(df1)

# if we need to change index name
df1 = pd.Series(df_1, index = ['a', 'b', 'c', 'd'])
print (df1)


# ======= How to create a data frame =======

# Creating a dataframe using a list
data = [1,2,3,4,5]
df2 = pd.DataFrame(data)
print (df2)

# Creating a dataframe using a dictionary
dict1 = {'fruits': ['apples', 'mangos', 'bananas'],
         'count': [10,20,15]}
df3 = pd.DataFrame(dict1)
print (df3)

# Creating a dataframe using a series
series1 = pd.Series([6,12], index = ['a','b'])
df = pd.DataFrame(series1)
print (df)

# Creating a dataframe using a numpy array
import numpy as np
num_arr = np.array([[81000, 75000], ['Sandeep', 'Python']])
df4 = pd.DataFrame({'name': num_arr[1], 'salary': num_arr[0]})
print (df4)

#==== Merge, Join and concatenation

# Merge (Inner merge, left, right and outer)
# tables can be joined as per their attributes in Merge
import pandas as pd
player = ['Kohli', 'Rahul', 'Rohit']
score = [45, 88, 72]
title = ['Batsman1', 'Batsman2',  'Batsman3']
df1 = pd.DataFrame({'Player': player, 'Score':score, 'Title':title})
print (df1)

player1 = ['Kohli', 'Jadeja', 'Bumrah']
power = ['Batting', 'All-rounder', 'Bowler']
title1 = ['Batsman1', 'Batsman4',  'Batsman5']
df2 = pd.DataFrame({'Player': player1, 'Power':power, 'Title':title1})
print (df2)

# Inner merge (common value)
pd.merge([df1, df2])
# or
df1.merge(df2)

pd.merge([df1, df2], on = 'Title', how = 'inner')
#or
df1.merge(df2, on = 'Title', how = 'inner')

# Left merge
df1.merge(df2, on = 'Title', how = 'left')

# right merge
df1.merge(df2, on = 'Title', how = 'right')

# right merge
df1.merge(df2, on = 'Title', how = 'outer')

# === Join ====
# tables can be joined as per their index names
player = ['Kohli', 'Rahul', 'Rohit']
score = [45, 88, 72]
title = ['Batsman1', 'Batsman2',  'Batsman3']
df3 = pd.DataFrame({'Player': player, 'Score':score, 'Title':title}, index = ['L1', 'L2', 'L3'])
print (df3)

player = ['Kohli', 'Jadeja', 'Bumrah']
power = ['Batting', 'All-rounder', 'Bowler']
title = ['Batsman1', 'Batsman4',  'Batsman5']
df4 = pd.DataFrame({'Players': player, 'Power':power, 'Titles':title}, index = ['L2', 'L3', 'L4'])
print (df4)

# inner join
df3.join(df4, how = 'inner')

# left join
df3.join(df4, how = 'left')

# Right join
df3.join(df4, how = 'right')

# Outer join
df3.join(df4, how = 'outer')

#===== concatenation ====
# concate wroks only on string = '1' + '1' = '11'
pd.concat([df3, df4])
pd.concat([df3, df4], axis = 1) # nothing will be common
pd.concat([df3, df4], axis = 0) # coulmn name should be same
# pd.concat([df3, df4, df5])

df3['Score'].sum()

# apply if to apply any function
def add(x):
    x = x+2
    return x
df3['Score'].apply(add) # it will add values

df3.sort_values('Score')    # to sort
df3['Score'].unique()   # for unique values
df3['Score'].nunique() # count of unique values
df3['Score'].value_counts() #  to check for how many time value is there
df3['Score'].isnull() # to check if there is any null value




























