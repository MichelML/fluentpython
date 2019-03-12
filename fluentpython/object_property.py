from array import array
import math

class Vector2d:
  typecode = 'd'

  def __init__(self, x, y):
    self.__x = float(x)
    self.__y = float(y)

  @property
  def x(self):
    return self.__x

  @property
  def y(self):
    return self.__y

  def __iter__(self):
    return (i for i in (self.x, self.y))

  def __repr__(self):
    class_name = type(self).__name__ 
    return '{}({!r}, {!r})'.format(class_name, *self)

  def __format__(self, fmt_spec=''):
    components = (format(c, fmt_spec) for c in self)
    return '({}, {})'.format(*components)