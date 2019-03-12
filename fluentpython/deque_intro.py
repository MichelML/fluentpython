# The class collections.deque is a thread-safe double-ended queue
# designed for fast inserting and removing from both ends. It
# is also the way to go if you need to keep a list of “last seen items”
# or something like that, because a deque can be bounded i.e., created
# with a maximum length and then, when it is full, it discards items from
# the opposite end when you append new ones.

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)
