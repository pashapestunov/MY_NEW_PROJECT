"""
Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке.
"""

from collections import Counter
import os

def count_words_in_line(line):
    word_count = Counter(line.split()) # разбиваем строку на слова и считаем кол-во повторений
    # фильтруем слова, которые встречаются 2 раза и больше
    return {word: count for word, count in word_count.items() if count>=2}

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:   # open file for read
            #print(f"Файл {file_path} успешно открыт")
            for line_number, line in enumerate(file, start=1): # считываем все строки и обробатываем
                #print(f"Строка {line_number}: {line.strip()}")
                line = line.strip()
                word_count = count_words_in_line(line)
                if word_count:
                    print(f'Строка {line_number}:')
                    for word, count in word_count.items():
                        print(f"    {word}: {count}")
                else:
                    print(f"Строка {line_number}: слова, свтречающиеся 2 паза и более, отсутствуют")
    except FileNotFoundError:
        print("Файл не найден.")

file_path = "random-text.txt"

count_words_in_file(file_path)