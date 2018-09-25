import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(3)*len(l))

array = np.array(1000)
print((array.size)*(array.itemsize))
