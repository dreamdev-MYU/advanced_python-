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
                   id serial not null,
                   first_name varchar(50),
                   car_model varchar(125));
    """)
    new_file = open('task3.csv',mode='r',newline='')
    for line in new_file:
        insert_query = "inser into human"
    



except Exception as ex:
    print(ex)
finally:
    cursor.close()
    connection.close()







