import numpy as np

alist=[1,2,3]
l=np.array(alist)
print(type(l))
print(l)

l_squared=l**2
print(l_squared)
print(l_squared.sum())

n=np.dot(l,l)
print(str(n))

cos=n/((np.sqrt(l_squared.sum()))*(np.sqrt(l_squared.sum())))
print(str(cos))