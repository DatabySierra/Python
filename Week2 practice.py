# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 20:02:16 2023

@author: 14236
"""
#%%
import numpy as np
import pandas as pd
#%%
series1 = pd. Series([1, 3, 5, 7])
print(series1)
## 0    1
## 1    3
## 2    5
## 3    7
## dtype: int64
#%%
series2 = pd. Series({'b': 1, 'a': 0, 'c': 2})
# The index is the keys of the dictionary.
print(series2)
## b    1
## a    0
## c    2
## dtype: int64
#%%
np.random.seed(500) 
#With the seed reset, the same set of numbers will appear every time
series3 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# np.random.randn(5) generates 5 random numbers
print(series3)
## a   -0.377364
## b    0.166759
## c    0.682802
## d    1.921379
## e   -0.197037
## dtype: float64
series4 = pd.Series(np.random.randn(5))
# the default integer index
print(series4)
## 0   -0.759879
## 1   -2.089066
## 2   -0.036373
## 3   -1.217749
## 4   -1.428905
## dtype: float64
print(len(series4))# get the length of the series4
## 5
#%%
#data = {'Country': ['Belgium', 'Brazil', 'China'], 'Capital': ['Brussels', 'Brasília', 'Beijing'], 'Population': [11190846, 207847528, 1409517397]}
data = {'Country': ['Belgium', 'China'], 'Capital': ['Brussels', 'Beijing'], 'Population': [11190846, 1409517397]}
pop = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
# the default integer index.
print(pop)
##    Country   Capital  Population
## 0  Belgium  Brussels    11190846
## 1    China   Beijing  1409517397
#%%
dates = pd.date_range('20200101', periods=6)
# use pd.date_range to generate 6 days as Datetime index
print(dates)
## DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
##                '2020-01-05', '2020-01-06'],
##               dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
#Creating a DataFrame by passing a NumPy array  with a datetime index and labeled columns:
print(df)
##                    A         B         C         D
## 2020-01-01 -0.170528  1.160940 -1.061140 -1.408500
## 2020-01-02  0.839550 -0.099625 -1.736265 -0.307186
## 2020-01-03 -0.080870  0.834319  1.885460  0.440898
## 2020-01-04  0.439874  1.070767  0.404252  0.133472
## 2020-01-05  1.937107  1.002275 -0.047000  1.153260
## 2020-01-06  0.019985 -1.579930 -0.197842 -0.220196
#%%
data = {'Country': ['Belgium', 'China'], 'Capital': ['Brussels', 'Beijing'], 'Population': [11190846, 1409517397]}
df1 = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
df1.to_csv('population.csv') 
# wrtie the data frame df1 to population.csv
df1.to_excel('population.xlsx')
# wrtie the data frame df1 to population.xlsx
#%%
pop_csv = pd.read_csv('population.csv')
# read data from the file population.csv
print(pop_csv)
##    Unnamed: 0  Country   Capital  Population
## 0           0  Belgium  Brussels    11190846
## 1           1    China   Beijing  1409517397
pop_xlsx = pd.read_excel('population.xlsx')
# read data from the file named population.xlsx
print(pop_xlsx)
##    Country   Capital  Population
## 0  Belgium  Brussels    11190846
## 1    China   Beijing  1409517397
#%%
np.random.seed(500)
dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df.head())
# default first five rows 
##                    A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
print(df.tail(3))
# the last three rows
##                    A         B         C         D
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
print(df.head(4))
# the first 4 rows
##                    A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
#%%
data = {'Country': ['Belgium', 'China'], 'Capital': ['Brussels', 'Beijing'], 'Population': [11190846, 1409517397]}
pop = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'],index=['country_1','country_2'])
print (len(pop))# find the number of rows
## 2
#%%
print(pop.shape) # 2 rows(index) and 3 columns.
## (2, 3)
#%%
pop_Transpose = pop.T
print(pop_Transpose) 
# The transpose of the DataFrame.
##            country_1   country_2
## Country      Belgium       China
## Capital     Brussels     Beijing
## Population  11190846  1409517397
#%%print(pop.index) # The index (row labels) of the DataFrame.
## Index(['country_1', 'country_2'], dtype='object')
print(pop.columns) # The column labels of the DataFrame.
## Index(['Country', 'Capital', 'Population'], dtype='object')
#%%
np.random.seed(500)
dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
##                    A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
#%%
df.A 
# select the entire column A
df['A'] 
# another way to select the column entire A. 
print(df.A)
## 2020-01-01   -0.377364
## 2020-01-02   -0.197037
## 2020-01-03   -1.217749
## 2020-01-04   -1.061140
## 2020-01-05   -1.736265
## 2020-01-06    1.885460
## Freq: D, Name: A, dtype: float64
df[['A', 'C']] 
# select the entire columns A and C. 
# use list form if more than one column ['A', 'C']
print(df[['A', 'C']])
##                    A         C
## 2020-01-01 -0.377364  0.682802
## 2020-01-02 -0.197037 -2.089066
## 2020-01-03 -1.217749 -0.170528
## 2020-01-04 -1.061140  0.839550
## 2020-01-05 -1.736265 -0.080870
## 2020-01-06  1.885460  0.439874
df[0:3]
# select the entire first to third rows by row postions.
# third row not include
df[:3] # from the beginning to the third row not include 3.
# the same as df[0:3]
print(df[0:3])
##                    A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
df['20200101': '20200103']
# select the entire first to third rows by row labels.
# '20200101': '20200103' means from row '20200101'to row '20200103'
print(df['20200101': '20200103'])
##                    A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
#%%
df.loc[:, ['A', 'C']] 
# another way to select the entire columns A and C, 
# : means all rows
print(df.loc[:, ['A', 'C']])
##                    A         C
## 2020-01-01 -0.377364  0.682802
## 2020-01-02 -0.197037 -2.089066
## 2020-01-03 -1.217749 -0.170528
## 2020-01-04 -1.061140  0.839550
## 2020-01-05 -1.736265 -0.080870
## 2020-01-06  1.885460  0.439874
df.loc['20200101', :]
# another way to select the entire row, 
# : means all columns
print(df.loc['20200101',:])
## A   -0.377364
## B    0.166759
## C    0.682802
## D    1.921379
## Name: 2020-01-01 00:00:00, dtype: float64
df.loc['20200101', ['A', 'C']]
# select a part of one row 
print(df.loc['20200101', ['A', 'C']])
## A   -0.377364
## C    0.682802
## Name: 2020-01-01 00:00:00, dtype: float64
df.loc['20200101': '20200103', ['A', 'C']]
# select a part of more rows and columns
print(df.loc['20200101': '20200103', ['A', 'C']])
##                    A         C
## 2020-01-01 -0.377364  0.682802
## 2020-01-02 -0.197037 -2.089066
## 2020-01-03 -1.217749 -0.170528
#%%
df.iloc[3] 
# select the fourth row. position is 3. 
print(df.iloc[3])
## A   -1.061140
## B   -1.408500
## C    0.839550
## D   -0.099625
## Name: 2020-01-04 00:00:00, dtype: float64
df.iloc[ :,3]
# select the fourth column. position is 3. 
print(df.iloc[ :,3])
## 2020-01-01    1.921379
## 2020-01-02   -0.036373
## 2020-01-03    1.160940
## 2020-01-04   -0.099625
## 2020-01-05    0.834319
## 2020-01-06    1.070767
## Freq: D, Name: D, dtype: float64
df.iloc[3:5, :] 
# select the rows from position 3 to 5 not include 5. 
print(df.iloc[3:5, :])
##                    A         B        C         D
## 2020-01-04 -1.061140 -1.408500  0.83955 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.08087  0.834319
df.iloc[ :,1:3]
# select the columns from positions 1 to 3 not include 3. 
print(df.iloc[ :,1:3])
##                    B         C
## 2020-01-01  0.166759  0.682802
## 2020-01-02 -0.759879 -2.089066
## 2020-01-03 -1.428905 -0.170528
## 2020-01-04 -1.408500  0.839550
## 2020-01-05 -0.307186 -0.080870
## 2020-01-06  0.440898  0.439874
df.iloc[3:5,1:3]
print(df.iloc[ 3:5,1:3])
##                    B        C
## 2020-01-04 -1.408500  0.83955
## 2020-01-05 -0.307186 -0.08087
df.iloc[5,3]
# select a value at poistion row 5 column 3. 
# the sixth row and fourth column.
print(df.iloc[ 5, 3])
## 1.070766736658775
#%%
df1 = df[df.A > 0] 
# select the  rows with column A > 0
# name the selected part as a data frame df1
print(df1)
##                   A         B         C         D
## 2020-01-06  1.88546  0.440898  0.439874  1.070767
df2 = df[df == 0] 
# select the values = 0 in the entire data frame.
print(df2)
##              A   B   C   D
## 2020-01-01 NaN NaN NaN NaN
## 2020-01-02 NaN NaN NaN NaN
## 2020-01-03 NaN NaN NaN NaN
## 2020-01-04 NaN NaN NaN NaN
## 2020-01-05 NaN NaN NaN NaN
## 2020-01-06 NaN NaN NaN NaN 
df3 = df[df.B != 0] 
# select the rows not equal to 0 in the column B
print(df3) 
##                   A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
## 2020-01-06  1.885460  0.440898  0.439874  1.070767 
df4 = df[df < 0] 
# select the values < 0 in the entire data frame.
# NaN means missing values
print(df4) ##       A         B         C         D
## 2020-01-01 -0.377364       NaN       NaN       NaN
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528       NaN
## 2020-01-04 -1.061140 -1.408500       NaN -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870       NaN
## 2020-01-06       NaN       NaN       NaN       NaN 
df5 = df[(df.A < 0) & (df.C > 0)]
# select the rows  with column A <0 and Column C >0
# two conditions. use ()for each condition
# '&' means 'and'
print(df5) ##        A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
df6 = df[(df.A >0) | (df.C >0)]
# select the rows  with column A <0 and Column C >0
# '|' means 'or'
print(df6)##        A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
#%%
df5 = df4.dropna() # drop any rows that have missing data
print(df5)
##                    A         B         C         D
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
df6 = df4.fillna(value=0)
# fill missing values  by 0
print(df6)
##                    A         B         C         D
## 2020-01-01 -0.377364  0.000000  0.000000  0.000000
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  0.000000
## 2020-01-04 -1.061140 -1.408500  0.000000 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.000000
## 2020-01-06  0.000000  0.000000  0.000000  0.000000
#%%
my_df = df.copy() 
print(my_df)
##                    A         B         C         D
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
difference = my_df-df 
print(difference)
##               A    B    C    D
## 2020-01-01  0.0  0.0  0.0  0.0
## 2020-01-02  0.0  0.0  0.0  0.0
## 2020-01-03  0.0  0.0  0.0  0.0
## 2020-01-04  0.0  0.0  0.0  0.0
## 2020-01-05  0.0  0.0  0.0  0.0
## 2020-01-06  0.0  0.0  0.0  0.0
#%%
df7 = df.sort_values('A') 
# the default ascending=True
print(df7)
##                    A         B         C         D
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
df8 = df.sort_values('A', ascending=False) 
print(df8)
##                    A         B         C         D
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
df9 = df.sort_values(['A', 'C']) 
# sort data by two columns
print(df9)
##                    A         B         C         D
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373
## 2020-01-06  1.885460  0.440898  0.439874  1.070767
#%%
df['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
# Adding a new Column to df
print(df)
##                    A         B         C         D      E
## 2020-01-01 -0.377364  0.166759  0.682802  1.921379    one
## 2020-01-02 -0.197037 -0.759879 -2.089066 -0.036373    one
## 2020-01-03 -1.217749 -1.428905 -0.170528  1.160940    two
## 2020-01-04 -1.061140 -1.408500  0.839550 -0.099625  three
## 2020-01-05 -1.736265 -0.307186 -0.080870  0.834319   four
## 2020-01-06  1.885460  0.440898  0.439874  1.070767  three
df10 = df.drop('B', axis=1)
# drop column B
# axis=1 means to drop by column
# axis
print(df10)
##                    A         C         D      E
## 2020-01-01 -0.377364  0.682802  1.921379    one
## 2020-01-02 -0.197037 -2.089066 -0.036373    one
## 2020-01-03 -1.217749 -0.170528  1.160940    two
## 2020-01-04 -1.061140  0.839550 -0.099625  three
## 2020-01-05 -1.736265 -0.080870  0.834319   four
## 2020-01-06  1.885460  0.439874  1.070767  three
#%%
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],\
                       'B': ['B0', 'B1', 'B2', 'B3'],\
                        'C': ['C0', 'C1', 'C2', 'C3']},\
                       index=[0, 1, 2, 3])
    
print('df1','\n', df1) 
## df1 
##      A   B   C
## 0  A0  B0  C0
## 1  A1  B1  C1
## 2  A2  B2  C2
## 3  A3  B3  C3
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],\
                        'B': ['B4', 'B5', 'B6', 'B7'],\
                        'C': ['C4', 'C5', 'C6', 'C7']},\
                       index=[4,5,6,7])
print('df2', '\n', df2) 
## df2 
##      A   B   C
## 4  A4  B4  C4
## 5  A5  B5  C5
## 6  A6  B6  C6
## 7  A7  B7  C7
df3 = pd.DataFrame({'D': ['D0', 'D1', 'D2', 'D3'],\
                        'E': ['E0', 'E1', 'E2', 'E3'],\
                        'F': ['F0', 'F1', 'F2', 'F3']},\
                       index=[0,1,2,3])
print('df3', '\n', df3) 
## df3 
##      D   E   F
## 0  D0  E0  F0
## 1  D1  E1  F1
## 2  D2  E2  F2
## 3  D3  E3  F3
merge1 = pd.concat([df1, df2])
#union df1 and df2 along rows with ignore_index=False
print(merge1)
##     A   B   C
## 0  A0  B0  C0
## 1  A1  B1  C1
## 2  A2  B2  C2
## 3  A3  B3  C3
## 4  A4  B4  C4
## 5  A5  B5  C5
## 6  A6  B6  C6
## 7  A7  B7  C7<
merge2 = pd.concat([df1, df3], axis=1)
#union df1 and df3 along columns with ignore_index=False
print(merge2)
##     A   B   C   D   E   F
## 0  A0  B0  C0  D0  E0  F0
## 1  A1  B1  C1  D1  E1  F1
## 2  A2  B2  C2  D2  E2  F2
## 3  A3  B3  C3  D3  E3  F3
merge3 = pd.concat([df1, df2], axis=1)
#union df1 and df2 along columns with ignore_index=False
print(merge3)
##      A    B    C    A    B    C
## 0   A0   B0   C0  NaN  NaN  NaN
## 1   A1   B1   C1  NaN  NaN  NaN
## 2   A2   B2   C2  NaN  NaN  NaN
## 3   A3   B3   C3  NaN  NaN  NaN
## 4  NaN  NaN  NaN   A4   B4   C4
## 5  NaN  NaN  NaN   A5   B5   C5
## 6  NaN  NaN  NaN   A6   B6   C6
## 7  NaN  NaN  NaN   A7   B7   C7
#%%
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',\
                             'foo', 'bar', 'foo', 'foo'],\
                      'B': ['one', 'one', 'two', 'three',\
                          'two', 'two', 'one', 'three'],\
                       'C': np.random.randn(8),\
                       'D': np.random.randn(8)})
print(df)
##      A      B         C         D
## 0  foo    one  0.404252 -0.197842
## 1  bar    one  0.133472 -0.220196
## 2  foo    two  1.937107 -0.267084
## 3  bar  three  1.002275 -0.412130
## 4  foo    two -0.047000  1.049545
## 5  bar    two  1.153260  1.663777
## 6  foo    one  0.019985  0.603633
## 7  foo  three -1.579930  0.231452
grouping_result1 = df.groupby('A').sum()
#Grouping and then applying the sum() function to the resulting groups
print(grouping_result1)
##             C         D
## A                      
## bar  2.289007  1.031451
## foo  0.734415  1.419703
grouping_result2 = df.groupby(['A', 'B']).mean()
#Grouping by multiple columns forms a hierarchical index, and again we can apply the mean function.            
grouping_result2.to_csv('grouping result.csv')
# save the grouping result grouping_result2 to a csv file
print(grouping_result2)
##                   C         D
## A   B                        
## bar one    0.133472 -0.220196
##     three  1.002275 -0.412130
##     two    1.153260  1.663777
## foo one    0.212119  0.202895
##     three -1.579930  0.231452
##     two    0.945054  0.391230
