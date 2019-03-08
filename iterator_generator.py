def gen_123():
  yield 1
  yield 2
  yield 3

for i in gen_123():
  print(i)

g = gen_123()
print(next(g))
print(next(g))
print(next(g))

def gen_AB():
  print('start')
  yield 'A'
  print('continue')
  yield 'B'
  print('end')

for i in gen_AB():
  print(i)