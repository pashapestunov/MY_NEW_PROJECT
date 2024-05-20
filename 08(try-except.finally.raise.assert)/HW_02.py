"""
2. Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку
исключений.
"""


def plus(x, y):
    sm = x + y
    return sm

def minus(x, y):
    ms = x - y
    return ms

def multiplication(x, y):
    mk = x * y
    return mk

def division(x, y):
    if y == 0:
        raise ValueError("Делить на ноль нельзя")
    dv = x / y
    return dv

def mat(x, y, mark):
    if mark == "+":
        solution = plus(x, y)
    elif mark == "-":
        solution = minus(x, y)
    elif mark == "*":
        solution = multiplication(x, y)
    elif mark == "/":
        solution = division(x, y)
    else:
        raise ValueError("Неподдерживаемая операция")
    return solution


try:
    first = int(input("Первое число: "))
    second = int(input("Второе число: "))
    mark = input("Что с этим сделать: +, -, *, / ?: ")

    final = mat(first, second, mark)
    print("Результат: ", final)

except ValueError as ve:
    print("Ошибка", ve)
except ZeroDivisionError:
    print("Делить на 0 нельзя")






