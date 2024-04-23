"""
Дан список чисел. Реализовать программу, которая
посчитает сумму всех чисел в списке, а также найдет
минимальный и максимальный элементы.
"""


print("""Список команд для программы:
nim number - показывает минимальное число в списке.
max number - показвает максимальное число в списке.
sum numbers - показывает сумму всех чисел в списке.
numbers - показывает все числа в списке.
break - заверает программу.
""")

list_numbers = []
go = True

while go:
    command = input("Введите число для добавления в список или команду\n")
    if command == "min number":
        print(f"Минимальное число в списке: {min(list_numbers)}")
    elif command == "max number":
        print(f"Максимальное число в списке: {max(list_numbers)}")
    elif command == "sum numbers":
        print(f"Сумма всех чисел в списке: {sum(list_numbers)}")
    elif command == "numbers":
        print(list_numbers)
    elif command == "break":
        break
    else:
        list_numbers.append(int(command))
        print(f"Число {command} в список добаленно!")
