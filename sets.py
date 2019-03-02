# set is a collection of unique objects
needles = ['spam', 'spam', 'eggs', 'spam']
haystack = ['spam', 'spam', 'eggs', 'spam', 'ham', 'cheese']
print(set(needles))
print(list(set(needles)))

# Count occurrences of needles in a haystack; these lines work for any iterable types
found = len(set(needles) & set(haystack))
print(found)

# secound method
found = len(set(needles).intersection(haystack))
print(found)

# set literals
sl = {1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4}
print(sl)

# empty set
m = {}
print(m)
print(type(m)) # dict
m = set()
print(m)
print(type(m)) # set
