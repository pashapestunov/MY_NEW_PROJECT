"""
3. Программа получает входное число. Реализовать
функция, которая определяет, является ли это простым значением
(делится только на единицу и на себя.
"""

import math


num = int(input('Введите число для проверки: '))

if num <= 1:
    print('Число дожно быть больше 1')
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % 2 == 0:
            is_prime = False
            break

    if is_prime:
        print('Ваше чило простое')
    else:
        print('Ваше число не простое')
