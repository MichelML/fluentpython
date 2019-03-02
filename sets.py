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
