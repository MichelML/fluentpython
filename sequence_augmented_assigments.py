l = [1, 2, 3]
print(l)
print(id(l))

l *= 2
print(l)
print(id(l))

t = (1, 2, 3)
print(t)
print(id(t))
t *= 2
print(t)
print(id(t))

# recommendations from the author
# 1. Putting mutable items in tuples is not a good idea.
# 2. Augmented assignment is not an atomic operation we just saw it throwing an exception after doing part of its job.
# 3. Inspecting Python bytecode is not too difficult, and is often helpful to see what is going on under the hood.