"""
2.Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""

number = [1, 2, -4, 0, 12, -5, 0, 32, -34]

next = (list(filter(lambda x: x > 0, number)))
print(next)