

def some_func(*args, **kwargs):
    a = 3
    print(type(args))
    print(type(kwargs))
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


some_func(1, 2, one_claas=10, two_claas=20)


def sum(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    return x + y


print(sum.__doc__)