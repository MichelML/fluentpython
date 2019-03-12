def gen():
  yield from 'AB'
  yield from range(1, 3)

genned = list(gen())
print(genned)