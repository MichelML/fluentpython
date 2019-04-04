import numpy as np 

arr = np.random.rand(100)
(arr > 0).sum() # number of positive values

bools = np.array([False, False, True, False])
bools.any()
bools.all()