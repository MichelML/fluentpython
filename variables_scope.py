b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


print(f3(1))
