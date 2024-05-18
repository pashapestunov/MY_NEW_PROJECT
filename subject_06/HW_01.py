"""
1. Дан список чисел, отсортированных по возрасту.
При входе принимается значение, равное одному из элементов
список. Реализовать функция, исполнительная рекурсивный
алгоритм бинарного определения, на выходе программа должна
вывести позицию искомого элемента в исходном списке.
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
