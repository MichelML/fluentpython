# A memoryview is essentially a generalized NumPy array structure in Python itself
# (without the math). It allows you to share memory between data-structures
# (things like PIL images, SQLlite databases, NumPy arrays, etc.) without first copying.
# This is very important for large data sets.

from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)

print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
print(memv_oct[5])
