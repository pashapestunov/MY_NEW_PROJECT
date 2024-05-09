"""
Напишите программу, которая получает на вход строку с названием текстового файла и выводит на экран содержимое этого
файла, заменяя все запрещённые слова звездочками. Запрещённые слова, разделённые символом пробела, должны храниться
в файле stop_words.txt. Программа должна находить запрещённые слова в любом месте файла, даже в середине другого слова.
Замена независима от регистра: если в списке запрещённых есть слово exam, то замениться должны exam, eXam, EXAm и
другие вариации.
Пример: в stop_words.txt записаны слова: hello email
python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python
IS the programming language of thE future. My EMAIL is...
PYTHON as AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming
language of *** future. My ***** **... ****** ** awesome!!!!
"""

def censor_text(input_file, stop_words_file):
    # читаем запрещенные слова их файла
    with open(stop_words_file, 'r', encoding='utf-8') as stop_words_file:
        stop_words = stop_words_file.read().split()
    # читаем текст из файла
    with open(input_file, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    # приводим все слова к нижнему регистру
    text_lower = text.lower()
    # заменяем запрещенные слова на звездочки
    for word in stop_words:
        text_lower = text_lower.replace(word.lower(), '*' * len(word))
    # выводим отредактированный текст
    print(text_lower)

input_file = input("Какой и этих файлов проверить: file-one.txt or file-two.txt or file-three.txt: ")
stop_words_file = 'stop_words.txt'
# вызываем функцию
censor_text(input_file, stop_words_file)

