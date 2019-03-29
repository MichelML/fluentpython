import numpy as np

# generate some random data
data = np.random.rand(2, 4)
print(data)

# perform mathematical operations with data
print(data * 10)
print(data + data)

# shape
print(data.shape)

# dtype
print(data.dtype)

######

# create ndarrays
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)

# multidimensional ndarray
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)

