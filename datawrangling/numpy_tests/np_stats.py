import numpy as np

arr = np.random.randn(5, 4)
arr

arr.mean()
np.mean(arr)
arr.sum()

# along one axis
# arr.mean(1) means “compute mean across the columns” where
# arr.sum(0) means “compute sum down the rows.” 
arr.mean(axis=1)
arr.sum(axis=0)

# cumulative sum
arr.cumsum()
# cumulative prod
arr.cumprod(axis=1)