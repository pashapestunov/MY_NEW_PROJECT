import sqlite3


connection = sqlite3.connect('home_work_14.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
Name TEXT PRIMARY KEY,
Position TEXT NOT NULL,
Department TEXT NOT NULL,
Salary INTEGER
)
''')

some_people = {
    ('pasha', 'admin', 'kolasa', 1300),
    ('vlad', 'admin', 'kolasa', 1000),
    ('oleg', 'admin', 'kolasa', 1200),
    ('bugai', 'barmen', 'kolasa', 1100),
    ('sanya', 'barmen', 'kolasa', 500),
    ('renata', 'ofik', 'kolasa', 400),
}

try:
    cursor.executemany('INSERT INTO Employees (Name, Position, Department, Salary) '
                       'VALUES (?, ?, ?, ?)', some_people)
except sqlite3.IntegrityError as e:
    print(f'Error inserting data {e}')

cursor.execute('UPDATE Employees SET Position = ? WHERE Name = ?', ('dvornik', 'sanya'))
cursor.execute('UPDATE Employees SET Position = ? WHERE Name = ?', ('dvornik', 'bugai'))

cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')

some_people_with_new = {
    ('pasha', 'admin', 'kolasa', 1300, '02.03.2020'),
    ('vlad', 'admin', 'kolasa', 1000, '05.12.2022'),
    ('oleg', 'admin', 'kolasa', 1200, '06.09.2021'),
    ('bugai', 'dvornik', 'kolasa', 1100, '11.11.2023'),
    ('sanya', 'dvornik', 'kolasa', 500, '01.01.2024'),
    ('renata', 'ofik', 'kolasa', 400, '01.01.2024'),
}

cursor.executemany('INSERT OR REPLACE INTO Employees (Name, Position, Department, Salary, HireDate)'
                   'VALUES (?, ?, ?, ?, ?)', some_people_with_new)

cursor.execute('SELECT * FROM Employees')
print_new = cursor.fetchall()

for person in print_new:
    print(person)


def find_admin():
    cursor.execute('SELECT Name, Position FROM Employees WHERE Position = ?', ('admin',))
    only_admin = cursor.fetchall()
    for admin in only_admin:
        print(admin)


def find_salary():
    cursor.execute('SELECT Name, Salary FROM Employees WHERE Salary > ?', (1100,))
    only_rich = cursor.fetchall()
    for rich in only_rich:
        print(rich)


def find_date():
    cursor.execute('SELECT Name, HireDate FROM Employees WHERE HireDate = ?', ('01.01.2024',))
    only_new = cursor.fetchall()
    for news in only_new:
        print(news)


def find_avg():
    cursor.execute('SELECT AVG(Salary) FROM Employees')
    avg_sel = cursor.fetchall()[0]
    for avg in avg_sel:
        print(f'средняя зарплата в paul: {avg:.2f}')


find_admin()
find_salary()
find_date()
find_avg()

cursor.execute('DROP TABLE IF EXISTS Employees')

connection.commit()
connection.close()
