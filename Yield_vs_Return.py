def func(n):
    for i in range(0,n):
        if (i % 2) == 0:
            return i
print(func(10))


def func2(n):
    for i in range(0,n):
        if (i % 2) == 0:
            yield i
print(func2(10))