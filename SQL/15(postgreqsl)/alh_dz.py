import psycopg2


try:
    connection = psycopg2.connect(dbname='postgres', user='pasha_user', password='db_pasha_pw',
                                  host='localhost', port='5433')
    print("Соединение с базой данных установлено успешно.")

    connection.autocommit = True   # автокоммит, не нужно писать после каждого действия (connection.commit())

    with connection.cursor() as cursor:   # c with нам не нужно писать кажный раз cursor.close()
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchall()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL);"""
    #     )
    #
    #     print('[INFO] Table created successfully')

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Oleg', 'barracuda'),
    #         ('Pasha', 'nub');"""
    #     )
    #     print("[INFO] Data was successfully inserted")
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
    #     )
    #
    #     oleg = cursor.fetchall()
    #     print(oleg)

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users"""
    #     )
    #
    #     print("[INFO] Table was deleted")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE people(
    #         id serial PRIMARY KEY,
    #         first_name varchar(50) NOT NULL,
    #         last_name varchar(50) NOT NULL);"""
    #     )
    #     print("[INFO] Table created successfully")
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE magazine(
    #         id serial PRIMARY KEY,
    #         title varchar(50),
    #         people_id INTEGER REFERENCES people(id),
    #         publication_year DATE);"""
    #     )
    #     print("[INFO] Table created successfully")
    #
    # with connection.cursor() as cursor:
    #   cursor.execute(
    #       """CREATE TABLE how_by(
    #       id serial PRIMARY KEY,
    #       book_id INTEGER REFERENCES magazine(id),
    #       quantity INTEGER);"""
    #     )
    #     print("[INFO] Table created successfully")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO people(first_name, last_name)
    #         VALUES ('pasha', 'pestunov'),
    #         ('tanya', 'pestunova'),
    #         ('dominika', 'osos');"""
    #     )
    #     print("[INFO] Datas inserted in table")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO magazine(title, people_id, publication_year)
    #         VALUES ('the_one', 1, '2024-01-01'),
    #         ('the_two', 2, '2022-01-01'),
    #         ('the_three', 1, '2023-12-12');"""
    #     )
    #     print("[INFO] Datas inserted in table")
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO how_by(book_id, quantity)
    #         VALUES (1, 33),
    #         (2, 44),
    #         (3, 55);"""
    #     )
    #     print("[INFO] Datas inserted in table")
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as people_name,
    #             people.last_name as people_l_name,
    #             magazine.title as magazine_title
    #         FROM
    #             magazine
    #         INNER JOIN
    #             people ON magazine.people_id = people.id;
    #         """)
    #     s = cursor.fetchall()
    #     for pep in s:
    #         print(pep)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as people_name,
    #             people.last_name as people_l_name,
    #             magazine.title as magazine_title
    #         FROM
    #             magazine
    #         RIGHT JOIN
    #             people ON magazine.people_id = people.id;
    #         """)
    #     s = cursor.fetchall()
    #     for pep in s:
    #         print(pep)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as people_name,
    #             people.last_name as people_l_name,
    #             magazine.title as magazine_title
    #         FROM
    #             people
    #         LEFT JOIN
    #             magazine ON people.id = magazine.people_id;
    #         """)
    #     s = cursor.fetchall()
    #     for pep in s:
    #         print(pep)

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as people_name,
    #             magazine.title as magazine_title,
    #             how_by.quantity as how_quantity
    #         FROM
    #             magazine
    #         INNER JOIN
    #             people ON magazine.people_id = people.id
    #         INNER JOIN
    #             how_by ON magazine.id = how_by.book_id;"""
    #     )
    #     s = cursor.fetchall()
    #     for pep in s:
    #         print(pep)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as people_name,
    #             magazine.title as magazine_title,
    #             how_by.quantity as how_quantity
    #         FROM
    #             people
    #         LEFT JOIN
    #             magazine ON people.id = magazine.people_id
    #         LEFT JOIN
    #             how_by ON magazine.id = how_by.book_id;"""
    #     )
    #     s = cursor.fetchall()
    #     for pep in s:
    #         print(pep)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as author_name,
    #             people.last_name as autor_last_name,
    #             SUM(how_by.quantity) as total_sold_books
    #         FROM
    #             magazine
    #         INNER JOIN
    #             people ON magazine.people_id = people.id
    #         INNER JOIN
    #             how_by ON magazine.id = how_by.book_id
    #         GROUP BY
    #             people.id, people.first_name, people.last_name
    #         ORDER BY
    #             total_sold_books DESC;"""
    #     )
    #     result = cursor.fetchall()
    #     for record in result:
    #         print(record)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as author_name,
    #             people.last_name as autor_last_name,
    #             COALESCE(SUM(how_by.quantity), 0) as total_sold_books
    #         FROM
    #             people
    #         LEFT JOIN
    #             magazine ON people.id = magazine.people_id
    #         LEFT JOIN
    #             how_by ON magazine.id = how_by.book_id
    #         GROUP BY
    #             people.id, people.first_name, people.last_name
    #         ORDER BY
    #             total_sold_books DESC;"""
    #     )
    #     result = cursor.fetchall()
    #     for record in result:
    #         print(record)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT
    #             people.first_name as author_name,
    #             people.last_name as author_last_name,
    #             author_sales.total_sold_books
    #         FROM
    #             people
    #         JOIN (
    #             SELECT
    #                 magazine.people_id,
    #                 SUM(how_by.quantity) AS total_sold_books
    #             FROM
    #                 magazine
    #             JOIN
    #                 how_by ON magazine.id = how_by.book_id
    #             GROUP BY
    #                 magazine.people_id
    #         ) AS author_sales ON people.id = author_sales.people_id
    #         ORDER BY
    #             author_sales.total_sold_books DESC
    #         LIMIT 1;
    #         """
    #     )
    #     result = cursor.fetchall()
    #     for rs in result:
    #         print(rs)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         SELECT
    #             magazine.title AS book_title,
    #             SUM(how_by.quantity) AS total_sold
    #         FROM
    #             magazine
    #         JOIN
    #             how_by ON magazine.id = how_by.book_id
    #         GROUP BY
    #             magazine.id, magazine.title
    #         HAVING
    #             SUM(how_by.quantity) > (
    #                 SELECT AVG(total_sales)
    #                 FROM (
    #                     SELECT SUM(how_by.quantity) AS total_sales
    #                     FROM how_by
    #                     JOIN magazine ON how_by.book_id = magazine.id
    #                     GROUP BY magazine.id
    #                 ) AS avg_sales_subquery
    #             )
    #         ORDER BY
    #             total_sold DESC;
    #         """
    #     )
    #     result = cursor.fetchall()
    #     for record in result:
    #         print(record)


except Exception as _ex:
    print(f"Не удалось подключиться к базе данных: {_ex}")
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection closed")
