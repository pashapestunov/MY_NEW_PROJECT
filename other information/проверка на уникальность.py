"""
Дан список чисел. Реализовать программу, которая
проверит, все ли числа в списке уникальны (встречаются
только один раз). Программа должна вывести результат
проверки, и, если не все элементы уникальны, вывести
дублирующиеся элементы и количество их повторений в
списке.
"""

run = True

numbers = [5, 3, 4, 7, 12, 33, 1, 2, 3, 54, 11, 12,]

print(f'\nДан список: {numbers}')

result_list = {}

for item in numbers:
    result_list[item] = result_list.get(item, 0) + 1

clones = {item: count for item, count in result_list.items() if count >1}

if clones:
    print(f'Одинаковые значения: {clones}')
else:
    print('Одинаковых сначений нет!')
