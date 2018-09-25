import numpy as np

a = np.arange(0,30).reshape(2,15)

a1,a2,a3 = np.hsplit(a,3) # similarly vsplit

print (a1)
print (a3)