import pandas as pd
import numpy as np

sal = pd.read_csv("datausage.csv")
print(sal)
print(sal.info())
print("Pulse Avg: ",sal['Pulse'].mean())
print("Max Pulse: ",sal['Pulse'].max())
print(sal[sal['Customer Id'] == "CUS1101315"])
print(sal[sal['Pulse'] == sal['Pulse'].max()]['Customer Id'])
print(sal.loc[sal['Pulse'] == sal['Pulse'].min()])
print(sal.groupby('Customer Id').sum())
print(sal.nunique())
print("Customers : ",sal['Customer Id'].nunique())
print("Customers : ",sal['Customer Id'].unique())

print("Top 5 : \n",sal['Pulse'].value_counts().head(5))
