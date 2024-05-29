
def call_with_five(function):
    return function(5)


def add_one(x):
    return x + 2


print(call_with_five(add_one))


def double(function):
    def inner(argument):
        return function(function(argument))
    return inner


def multiply_by_five(x):
    return x * 7


print(double(multiply_by_five)(3))   # (7 * 3) * 7 = 147