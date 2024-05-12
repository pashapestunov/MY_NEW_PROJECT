def find_tens(number):
    result = (number // 10) % 10
    print(f'В числе {number} найдено {result} десятков')
    return result


number = int(input('Введите число: '))

if number >= 10:
    find_tens(number)
else:
    print(f'В числе {number} нет ни одного десятка')


def find_sum(num):
    x = num // 100
    y = (num % 100) // 10
    z = num % 10
    result = x + y + z
    print(f'Сумма цифр {num} будет: {result}')
    return result


num = int(input('Введите трехзначное число: '))
otvet = find_sum(num)

