"""
Реализовать алгоритм бинарного поиска по
сдвинутому списку отсортированных чисел (например, дан
список [5, 6, 7, 1, 2, 3, 4])
"""

def find_num(lst, search_num):
    low = 0
    high = len(lst) - 1
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_num:
            result_srh = True
            return result_srh
        if guess > search_num:
            high = middle - 1
        else:
            low = middle + 1
    return search_res

lst = [2, 13, 15, 24, 66, 76, 88, 99]
value = int(input("Введите число для поиска: "))

result = find_num(lst, value)
if result:
    print("Число найдено")
else:
    print("Число не найдено")
