# Some introductory texts about Python present tuples as “immutable lists,”
# but that is short selling them. Tuples do double duty: they can be used as
# immutable lists and also as records with no field names.
# This use is sometimes overlooked, so we will start with that.

# tuples as records
# Tuples hold records: each item in the tuple holds the data for one field and the
# position of the item gives its meaning.

import os

lax_coordinates = (33.9425, -118.408056)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE34876'), ('ESP', 'XDA9347')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


# Tuple unpacking
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

## swapping value of two variables
a = 1
b = 2
b, a = a, b
c, d = 3, 4
print(a, b, c, d)

## prefixing an argument with a star when calling a function
divmod(20, 8)
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

## excess items
a, b, *rest = range(5)
print(a, b, rest)

## middle items
a, *body, c = range(5)
print(a, body, c)
