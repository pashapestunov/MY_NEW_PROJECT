import sqlite3

# Создаем подключение к базе данных (файл 'my_data.db' будет создан)
connection = sqlite3.connect('my_data.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
is_active INTEGER DEFAULT 1
)
''')

# Создаем индекс для столбца 'email'
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Добавим нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
               ('newuser', 'newuser@example.com', 28))

# доьавим сразу несколько пользователей

users_to_add = [
    ('pasha', 'pasha@.com', 26),
    ('tanya', 'tanya@.com', 32),
    ('dominika', 'donimika@.com', 10)
]

cursor.executemany('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', users_to_add)

connection.commit()

# Обновляем возраст пользователя 'newuser'
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

# Удаляем пользователя 'newuser'
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# Достаем все данные
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Примеры операторов SELECT, FROM, WHERE
# Выбираем имена и возраст пользователей, чей возраст старше 25 лет
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
result = cursor.fetchall()

for row in result:
    print(row)

# Примеры операторов GROUP BY and HAVING
# Получаем средний возраст пользователей для каждого возраста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
result = cursor.fetchall()

for row in result:
    print(row)

# Фильтруем группы по среднему возрасту больше 30
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filter_result = cursor.fetchall()

for row in filter_result:
    print(row)

# Примеры операторов ORDER BY для сортировки результатов по указанным столбцам
# Выбираем и сортируем пользователей по возрасту по убыванию
cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
result = cursor.fetchall()

for row in result:
    print(row)

# Комбинированный запрос
# Выбираем пользователей, у которых средний возраст в группе больше 30 и сортируем по возрасту по убыванию
cursor.execute('''
SELECT username, age
FROM Users
WHERE age > (SELECT AVG(age) FROM Users)
ORDER BY age DESC
''')
results = cursor.fetchall()

for row in results:
    print(row)

# Использование агрегатных функций: COUNT, SUM, AVG, MIN, MAX
# COUNT - подсчет количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

print('Общее количество пользователей:', total_users)

# SUM - суммирование числовых значений
cursor.execute('SELECT SUM(age) FROM Users')
total_age = cursor.fetchone()[0]

print('Общая сумма возрастов пользователей:', total_age)

# AVG - вычисление среднего значения
cursor.execute('SELECT AVG(age) FROM Users')
average_total = cursor.fetchone()[0]

print('Средний возраст пользователей:', average_total)

# MIN - нахождение минимального значения
cursor.execute('SELECT MIN(age) FROM Users')
min_age = cursor.fetchone()[0]

print('Минимальный возраст:', min_age)

# MAX - нахождение максимального значения
cursor.execute('SELECT MAX(age) FROM Users')
max_age = cursor.fetchone()[0]

print('Максимальный возраст:', max_age)


# примеры сложных запросов с объединением таблиц и подзапросами (давайте найдем пользователей и набольшим возрастом)
cursor.execute('''
SELECT username, age
FROM Users
WHERE age = (SELECT MAX(age) FROM Users)
''')
oldest_users = cursor.fetchall()
for user in oldest_users:
    print(user)


# получение результатов запроса в виде списка кортежей:
cursor.execute('SELECT * FROM Users')
full_list = cursor.fetchall()

for user in full_list:
    print(user)

# fetchone - первый, fetchmany() - какое-то кол-во, fetchall - все. это методы для порлучения данных:

cursor.execute('SELECT * FROM Users')
first = cursor.fetchone()
print(first)

cursor.execute('SELECT * FROM Users')
first_two_users = cursor.fetchmany(2)
print(first_two_users)

cursor.execute('SELECT * FROM Users')
full_users = cursor.fetchall()
print(full_users)


# преобразование результатов в более удобные структуры данных(списки, словари)
# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# преобразуем результаты  список словарей
users_list = []
for user in users:
    user_dict = {
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
    }
users_list.append(user_dict)

for user in users_list:
    print(user)


# Обработка IS NULL (IS NOT NULL) значений
# Выберем пользователей с неизвестным возрастом
cursor.execute('SELECT username, age FROM Users WHERE age IS NULL')
users_is_null = cursor.fetchall()

for user in users_is_null:
    print(user)


"""
                            Транзакции и управление данными
                            
Транзакции - это группа операций, выполняемых как единое целое. Они обеспечивают надежность и целостность данных,
гарантируя, что либо все операции будут выполнины успешно, либо ни одна из низ не будет применена.

Операторы BEGIN, COMMIT, ROLLBACK позволяют управлять транзакциями в SQLite. Оператор BEGIN начинает транзакцию,
COMMIT подтверждает изменения, а ROLLBACK отменяет транзакцию.
"""

try:
    # начинаем транзакцию
    cursor.execute('BIGAN')

    # выполняем операцию
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?,)', ('user1', 'user1@mail.com'))
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?,)', ('user2', 'user2@mail.com'))
    cursor.execute('COMMIT')

except:
    # отменяем транзакцию в случае ошибки
    cursor.execute('ROLLBACK')

connection.commit()
connection.close()


""" Автоматическое управление транзакциями с помощью контекстных менеджеров"""

# устанавливаем соединение с базой
with sqlite3.connect('my_data.db') as connection:
    cursor = connection.cursor()

    try:
        # начинаем транзакцию автоматически
        with connection:
            cursor.execute('INSERT INTO Users (username, email) VALUE (?, ?)', ('user3',
                                                                                    'user3@mail.com'))
            cursor.execute('INSERT INTO Users (username, email) VALUE (?, ?)', ('user3',
                                                                                    'user3@mail.com'))

    except:
        # ошибки будут приводить к автоматическому откату транзакций
        pass


""" ИСПОЛЬЗОВАНИЕ ПОДГОТОВЛЕННЫХ (prepared) ЗАПРОСОВ ПОЗВОЛЯЮТ МНОГОКРАТНО ИСПОЛЬЗОВАТЬ SQL - запросы с разными
параметрами:
"""

# устанавливаем соединение с базой данных
connection = sqlite3.connect('my_data.db')
cursor = connection.cursor()

# создаем подготовленный запрос
qwery = 'SELECT * FROM Users WHERE age > ?'
cursor.execute(qwery, (25,))
users = cursor.fetchall()

# выводим результат
for user in users:
    print(user)

# закрываем соединение
connection.close()


""" Представления(views) позволяют создавать виртуальные таблицы, которые являются результатом выполнения 
SQL - запроса. Это упрощает выполнение сложных запросов """

connection = sqlite3.connect('my_data.db')
cursor = connection.cursor()

# создаем представление для активных пользователей
cursor.execute('''
CREATE VIEW ActiveUsers AS 
SELECT id, username, email, age, is_active FROM Users WHERE is_active = 1''')

# выбираем активных пользователей
cursor.execute('SELECT * FROM ActiveUsers')
active_users = cursor.fetchall()

# выводим результат
for user in active_users:
    print(user)

connection.close()


""" Триггеры - это специальные хранимые процедуры, которые автоматически вызываются при изменении данных в таблице """

connection = sqlite3.connect('my_data.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NUT NULL,
age INTEGER,
create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Создаем триггер для обновления времени создания при вставке новой записи
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_created_at
AFTER INSERT ON Users
BEGIN
UPDATE Users SET created_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
''')

connection.commit()
connection.close()


""" Индексы позволяют ускорить выполнение запросов к базе данных: """

connection = sqlite3.connect('my_data.db')
cursor = connection.cursor()

# создаем индекс для столбца "username"
cursor.execute('CREATE INDEX idx_username ON Users (username)')

connection.commit()
connection.close()
