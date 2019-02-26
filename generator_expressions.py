# To initialize tuples, arrays, and other types of sequences,
# you could also start from a listcomp, but a genexp saves memory because
# it yields items one by one using the iterator protocol instead of building a
# whole list just to feed another constructor. Genexps use the same syntax as listcomps, 
# but are enclosed in parentheses rather than brackets.

import array

symbols = '$¢£¥€¤'

symtuple = tuple(ord(symbol) for symbol in symbols)
print(symtuple)

symarray = array.array('I', (ord(symbol) for symbol in symbols))
print(symarray)

# cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
  print(tshirt)
