"""Работа с модулем os Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
● Вывести имя вашей ОС
● Вывести путь до папки, в которой вы находитесь
● Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений
● После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт»
● Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt»
● Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами"""

import os
import shutil
import re

#1 print(os.name)
#2 print('some_files', os.getcwd())
# print(os.path.exists('../files_py'))
# print(os.path.exists('../files_txt'))
# os.mkdir('files_py')
# os.mkdir('files_txt')
# check = os.path.join('..', 'subject_09', 'some_files')
# print(os.listdir(check))

source_dir = os.path.join('..', 'subject_09', 'some_files') # путь к файлам с учетом особенности ОС
destination_dir = os.path.join('..', 'subject_09', 'files_py') # куда нужно переместить файлы

extension_folders = {}  # словарь для хранения папок с расширениями
files = os.listdir(source_dir)  # получем список файлов в исходной папке

for file in files:  # создаем папки для каждого типа расширения
    if os.path.isfile(os.path.join(source_dir, file)):  # является ли путь файлом
        _, ext = os.path.splitext(file)  # разбивает путь на пару(root, ext) где ext начинается с одной точки
        if ext not in extension_folders:
            extension_folders[ext] = os.path.join(destination_dir, ext[1:])  # забираем расширение файла без точки
            os.makedirs(extension_folders[ext], exist_ok=True)  # создаем папку и игнорируем папки с тамиже именами

for file in files:
    if os.path.isfile(os.path.join(source_dir, file)):   # является ли путь файлом
        _, ext = os.path.splitext(file)  # разбивает путь на пару(root, ext) где ext начинается с одной точки
        src_path = os.path.join(source_dir, file)
        dst_path = os.path.join(extension_folders.get(ext, destination_dir), file)
        shutil.move(src_path, dst_path)

print("Файлы успешно рассортированы.")

destination_dir = os.path.join('..', 'subject_09', 'files_py')  # путь к целевой папке
files_count = {}        # создаем словарь для хранения кол-ва файдов в каждой папке

# Получаем список всех папок в целевой папке
subdirectories = [d for d in os.listdir(destination_dir) if os.path.isdir(os.path.join(destination_dir, d))]

# Подсчитываем кол-во файлов в каждой папке
for folder in subdirectories:
    files_count[folder] = len(os.listdir(os.path.join(destination_dir, folder)))

# Выводим корл-ва файлов в каждой папке
for folder, count in files_count.items():
    print(f"В папке {folder} перемещено {count} файлов.")
