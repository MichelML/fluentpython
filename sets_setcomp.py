# Build set of characters with codes from 32 to 255 that have the word 'SIGN' in their names.

from unicodedata import name

m = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(m)
