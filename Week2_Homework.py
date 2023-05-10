# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:55:10 2023

@author: 14236
"""

#%%
#Problem 1
import pandas as pd
data={'Coffee':['Espresso','Americano', 'Latte', 'Macchiato'], 
        'Tea':['Earl Grey', 'Masala', 'Green', 'Ginger'], 
        'Water':['Flat', 'Mineral', 'Alkaline', 'Sparkling']}
df = pd.DataFrame(data, columns = ['Coffee', 'Tea', 'Water'])
df.to_csv('my_table.csv', index=False)
#%%
#Problem 2
#1
auto = pd.read_csv('auto.csv')
print(auto)
#%%
#2
print(auto.shape)
#%%
#3
auto= auto.dropna()
print(auto)
#%%
#4
print(auto.columns)
#%%
#5
auto[:21]
print(auto[:21])
#%%
#6
auto[['car', 'cylinders', 'mpg']]
print(auto.car, auto.cylinders, auto.mpg)
#%%
#7
auto.iloc[2,4]
print(auto.iloc[2,4])
#%%
#8
auto.loc[30:100, ['mpg', 'car']]
print(auto.loc[30:100, ['mpg', 'car']])
#%%
#9
auto.sort_values(['origin', 'cylinders'])
print(auto)
#%%
#10
my_auto=auto.drop(['displacement', 'weight', 'acceleration', 'model'], axis=1)
print(my_auto)
#%%
#11
piece1=my_auto[(my_auto.origin=='US') & (my_auto.mpg > 30)]
print(piece1)
#%%
#12
piece2=my_auto[(my_auto.origin=='Japan') & (my_auto.mpg>30)]
print(piece2)
#%%
#13
auto_new=pd.concat([piece1, piece2])
print(auto_new)
auto_new.to_excel('auto_new.xlsx')
#%%
#14
grouping_result1=auto_new.groupby(['origin', 'cylinders']).mean()
print(grouping_result1)



































