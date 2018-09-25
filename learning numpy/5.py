import numpy as np

a = np.array([[3,4,5],[6,7,8],[5,7,11]])
print(a[1,1])
print(a[0:2,1]) #0,1 row and 1 col

for cell in a.flat:
    print(cell)
