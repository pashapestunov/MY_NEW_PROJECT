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

"""
Второй способ 
"""


def find_num(list_1, num, min, max):
    if max >= min:
        middle = min + (max - min) // 2
        if list_1[middle] == num:
            return middle
        elif list_1[middle] < num:
            return find_num(list_1, num, middle + 1, max)
        else:
            return find_num(list_1, num, min, middle - 1)
    else:
        return


list_1 = sorted([3, 4, 1, 2, 9, 5, 7, 6, 8, 10])
print(list_1)
num = int(input("Какое число из списка нужно найти?: "))
print("Число, которое вы искали, находиться под индексом:", find_num(list_1, num, 0, len(list_1) - 1))