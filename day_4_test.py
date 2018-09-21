# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:21:02 2018

@author: gydwo
"""

import pandas
import matplotlib.pyplot as plt

series = pandas.Series([10, 15, 21])

dates = pandas.date_range('20180920', '20180930')

df = pandas.DataFrame([[10, 15], [21, 17], [1, 5]])

df = pandas.DataFrame([[10, 15], [21, 17], [1, 5]],
                 columns=['money', 'happiness'],
                 index=['Bob', 'Tom', 'Cheryl'])


print(df.dtypes)

print(df.columns)

print(df.index)

df.describe()

#Print columns
print(df['money'])
df.money

#Print rows
df[0:1]
df[1:2]

#find specific value by word
df.loc['Bob']
df.loc['Bob', 'money']

#find with integer value - row and then column
df.iloc[:0]
df.iloc[1,0]
df.iloc[1,1]

#find data on 'Data Mill North'

pubs = pandas.read_csv('leedsbeerquest.csv')

#calculate mean in dataset
pubs.lat.mean()

#
pubs.describe()

#change dataset index from numbers to the pub names
#search all names
pubs.name
pubs.name.describe()
named_pubs = pubs.set_index('name')
#search specific
named_pubs.loc['Veritas']


#find cheapest
pubs.stars_value
named_pubs.stars_value.describe()
named_pubs.stars_value.value_counts()
named_pubs.stars_value == 5
#find the name of the pub
named_pubs[named_pubs.stars_value == 5].index
#want to find address 
named_pubs[named_pubs.stars_value == 5].address
#graph
named_pubs.stars_value.hist(bins=9)

#put the pubs with same rating in a group
named_pubs.groupby('stars_value')
named_pubs.groupby('stars_value').mean()

#locate
named_pubs.lat
named_pubs.loc[:, ('lat', 'lng')]
plt.plot(named_pubs.lat, named_pubs.lng)
#only want points
plt.plot(named_pubs.lat, named_pubs.lng, '.')
#switch axis
plt.plot(named_pubs.lng, named_pubs.lat, '.')


#create a hexbin plot
plt.hexbin(named_pubs.lng, named_pubs.lat)
#make bin size bigger
plt.hexbin(named_pubs.lng, named_pubs.lat, gridsize=15)
plt.hexbin(named_pubs.lng, named_pubs.lat, gridsize=15);plt.colorbar()

