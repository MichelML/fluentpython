# My rule of thumb in choosing the syntax to use is simple: 
# if the generator expression spans more than a couple of lines,
# I prefer to code a generator function for the sake of readability. 

# arithmetic progression generator
class ArithmeticProgression:
  def __init__(self, begin, step, end=None):
    self.begin = begin
    self.step = step
    self.end = end # None --> 'infinite' series

  def __iter__(self):
    result = type(self.begin + self.step)(self.begin)
    forever = self.end is None
    index = 0
    while forever or result < self.end:
      yield result 
      index += 1
      result = self.begin + self.step * index


