import numpy as np
'''
a=np.arange(1,10)
print(a)
b=np.arange(10.4)
print(b)
c=np.arange(0.4,10.4,0.8)
print(c)
d=np.arange(0.4,10.4,0.8,int)
print(d)
e=np.linspace(1,10,7)
print(e)


#zero dimensional
x = np.array(42)
print("x : ",x)
print("type of x : ",type(x))
print("dimension : ",np.ndim(x))

y=np.array([7,4,5,8,3,6])
z=np.array([4.5,6.3,8.2,9.6])
print("type of y : ",y.dtype)
print("type of z : ",z.dtype)
print("dimension of y : ",np.ndim(y))
print("dimension of z : ",np.ndim(z))

A = np.array([[[111,112],[121,122]],[[211,212],[221,222]],[[311,312],[321,322]]])
print("dimension of A : ",np.ndim(A))
print("shape of A : ",np.shape(A))#Number of Matrices*Rows*Cols
print(A)
A.shape = (2,2,3)
print(A)


print(np.arange(0,11,2))
print(np.zeros(3))
print(np.zeros((4,3)))

ls = np.linspace(0,5,20)
print(ls)

ls1 = np.eye(3)
print(ls1)

t1 = np.random.rand(5)
print(t1)

t2 = np.random.randint(5,100,10)
print(t2)

print(t2.reshape(2,5))

print(t2.argmax())
print(t2.argmin())
print(t2.shape)
print(t2.dtype)
'''

arr = np.arange(0,11)
print(arr)
part_arr = arr[0:4]
print(part_arr)
part_arr[:] = 99
print(part_arr)
print(arr)



array_2d = np.arange(50).reshape(5,10)
print(array_2d)
''' [Row logic:Column logic]'''
arr_p1 = array_2d[1:3,3:5]
print(arr_p1)

a=[1,2,3,4]
b=[3,2,1,4]
for i in range(0,len(a)):
    print(a[i],b[i])


list1=[10,11,12,7]
k=17

result = [a for a in list1]
print("Result : ",result)
