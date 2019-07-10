import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,5,11)
y = x ** 2

print(x)
print(y)

'''
#Functional
plt.plot(x,y,'r-')
plt.xlabel('XLabel')
plt.ylabel('YLabel')
plt.title('Title of the Graph')
'''

'''
plt.subplot(1,2,1)
plt.plot(x,y,'r-')

plt.subplot(1,2,2)
plt.plot(y,x,'b-')
'''

#OO
'''
fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y,'b-')
axes1.set_xlabel("lxlabel")
axes1.set_ylabel("lylabel")
axes1.set_title("Larger")

axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes2.plot(y,x,'r-')
axes2.set_xlabel("sxlabel")
axes2.set_ylabel("sylabel")
axes2.set_title("Smaller")
'''

fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(2,8))

axes[0].plot(x,y)
axes[0].set_title("x col1")

axes[1].plot(y,x)
axes[1].set_title("y col2")


plt.show()

