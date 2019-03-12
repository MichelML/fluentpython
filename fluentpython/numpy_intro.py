import numpy

# multi-dimensional arrays
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)

a.shape = 3,4
print(a)
print(a[2,1])
print(a[:,1])

print(a.transpose())

# NumPy also supports high-level operations for loading,
# saving, and operating on all elements of a numpy.ndarray
