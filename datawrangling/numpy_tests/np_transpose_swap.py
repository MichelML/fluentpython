import numpy as np

arr = np.arange(15).reshape((3, 5)) # reshape
arr
arr.T # transpose

np.dot(arr.T, arr)
np.dot(arr, arr.T)

arr = np.arange(16).reshape((2,2,4))
arr
arr.transpose((1, 0, 2))
arr.swapaxes(1,2)

