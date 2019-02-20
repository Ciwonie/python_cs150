# Hey friends, I made a small changes to the professors examples
def someFunction(a, b):
    c = a+b
    return c


d = someFunction(10, 5)
print(d)


def mayIncrement(a):
    b = 5
    c = a + b
    if c % 3 == 0:
        return c
    else:
        return a


f = mayIncrement(4)
print(f)
