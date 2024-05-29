"""В первой строке csv-файла обычно указывается, какая информация будет находиться в каждом столбце.
В конце строки данных разделитель (запятая) не ставится, новая запись начинается с новой строки."""

import csv

# with open('some_data.csv.py', encoding='utf-8') as r_file:
#     file_reader = csv.reader(r_file, delimiter=',')
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {",".join(row)}')
#         else:
#             print(f'    {row[0]} - {row[1]} и он родился в {row[2]}')
#         count +=1
#     print(f"Всего в файле {count} строк.")

"""Библиотека csv позволяет работать с файлами как со словарями. Для этого нужно вместо reader создать объект 
DictReader. Обращаться к элементам можно будет по имени столбцов, а не по индексам."""

with open('some_data.csv.py', encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=',')
    count = 0

    for row in file_reader:
        if count == 0:
            print(f'Файл содержит столбцы: {",".join(row)}')
        print(f'    {row["Имя"]} - {row["Профессия"]}', end='')
        print(f'    и он родился в {row["Год рождения"]}, году.')
        count +=1
    print(f"Всего в файле {count +1} строк.")

"""Для записи в csv-файл необходимо создать объект writer и использовать 
метод writerow() для записи одной строки данных."""

# with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
#     file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
#     file_writer.writerow(["Имя", "Класс", "Возраст"])
#     file_writer.writerow(["Женя", "3", "10"])
#     file_writer.writerow(["Саша", "5", "12"])
#     file_writer.writerow(["Каша", "11", "17"])

"""Запись в файл также может быть осуществлена с помощью объекта DictWriter, он требует явного указания 
названий столбцов (fieldnames)"""

# with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
#     names = ["Имя", "Класс", "Возраст"]
#     file_writer = csv.DictWriter(w_file, delimiter=",",
#                         lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Женя", "Класс": "3", "Возраст": "10"})
#     file_writer.writerow({"Имя": "Вова", "Класс": "5", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Саша", "Класс": "11", "Возраст": "17"})
