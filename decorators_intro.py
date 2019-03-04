# A decorator is a callable that takes another function as argument

# Strictly speaking, decorators are just syntactic sugar. 
# As we just saw, you can always simply call a 
# decorator like any regular callable, passing 
# another function. Sometimes that is actually 
# convenient, especially when doing metaprogramming changing 
# program behavior at runtime. 

# They are executed immediately when a module is loaded


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

