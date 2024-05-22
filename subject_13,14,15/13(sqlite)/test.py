import sqlite3

""" Создание простого приложения для управления задачами с использованием SQLite и Python """

# устанавливаем соединение с базой данных
connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

# создаем таблицу Tasks
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasks (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
status TEXT DEFAULT 'Not Started'
)
''')


# фуенкция для добавления новой задачи
def add_task(title):
    cursor.execute('INSERT INTO Tasks (title) VALUES (?)', (title,))
    connection.commit()


# функция для обнавления статуса задачи
def update_task_status(task_id, status):
    cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
    connection.commit()


# функция для вывода списка задач
def list_tasks():
    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)


add_task('Выучить SQL')
add_task('Выучить English')
add_task('поесть')

update_task_status(2, 'In Progress')

list_tasks()

connection.close()

