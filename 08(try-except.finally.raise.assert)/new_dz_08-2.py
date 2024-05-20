
def math(fun, x, y):
    return fun(x, y)


def summa(x, y):
    return x + y


def diff(x, y):
    return x - y


def mult(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ZeroDivisionError('Deversion by zero in not allowed')
    return x / y


try:
    a = float(input('Первое число: '))
    b = float(input('Второе число: '))
    c = input('Знак действия: ')
    if c == '+':
        otw = math(summa, a, b)
    elif c == '-':
        otw = math(diff, a, b)
    elif c == '*':
        otw = math(mult, a, b)
    elif c == '/':
        otw = math(division, a, b)
    else:
        raise ValueError('Недопустимый знак действия')

    if otw.is_integer():
        otw = int(otw)
    else:
        otw = round(otw, 10)

    a = int(a) if a.is_integer() else a
    b = int(b) if b.is_integer() else b

    print(f'Ответ на {a} {c} {b} = {otw}')
except ValueError as v:
    print('Ошибка', v)
except ZeroDivisionError as z:
    print('Ошибка', z)
