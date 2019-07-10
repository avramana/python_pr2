import numpy as np
import pandas as pd

ser1 = pd.Series(data=[1,2,3],index=['a','b','c'])
print(ser1)

print(ser1['a'])

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],['a','b','c'],['x','y','z'])
print(df)

print(df['x'])

df['new'] = df['y'] + df['z']
print(df)

df.drop('new',axis=1)
print(df)

df.drop('new',axis=1,inplace=True)
print(df)

df.drop('c')
print(df)

print(df.shape)

print(df.loc['a'])
print(df.iloc[0])
print(df.loc['b','z'])

from numpy.random import randn
np.random.seed(101)
df1 = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['x','y','z','w'])

print(df1)

#Conditional Selection
print(df1>0)
booldf1 = df1>0

print(df1[booldf1])

print(df.reset_index())










