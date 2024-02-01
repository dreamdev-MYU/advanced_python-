import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        host=host,
        dbname=dbname,
        port=port,
        user=user,
        password=password
    )
    connection.autocommit = True
    cursor = connection.cursor()

    cursor.execute(""" 
        CREATE TABLE human(
            id int PRIMARY KEY NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            email VARCHAR(65) NOT NULL
        );
    """)

    new_file = open('new.csv', mode="r", encoding="utf-8")
    
    insert_query = "INSERT INTO human(id, first_name, email)  VALUES (%s, %s, %s);"

    for line in new_file:

        data = line.strip().split(',')
        cursor.execute(insert_query, (data[0], data[1], data[2]))

except Exception as ex:
    print(ex)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()