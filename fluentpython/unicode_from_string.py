# version 1
symbols = '$@#$%'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# version 2 (list comprehensions, or listcomps) - best solution
symbols = '$@#$%'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# version 3 (map and filter)
symbols = '$@#$%'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 35]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c:c > 35, map(ord, symbols)))
print(beyond_ascii)