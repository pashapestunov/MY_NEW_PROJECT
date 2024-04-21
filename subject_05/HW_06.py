"""
6.Cм. предыдущую задачу, но вместо шифра Цезаря
использовать шифр Виженера.
"""
HELP = """
help - напечатать справку по программе.
text - добавить текст для шифровки.
show - показывает заметки.
back - Дешифровать текст.
"""

alhfavit_EU = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number_EU = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
alhfavit_RU = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ')
number_RU = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
             28, 29, 30, 31, 32, 33)


run = True
itog_RU = ""
itog_RU_back = ""
itog_EU = ""
itog_EU_back = ""

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("заметки на русском:", itog_RU)
        print("заметки на русском Дешифрованые:", itog_RU_back)
        print("заметки на английском:", itog_EU)
        print("заметки на английском Дешифрованные:", itog_EU_back)
    elif command == "text":
        # step_cip = int(input("Шаг шифраваня: "))
        message = input("Сообщение для шифровки: ").upper()
        land = input("Выберите язык eu/ru: ")
        if land == "ru":
            for i in message:
                mesto = alhfavit_RU.find(i)
                new_mesto = mesto + 3
                if i in alhfavit_RU:
                    itog_RU += alhfavit_RU[new_mesto]
                else:
                    itog_RU += i
        else:
            for i in message:
                mesto = alhfavit_EU.find(i)
                new_mesto = mesto + 3
                if i in alhfavit_EU:
                    itog_EU += alhfavit_EU[new_mesto]
                else:
                    itog_EU += i
    elif command == "back":
        message = input("Сообщение для Дешифровки: ").upper()
        land = input("Выберите язык eu/ru: ")
        if land == "ru":
            for i in message:
                mesto = alhfavit_RU.find(i)
                new_mesto = mesto - 3
                if i in alhfavit_RU:
                    itog_RU_back += alhfavit_RU[new_mesto]
                else:
                    itog_RU_back += i
        else:
            for i in message:
                mesto = alhfavit_EU.find(i)
                new_mesto = mesto - 3
                if i in alhfavit_EU:
                    itog_EU_back += alhfavit_EU[new_mesto]
                else:
                    itog_EU_back += i
    else:
        print("ОШИБКА! Введите команду \"help\" ")
        break