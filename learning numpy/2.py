import numpy as np
import time
import sys

SIZE =  10000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(0,SIZE, dtype=int)
A2 = np.arange(0,SIZE, dtype=int)

start1=time.time()
result1 = [(x+y) for x,y in zip(L1,L2)]
print("Python list took = ", str((time.time() - start1)*1000) +' ms')

start2=time.time()
result2 = A1+A2
print("Numpy array took = ", str((time.time() - start2)*1000) +' ms')
