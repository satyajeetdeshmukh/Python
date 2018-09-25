import  numpy as np

a = np.array([[1,2], [3,3], [5,6]], dtype=complex)
print(a.ndim)
print(a.itemsize)
print(a)

b = np.array([[1,2,6], [3,3,11], [5,6,88]], dtype=float) #  or np.float6
print('dim of b = ', b.ndim)
print('item size of b = ', b.itemsize)
print('Shape of b = ', b.shape)

# init with zeros

z = np.zeros((3,4))
print(z)

# init with ones

o = np.ones((4,5))
print(o)

# range
print(np.arange(1,5))

print(np.linspace(1,5,10))

print(np.linspace(1,5,5)) #5 no.s linearly spaced in between 1,5

print(b.reshape(9,1)) #shape changed

print(b.ravel()) #flattened

print (b) #unchanged

print(b.sum(axis=0)) #coulmn addition, 1 for row addition

print('standard deviation = ', np.std(b))

# for matrix multiplication a.dot(b)