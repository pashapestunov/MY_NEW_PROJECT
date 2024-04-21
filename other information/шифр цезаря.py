"""
5. Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное
сообщение шифром Цезаря, вторая расшифровывает. В
зависимости от выбора пользователя (шифровать или
дешифровать) вызывается соответствующая функция,
результат выводится в консоль.
"""

alhfavit_EU =  ('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
alhfavit_RU = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

step_cip = int(input("Шаг шифраваня: "))         #Создаем переменную с шагом шифровки
message = input("Сообщение для шифровки: ").upper()     #создаем переменнную, куда запишем наше сообщение
itog = ""                                   #создаем переменную для вывода итогового сообщения
land = input("Выберите язык EU/RU: ")

if land == "RU":
    for i in message:
        mesto = alhfavit_RU.find(i)                    #Вычисляем места символов в списке
        new_mesto = mesto + step_cip                #Сдвигаем символы на указанный в переменной smeshenie шаг
        if i in alhfavit_RU:
            itog += alhfavit_RU[new_mesto]       # Задаем значения в итог
        else:
            itog += i
else:
    for i in message:
        mesto = alhfavit_EU.find(i)
        new_mesto = mesto + step_cip
        if i in alhfavit_EU:
            itog += alhfavit_EU[new_mesto]
        else:
            itog += i
print(itog)