"""
2. Программа получает входное число в десятичной
система счисления. Реализовать функция, которая
переводит входное число в двойную систему вычислений.
Осуществляет реализацию функций как в рекурсивном
вариант, так и с итеративным подходом.
"""


def ten_in_two(num: int) -> str:
    dict_num = []

    while num > 0:
        dict_num.append(num % 2)
        num //= 2

    dict_num.reverse()

    dict_sting = ''.join(map(str, dict_num))

    return dict_sting


num = int(input('Введите число для перевода в двоичную: '))

next = ten_in_two(num)
print(f'Ваше число в двоичной форме: {next}')