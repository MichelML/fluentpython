def deco(printprint=True):
    def decorate(func):
        def newfunc(n):
            if printprint:
                print('print!')

            return func(n)

        return newfunc

    return decorate


@deco(printprint=False)
def simple_func(n):
    print(n)


@deco()
def simple_func2(n):
    print(n)


simple_func(1)
simple_func2(2)
