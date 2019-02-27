# * and + always create a new object and do not modify their operands
l = [1, 2, 3]
print(l*5)
print(5 * 'abcd')
print([1,2,3] + [3])

# Beware of expressions like a * n when a is a sequence containing mutable items because the result may surprise you. For example, trying to initialize a list of lists as my_list = [[]] * 3 will result in a list with three references to the same inner list, which is probably not what you want. 