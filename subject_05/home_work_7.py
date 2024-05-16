"""
Реализовать алгоритм бинарного поиска по
сдвинутому списку отсортированных чисел (например, дан
список [5, 6, 7, 1, 2, 3, 4])
"""


def find_num(lst, search_num):
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_num:
            return True
        elif guess > search_num:
            high = middle - 1
        else:
            low = middle + 1
    return False


lst = [2, 99, 15, 45, 65, 66, 88, 13]
lst.sort()
value = int(input("Введите число для поиска: "))

result = find_num(lst, value)
if result:
    print("Число найдено")
else:
    print("Число не найдено")
