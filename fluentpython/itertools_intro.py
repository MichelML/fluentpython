import itertools  
gen = itertools.count(1, .5)

for i in range(1,10):
  print(next(gen))

def aritprog_gen(begin, step, end=None):
  first = type(begin + step)(begin)
  ap_gen = itertools.count(first, step)
  if end is not None:
    ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
  return ap_gen

gen2 = aritprog_gen(0, .2)
for i in range(1,100):
  print(next(gen2))