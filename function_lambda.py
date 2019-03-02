fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sortedfruits = sorted(fruits, key=lambda word: word[::-1])
print(sortedfruits)