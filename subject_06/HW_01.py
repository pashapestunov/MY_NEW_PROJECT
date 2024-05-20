"""
1. Дан список чисел, отсортированных по возрасту.
При входе принимается значение, равное одному из элементов
список. Реализовать функция, исполнительная рекурсивный
алгоритм бинарного определения, на выходе программа должна
вывести позицию искомого элемента в исходном списке.
"""

from typing import List, Optional


def find_num(list_1: List[int], num: int, min: int, max: int) -> Optional[int]:
    if max >= min:
        middle = min + (max - min) // 2
        if list_1[middle] == num:
            return middle
        elif list_1[middle] < num:
            return find_num(list_1, num, middle + 1, max)
        else:
            return find_num(list_1, num, min, middle - 1)
    else:
        return None


list_1 = sorted([1, 2, 4, 5, 3, 7, 8, 9, 6, 10])
print(list_1)

num = int(input('Введите число из списка для поиска его индекса: '))

index = find_num(list_1, num, 0, len(list_1) - 1)

if index is not None:
    print(f'Чсло находиься под индексом: {index}')
else:
    print('Число не найдено')