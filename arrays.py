# A Python array is as lean as a C array. When creating an array ,
# you provide a typecode, a letter to determine the underlying C type used
# to store each item in the array. For example, b is the typecode for
# signed char . If you create an array('b') , then each item will be stored
# in a single byte and interpreted as an integer from –128 to 127. For large sequences of
# numbers, this saves a lot of memory. And Python will not let you put any number
# that does not match the type for the array.
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
print(floats2[:5])
fp.close()
