from inspect import getgeneratorstate

def simple_coro2(a):
  print('a = ', a)
  b = yield a
  print('b = ', b)
  c = yield a + b
  print('c = ', c)

my_coro2 = simple_coro2(14)
print(getgeneratorstate(my_coro2))
next(my_coro2)
print(getgeneratorstate(my_coro2))
my_coro2.send(22)
print(getgeneratorstate(my_coro2))
try:
  my_coro2.send(99)
except:
  print(getgeneratorstate(my_coro2))
