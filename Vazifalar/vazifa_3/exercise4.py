import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        host=host,
        password=password,
        port=port,
        user=user,
        dbname=dbname
    )
    connection.autocommit = True
    cursor = connection.cursor()

    cursor.execute("""
                   create table human(
                   id  int not null,
                   first_name varchar(50),
                   car_model varchar(125));
    """)



    try:
        new_file = open('task3.csv', mode='r', encoding='utf-8')
    except FileNotFoundError as ex:
        print(f"Error: {ex}")
        raise

    insert_query = "insert into human(id, first_name, car_model) values (%s,%s,%s);"

    for line in new_file:
        data = line.strip().split(',')
        cursor.execute(insert_query, (int(data[0]), data[1], data[2]))

except Exception as ex:
    print(ex)
finally:
    cursor.close()
    connection.close()








