"""
В текстовый файл построчно записаны фамилия и имя учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.
"""


def find_students_below_grade(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file: # открываем файл для чтения
            print(f'Студенты с оценкой ниже трех в файле {file_path}:')
            for line_number, line in enumerate(file, start=1): # считываем каждую строку и обрабатываем её
                last_name, first_name, grade = line.strip().split() # разбираем строку на фамилию, имя, оценку
                grade = float(grade) # приобразуем оценку в числовой формат
                if grade < 3.0: # Проверяем, если оценка меньше трех, выводим онформацию о студенте
                    print("{} {} оценка: {}".format(last_name, first_name, grade))
    except FileNotFoundError:
        print("Файл не найден")


file_path = 'class.txt' # путь к файлу

find_students_below_grade(file_path) # вызываем функцию




