import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
result

result = np.where(cond, xarr, yarr)
result


# replace all positive values with 2 and negative values with -2
arr = np.random.randn(4, 4)
arr
arr > 0
np.where(arr > 0, 2, -2)