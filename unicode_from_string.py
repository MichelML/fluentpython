# version 1
symbols = '$@#$%'
codes = []

for symbol in symbols:
  codes.append(ord(symbol))

print(codes)

# version 2
symbols = '$@#$%'
codes = [ord(symbol) for symbol in symbols]
print(codes)