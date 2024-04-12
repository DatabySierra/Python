# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:04:56 2023

@author: 14236
"""
#%%
#1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Top_100 = pd.read_csv('Top 100 Retailers 2015.csv')
Top_100 = Top_100.dropna()
Top_100.shape
Top_100.index = Top_100.Company
print(Top_100.head())
#%%
#2
Top_20 =Top_100[Top_100['Rank'].between(11,20)]
Top_20=Top_20.sort_values('Rank')
Top_20.to_excel('Top_20.xlsx')
print(Top_20)
#%%
#3
#a
Top_20.plot.bar(y='Worldwide_Retail_Sales_million', x='Company')
plt.show()
#%%
#b
Top_20.plot.barh(y=['Worldwide_Retail_Sales_million','USA_Retail_Sales_million'], x='Company', rot=45, stacked=True)
plt.savefig('bar_chart.png')
plt.show()
#%%
#c
plt.figure()
Top_20.Worldwide_Retail_Sales_million.plot.pie(subplots=True,figsize=(16, 8), autopct='%1.1f%%', legend=False)
plt.show()
plt.savefig('pie_chart.png')
#%%
#4
#a
Top_100.plot(y=['USA_Retail_Sales_million','Worldwide_Retail_Sales_million'])
plt.show()
#%%
#b
Top_100.hist(bins=10, figsize=(6,8))
plt.show()
plt.savefig('histogram.png')
#%%
#c
Top_100.hist(column=['USA_percentage_Worldwide_Sales'], bins=20)
plt.show()
#%%
#d
Top_100.plot.scatter(y='USA_percentage_Worldwide_Sales',x='USA_Retail_Sales_million', alpha=0.4, c='Rank', cmap=plt.get_cmap("jet"), colorbar=True)
plt.show()
plt.savefig('scatter.png')
#%%
#e
ax1=Top_100.plot.scatter(y='USA_Retail_Sales_million', x='Rank')
Top_100.plot.scatter(y='Worldwide_Retail_Sales_million', x='Rank', ax=ax1)
plt.show()
plt.savefig('scatter2.png')
#%%
#f
pd.plotting.scatter_matrix(Top_100, alpha=0.4, figsize=(15,15))
plt.show()
plt.savefig('scatter matrix.png')
#%%
#g
Top_100.boxplot(column='USA_percentage_Worldwide_Sales', grid=False)
plt.show()
plt.savefig('boxplot.png')
