import os

"""самая простая и вместе с тем одна из самых важных команд для Python-разработчика – показать текущий
каталог. Она нужна, потому что разработчики чаще всего имеют дело с относительными путями, но в некоторых случаях 
важно знать, где мы находимся."""

print("Current directory:", os.getcwd())

"""Прежде чем задействовать команду по созданию файла  или каталога, стоит убедиться, что аналогичных элементов
ещё нет. Это поможет избежать ряда ошибок, включая перезапись существующих элементов с данными."""

print(os.path.exists("../matrix.py"))     # True - файл есть. False - файла нет

"""Если вы хотите, чтобы ваше приложение было кроссплатформенным, не стоит использовать “/” как разделитель пути, 
некоторые старые версии Windows распознают только “\” в качестве разделителя. Python решает эту 
проблему – os.path.join()"""

path = os.path.join('data', 'README.nd')
right_or_not = os.path.exists(path)           # and check if it exists
print(right_or_not)

"""Создать новую директорию можно командой mkdir. Если мы попытаемся создать директорию, которая уже существует, то 
получим исключение, поэтому лучше всегда проверять наличие одноимённого каталога перед созданием"""

print(f"test_dir exists {os.path.exists('test_dir')}")     # False
#os.mkdir("test_dir")                                       # I make file
print(f"test_dir exists {os.path.exists('test_dir')}")     # True there is file

"""иногда нам нужно создать подкаталоги с уровнем вложенности 2 и более. Если мы всё ещё используем os.mkdir(), 
нам нужно будет вызвать её несколько раз. Для таких ситуаций можно использовать os.makedirs(), она позволит создать
все необходимые промежуточные каталоги."""

#os.makedirs(os.path.join('files_in', 'level1', 'level2', 'level3'))

"""Ещё одна полезная команда – os.listdir(), она показывает всё содержимое каталога."""

print(os.listdir('../subject_05'))

"""C помощью модуля os достаточно просто переименовать файл:"""

#os.rename('имя файла', 'новое имя файла')

"""Функцию os.replace() можно использовать для перемещения файлов или каталогов. Стоит обратить внимание, что если 
в папке folder уже есть файл с таким именем, он будет полностью перезаписан."""

#os.replace('renamed-matrix.py', 'other information/renamed-matrix.py')

"""Если вывод os.listdir() оказывается недостаточным, и нам нужно узнать состав всех вложенных каталогов, можно
использовать os.walk() – генератор дерева каталогов. ”.” здесь – корень дерева."""

for subject_05, subject_06, subject_07 in os.walk("."):

    for lesson in subject_06:
        print("Каталог:", os.path.join(subject_05, lesson))

    for lesson2 in subject_07:
        print("Файл:", os.path.join(subject_05, lesson2))

"""Удалить существующий файл (не каталог) можно командой os.remove()"""

os.remove("folder/renamed-text.txt")

"""C помощью функции os.rmdir() можно удалить указанную папку. Для удаления каталогов рекурсивно стоит 
использовать os.removedirs()"""

os.rmdir("folder")

"""Для получения информации о файле используется функция os.stat(), которая вернёт кортеж с несколькими метриками.
● st_size – размер файла в байтах
● st_atime – время последнего доступа
● st_mtime – время последнего изменения
● st_ctime – в Linux это время последнего изменения метаданных, в Windows – время создания файла"""

open("text.txt", "w").write("Some data")

print(os.stat("text.txt"))