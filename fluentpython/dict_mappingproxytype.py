# MappingProxyType , which, given a mapping,
# returns a mappingproxy instance that is a read-only but dynamic
# view of the original mapping.

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d_proxy[1]
# the next line wil work
d[2] = 'B'
print(d_proxy)
# the next line will throw
d_proxy[2] = 'x'

