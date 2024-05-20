import sqlite3

# Создаем подключение к базе данных (файл 'my_data.db' будет создан)
connection = sqlite3.connect('my_databesw.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Создаем индекс для столбца 'email'
cursor.execute('CREATE INDEX idx_email ON Users (email)')

# Добавим нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
               ('newuser', 'newuser@example.com', 28))

# Обновляем возраст пользователя 'newuser'
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

# Удаляем пользователя 'newuser'
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# Достаем все данные
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

""" Примеры операторов SELECT, FROM, WHERE"""
# Выбиваем имена и возраст пользователей чей возраст старше 25 лет
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
result = cursor.fetchall()

for row in result:
    print(row)

""" Примеры операторов GROUP BY and HAVING"""
# Получаем средний возраст пользователей для каждого восраста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
result = cursor.fetchall()

for row in result:
    print(row)

# Фильтруем группы по сред. возрасту больше 30
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filter_result = cursor.fetchall()

for row in filter_result:
    print(row)

""" Примеры операторов ORDER BY используется для сортировки результатов по указанным столбцам"""
# Выбираем и сортируем пользователей по возрасту по убыванию
cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
result = cursor.fetchall()

for row in result:
    print(row)



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
