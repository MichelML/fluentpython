import numpy as np

# Universal functions (ufunc): Fast Element-Wise Array functions
## also known as fast vectorized wrappers for simple functions that take one or more scalar values
## and produce one or more scalar results

## Many ufuncs are simple element-wise transformations, like sqrt or exp:

arr = np.arange(10)
arr

# sqrt, exp, maximum, modf are u funcs
np.sqrt(arr)
np.exp(arr)

x = np.random.randn(8)
y = np.random.randn(8)
x
y
np.maximum(x, y)

arr = np.random.randn(7) * 5
arr
remainder, whole_part = np.modf(arr)
remainder
whole_part

# there are unary and binary ufuncs https://docs.scipy.org/doc/numpy-1.14.0/reference/ufuncs.html