import itertools  
gen = itertools.count(1, .5)

for i in range(1,10):
  print(next(gen))