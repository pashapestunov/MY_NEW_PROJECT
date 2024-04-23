
spicok = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(list(map(lambda x: x ** 2, spicok)))

def my_func(x):
    if x % 2 == 0:
        return True
    return False
print(list(filter(my_func, (spicok))))

print(list(filter(lambda x: x % 2 == 0, spicok)))