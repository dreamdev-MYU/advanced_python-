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
        SELECT ustoz.first_name, child.car_model 
        FROM ustoz
        JOIN child ON ustoz.car_id = child.id
        ; 
    """)

    with open('task1.txt', mode='w', newline='') as file:
        writer = file
        for row in cursor.fetchall():
            writer.writelines(str(row) + '\n')

except Exception as ex:
    print(ex)