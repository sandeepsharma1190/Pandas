# Data Analysis

# File at "C:\Users\sshar127\Desktop\Learnings\Pandas Datasets"

import pandas as pd
import numpy as np

df = pd.read_excel('weather.xlsx')
'''or'''
df = pd.read_excel('weather.xlsx', 'Sheet1')

# to skip first row
df = pd.read_excel('weather.xlsx', skiprows = 1)

# to skip first 2 rows
df = pd.read_excel('weather.xlsx', skiprows = 2)

# to skip first row (header is located at rows no. 1)
df = pd.read_excel('weather.xlsx', header = 1)

# to generate automatic new column name
df = pd.read_excel('weather.xlsx', header = None)

# to give new column name
df = pd.read_excel('weather.xlsx', header = None, names = ['day1','temp','windspeed','event'])

# to pull few rows from a huge data 
# 3 means we are reading only 3 datas
df = pd.read_excel('weather.xlsx', skiprows = 2, nrows=3)

# to change na values to NaN (give names you want to change)
df = pd.read_excel('weather.xlsx', na_values= 'not avaiable')

df.columns  # to pull column names
df.rows

df.shape
rows, columns = df.shape
print(rows)
print(columns)

df.head         # it will print top 5
df.tail         # it will print bottom 5
df.head(2)         # it will print top 2
df.tail(2)         # it will print bottom 2
df[2:5]         # Slicing
df[:]   '''Or''' print(df)    # for entire data
df.shape    # (to check shape)
df.columns      # print names of all columns

# Summary of columns, how many non-null values are here
df.info (null_counts = True)    # Summary of columns
df.info()
# for a specific column
df.day

# for a specific column (another way)
df['day']

type(df['day'])     # to check the type

df[['day', 'event']]    #to print two columns
df[['day', 'event', 'temp']]    #to print three columns
df['temp'].max()    # to check max temp
df['temp'].min()    # to check min temp
df.mean() # for mean value
df['temp'].mean()   # for mean temprature 
df.median() # for median value
df['temp'].median()   # for median temprature 
df.mode() # for mode value
df['temp'].mode()   # for mode temprature 
df.std() # for standerd daviation value
df['temp'].std()   # for standered daviation temprature 

# to check statistics on dataframe
df.describe()

# conditional data
df[df.temp >= 32]

#to pull a row where temprature is maximum
df[df.temp == df.temp.max()]
'''or'''
df[df.temp == df['temp'].max()]     
#using this syntax is best practise, cauze there can be a space in name

# for a range
df[(df['temp']>= 32) & (df['temp']<= 35)]

#to pull a row where temprature is minimum--------
df[df.temp == df.temp.min()]

# to pull only two or three rows
df[['day','temp']][df.temp == df.temp.max()]
df[['day','temp', 'event']][df.temp == df.temp.max()]

# to check index
df.index

# to make index of an actual column, it wont make changes in current dataframe
# it will create a new dataframe (virtual)----------
df.set_index('day')

#to make changes in current dataframe
df.set_index('day', inplace = True)
'''or'''
df.set_index('event', inplace = True)

# to reset index to original state
df.reset_index(inplace = True)

# to fix a column value
df.loc['city']

# to create a new file, it will worked data in new file
df.to_csv('new.csv')

# to remove automatic index from newly created file
df.to_csv('new.csv', index = False)

# to export only wanted columns
df.to_csv('new.csv', columns = ['day', 'temp'])
df.to_csv('new.csv', columns = ['day', 'temp'], index = False)

# How to rename columns
df1 = df.rename(columns = {'day':'days'})
df1 = df.rename(columns = {'days':'day', 'temp':'temps'})

# to skip importing headers
df.to_csv('new.csv', header = False)

# to make changes in categorical data
import pandas as pd

def convert_data(cell):
    if cell == 'n.a':
        return 'sunny'
    return cell

df1 = pd.read_excel('whether.xlsx', 'Sheet1', converters = {
        'event': convert_data})    

# ===== to deal with missing data ====================
import pandas as pd

# parse_dates = ['day'] is needed when date is not in day format
df = pd.read_excel('weather.xlsx', parse_dates = ['day'])
type(df.day[0])

# to set an index (inplace = True is mendetory, else, it wont work)
df.set_index('day', inplace = True)

# fill na values
new_df = df.fillna(0)
print (new_df)

# filling null values with mean (temp column)
df.temp = df.temp.fillna(df.temp.mean())
print (df)

# filling null values with median (temp column)
df.temp = df.temp.fillna(df.temp.median())
print (df)

# filling null values with mode (temp column)
df.temp = df.temp.fillna(df.temp.mode())
print (df)

# fill na values in all fields seprately
new_df = df.fillna({'temp': 0,
                    'windspeed' : 0,
                    'event': 'No event'})
print (new_df)

# carry forward last available value (ffill = forward fill)
# we can use bfill (backword fill) as well
new_df = df.fillna(method = 'ffill')
print (new_df)

# axis = 'columns' means, values will be taken from columns instead of rows
new_df = df.fillna(method = 'ffill', axis = 'columns')
print (new_df)
# or
new_df = df.fillna(method = 'ffill', axis = 1)
print (new_df)

# what id we need to carry forward one fig only once, limit can be increased
new_df = df.fillna(method = 'ffill', limit = 1)
print (new_df)

# Interpolation (middle of two numbers)
new_df = df.interpolate()
print (new_df)

# to delete all na value rows (contains atleas one na)
new_df = df.dropna()
print (new_df)

# delete rows where all values are na
new_df = df.dropna (how= 'all')
print (new_df)

# to save rows where atleast one value is available
# thres = 3 mean, atleast 3 values are available
new_df = df.dropna (thresh=1)
print (new_df)

# to add a missing date
dt = pd.date_range('1/1/2017', '1/11/2017')
dt1 = pd.DatetimeIndex(dt)
df = df.reindex(dt1)
print (df)

# to drop an unwanted column (add an unwanted column in data)
df = df.drop(columns=['#column name here'])

#correlation matrix (How a variable is correlated with other variable)
# correlation dont work on string
df1 = df[['day','temp']].corr()
df1 = df[['day','temp', 'windspeed']].corr()

# changing the datatype
df1.temp = df1.temp.astype(float)
# see the change
df1.info(null_counts = True)

# ====== Manipulatin datasets ========
# indexing by position
# iloc - integer location, loc - location

# how to view a single column
df.iloc[:,3]
df.iloc[:,:] # to view all rows and columns

# how to view a single column (first 5 records)
df.iloc[:5,3]
df.iloc[:5,3].values

# how to view columns in a range
# row starts from 2 till end, column from 3 till end
df.iloc[2:, 3:]

# all the rows from 1 column
df.iloc[:,1]

# to see records using column name
df.loc[:, 'temp']

# to see records from 0 index to 5 index using column name
df.loc[:5, 'temp']

# to see records from 0 index to 5 index using column name
# from column name 'temp' to 'windspeed'
df.loc[:5, 'temp':'windspeed']

# assigning entire value to column
df['temp'] = 1

# to double the values
f = lambda x:x*2
df['temp']=df['temp'].apply(f)

# how to sort a column in ascending order
df.sort_values(by='windspeed')

# how to sort a column in decending order
df.sort_values(by='windspeed', ascending = False)

#filter the data
df['temp']>30

#filter the data, to view only 30 degree plus days
filter1 = df['temp']>30
df3 = df[filter1]
print (df3)

# with two or more filter, to view only 30 degree plus days
filter2 = (df['temp']>30) & (df['windspeed']>4)
df4 = df[filter2]
print (df4)

# Handle missing data: replace function
# when we have special data '-9999'
import pandas as pd
import numpy as np

df = pd.read_excel('whether.xlsx')
new_df = df.replace(-99999, np.NaN)
print (new_df)
# new_df = df.replace([-99999, -88888], np.NaN)
# we can give a list instead of nbr, if we have multiple values to be replaced with nan
# we can replace 0 as well, but 0 is also associated with fig in temp and windspeed

# so to resolve this issue, we use replace column by column with dictionary
new_df = df.replace({'temp': -99999,
                    'windspeed': -99999,
                    'event': 0}, np.NaN)
print (new_df)
# or, if you want to replace 0 to 'sunny' in event column
new_df = df.replace({-99999 : np.NaN,
                     'No Event' : 'sunny'})
print (new_df)

# ===== Regular expression
new_df = df.replace('[A-Za-z]', '', regex = True)
# it removed all alphbets, even from events columns, hence to avoid that

new_df = df.replace({'temp': '[A-Za-z]',
                     'windspeed': '[A-Za-z]'}, '', regex = True)
print (new_df)

# Replace using list (most commonly used)
df = pd.DataFrame({'grade' : ['A', 'D', 'B', 'C', 'A'],
                   'name': ['Sandeep', 'Nahar', 'Jesse', 'Rahul', 'Rashmi']})
print (df)
new_df = df.replace(['A', 'B', 'C', 'D'], [1,2,3,4])
print (new_df)

# === Group By (Split, apply, combine)
# add new column of cities in data
import pandas as pd
import numpy as np

df = pd.read_excel('whether.xlsx')
print (df)

city_grouping = df.groupby('city')
print (city_grouping)

# iterator (to see all cities grouping)
for city, city_df in city_grouping:
    print (city)
    print (city_df)

# to pull a specific city group
city_grouping.get_group('Delhi')   

# to check max temp for all cities
city_grouping.max()

# to check min temp for all cities
city_grouping.min()
city_grouping.mean() # fo average values
city_grouping.describe()

# =================concatenation
import pandas as pd
import numpy as np
india_weather = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'temp': [32, 28, 26],
                 'humidity': [50, 80, 70]})

us_weather = pd.DataFrame({'city': ['new-york', 'chicago', 'seattle'],
                 'temp': [22, 25, 18],
                 'humidity': [68, 72, 56]})

df = pd.concat([india_weather, us_weather])

# to ignore index
df = pd.concat([india_weather, us_weather], ignore_index = True)

# tu pull data key wise
df = pd.concat([india_weather, us_weather], keys = ['india', 'us'])
df.loc['india']

# ===== Same city data concatenation
temp1 = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'temp': [32, 28, 26]})
windspeed = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'windspeed': [2, 8, 6]})

pd.concat([temp1, windspeed]) # by default axis = 0
pd.concat([temp1, windspeed], axis = 0)
pd.concat([temp1, windspeed], axis = 1)

# if data is mis matched, to avoid contradiction, we assign index
temp1 = pd.DataFrame({'city': ['mumbai', 'delhi'],
                 'temp': [32, 28]}, index=[1,0])
windspeed = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'windspeed': [2, 8, 6]}, index=[0,1,2])
pd.concat([temp1, windspeed], axis = 1)
##======== or, we can assign names in index as well
temp1 = pd.DataFrame({'city': ['mumbai', 'delhi'],
                 'temp': [32, 28]}, index=['mumbai', 'delhi'])
windspeed = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'windspeed': [2, 8, 6]}, index=['delhi', 'mumbai', 'goa'])
pd.concat([temp1, windspeed], axis = 1)

# appending a series into a dataframe
temp1 = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'temp': [32, 28, 26]})
series = pd.Series(['Hot', 'Rainy', 'Mix'], name = 'event')
df = pd.concat([temp1, series], axis = 1)

# ========================= Merge ==============================
import pandas as pd
import numpy as np
temp1 = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'temp': [32, 28, 26]})
windspeed = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'windspeed': [2, 8, 6]})

df2 = pd.merge(temp1, windspeed, on='city') # 'how = inner' is default value
df2 = pd.merge(temp1, windspeed, on='city', how = 'outer')
print (df2)

# indicator can show date is from left table or right
df2 = pd.merge(temp1, windspeed, on='city', how = 'outer', indicator = True)
#--------
temp2 = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'windspeed': [2, 8, 6]})
windspeed1 = pd.DataFrame({'city': ['delhi', 'mumbai', 'goa'],
                 'windspeed': [2, 8, 6]})
df3 = pd.merge(temp2, windspeed1, on='city')
print (df3)
# in order to resolve X n Y, we use suffix
df3 = pd.merge(temp2, windspeed1, on='city', suffixes = ('_left', '_right'))
print (df3)

#=============== Pivot
import pandas as pd
import numpy as np

df = pd.read_csv('weather.csv')
df.pivot(index = 'day', columns = 'city') # we will see all fields

# if we want any specific value or field
# try to took same dates, but in csv
df.pivot(index = 'day', columns = 'city', values='humidity')

#=============== Pivot Table
df = pd.read_csv('weather1.csv')

#aggfunc (numpy function) and give us operators to perform
df.pivot_table(index = 'day', columns = 'city')
df.pivot_table(index = 'day', columns = 'city', aggfunc = 'sum')
df.pivot_table(index = 'day', columns = 'city', aggfunc = 'count')
df.pivot_table(index = 'day', columns = 'city', aggfunc = 'mean')
df.pivot_table(index = 'day', columns = 'city', aggfunc = 'diff')

# Margins
df.pivot_table(index = 'day', columns = 'city', margins = True)

# grouper function
import pandas as pd
import numpy as np

df1 = pd.read_csv('weather2.csv')
print (df1)

# first we need to change day to date time object
df1['day'] = pd.to_datetime(df1['day'])

# 'M' means monthly
df1.pivot_table(index = pd.Grouper(freq = 'M', key = 'day'), columns = 'city')

#======== Transform or reshape data using melt=============
import pandas as pd
import numpy as np

df2 = pd.read_csv('weather3.csv')
print (df2)

# melt can transform data in one single column
df2_1 = pd.melt(df2, id_vars = ['day'])
print (df2_1)

# to see one city's data
df2_1[df2_1['variable']=='delhi']

# to change name from 'variable' to city in output table
df2_1 = pd.melt(df2, id_vars = ['day'], var_name = 'city', value_name = 'temp')
print (df2_1)
df2_1[df2_1['temp']=='delhi']

#======== Stacking unstacking=============
import pandas as pd
import numpy as np
# header = [0,1] means we have 2 headers
df3 = pd.read_excel('stockmarket.xlsx', header = [0,1])
print (df3)
'''
x = df3.stack() # inner most level, which is company
print (x)
x.to_excel('test.xlsx')     # to save file as excel and see changes
'''
# level will change levels for columns
# level will transpors data as per levels
df3.stack(level = 0) # 0 means 0 level which is company

# stacked to unstacked
stacked_data = df3.stack()
stacked_data.unstack()

####### ======= for more level data in stacking
# 3 level of header = [0,1,2]
df4 = pd.read_excel('stockmarket1.xlsx', header = [0,1,2])
df4.stack() # inner most level, which is company
df4.stack(level = 0)
df4.stack(level = 1)
df4.stack(level = 2)

#====================== Crosstab===================
# Cross tabulation or contingency table
# it shows th frequency distribution of a variable
'''A frequency distribution is an overview of all distinct values in some 
variable and the number of times they occur'''
import pandas as pd
import numpy as np
df4 = pd.read_excel('survey.xls')
print (df4)

# df4.Nationality - X- axis (index/ rows)
# df4.Sex - Y axis - columns
pd.crosstab(df4.Nationality, df4.Sex)

# margins means total
pd.crosstab(df4.Nationality, df4.Sex, margins = True)

# for multiple variable in columns
pd.crosstab(df4.Nationality, [df4.Sex, df4.Handedness], margins = True)
# or in rows
pd.crosstab([df4.Handedness, df4.Nationality], df4.Sex, margins = True)

# for %age
pd.crosstab(df4.Nationality, df4.Sex, normalize = 'index')

# for average age
pd.crosstab(df4.Nationality, df4.Sex, values = df4.Age, aggfunc = np.average)

#============== Time Series analysis ===========================
# =======DatetimeIndex and Resample======
# download apple stock from yahoo finance
# https://finance.yahoo.com/quote/AAPL/history?p=AAPL
import pandas as pd
import numpy as np
df4 = pd.read_csv('AAPL.csv')
print (df4)
print (df4.head(5))

# to check type of date
type(df4.Date[0])

# to change date type in data from string to date
df4 = pd.read_csv('AAPL.csv', parse_dates=['Date'])
type(df4.Date[0])

# to make date column index
df4 = pd.read_csv('AAPL.csv', parse_dates=['Date'], index_col = 'Date')

# to pull data for january 2020
df4['2020-01']
df4['2020-01'].Close # for closing price
# df4['2020-01-10']

#to pull date within a range
df4['2020-01-10':'2020-01-13']

# average stock price for month Jan
df4['2020-01'].Close.mean()

# for monthly frequency
df4.Close.resample('M').mean()




















