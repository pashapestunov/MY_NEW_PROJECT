import psycopg2


try:
    connection = psycopg2.connect(dbname='postgres', user='pasha_user', password='db_pasha_pw',
                                  host='localhost', port='5433')
    print("Соединение с базой данных установлено успешно.")

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
        )

except Exception as _ex:
    print(f"Не удалось подключиться к базе данных: {_ex}")
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection closed")



