# A decorator is a callable that takes another function as argument

def decorate(callback):
  return callback()

@decorate
def target():
  print('running target()')

# has the same effect as 
# def target():
#   print('running target()')

# target = decorate(target)

# decorator usually replaces a function with a different one 