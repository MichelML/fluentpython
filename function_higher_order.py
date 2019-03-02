# A function that takes a function as argument or returns a function as the result is a higher-order function 
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

def reverse(word):
  return word[::-1]

print(reverse('testing'))
print(sorted(fruits, key=reverse))