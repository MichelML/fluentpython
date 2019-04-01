import numpy as np

arr = np.array([np.arange(1, 4, 1), np.arange(4, 7, 1)])
print(list(map(list, arr)))

print(arr * arr)
print(arr - arr)
print(1 / arr)
print(arr ** 0.5)

arr2 = np.array([[0, 4, 1], [7, 2, 12]])
arr2 > arr

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = np.full(3, 12)
print(arr)

arr3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr3d)
print(arr3d[0])
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names == 'Bob'
cond = names == 'Bob'

data = np.random.randn(7, 4)
data[~cond]

# The Python keywords and and
# or do not work with boolean arrays. Use
# & (and) and | (or)
# instead. 

