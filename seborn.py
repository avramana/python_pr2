import seaborn as sns
import matplotlib.pyplot as plt

#tips = sns.load_dataset('tips')
#flights = sns.load_dataset('flights')
#print(tips.head())
#print(flights.head())

#sns.distplot(tips['total_bill'],kde=False,bins=30)
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')#kde,reg,hex
#sns.pairplot(tips,hue='sex',palette='coolwarm')
#sns.rugplot(tips['total_bill'])
#sns.kdeplot(tips['total_bill'])

import numpy as np
#sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
#sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
#sns.violinplot(x='day',y='total_bill',data=tips)
#sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)
#sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
#sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')


#tc = tips.corr()
#sns.heatmap(tc,annot=True,cmap='coolwarm')

#fp = flights.pivot_table(index='month',columns='year',values='passengers')
#print(fp.head())
#sns.heatmap(fp,cmap='coolwarm',linecolor='white',linewidths=1)
#sns.clustermap(fp,cmap='coolwarm',standard_scale=1)

#grids

iris = sns.load_dataset('iris')
print(iris.head())

g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()