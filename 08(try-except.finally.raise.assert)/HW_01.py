"""
1. Реализовать программу для подсчёта индекса массы
тела человека. Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать обработку
исключений.
"""


def index(height, weight):
    if height <= 0 or weight <= 0:
        return "Вес или Рост не может быть отрицательным или равняться нулю"
    imt = weight / (height / 100) **2
    return imt


def imt_info(imt):
    if imt <= 20:
        return "Вы очень худой"
    elif 20 <= imt <= 30:
        return "Вы стройный"
    elif 30 <= imt <= 40:
        return "Вам нужно немного скинуть"
    else:
        return "Таких данных не может быть или у вас большие проблемы!"


try:
    height = int(input("Введите свой рост в \"см\": "))
    weight = int(input("Введите свой вес в \"кг\": "))

    find_index = index(height, weight)
    talk_you = imt_info(find_index)

    print(f"Ваш индекс массы тела: {find_index:.2f}")
    print(f"Интрепритация: {talk_you}")

except ValueError as hw:
    print(f"Ошибка {hw}")