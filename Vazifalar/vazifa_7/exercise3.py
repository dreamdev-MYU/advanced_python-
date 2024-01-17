import psycopg2
from config import *
import csv
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
 select child.first_name, ustoz.car_model from ustoz
right join child on ustoz.car_id = child.id order by first_name;
    """)

    with open('task3.csv',mode= 'w', newline='') as file:
        writer = csv.writer(file)
        for i in cursor.fetchall():
            writer.writerow(i)

except Exception as ex:
    print(ex)
finally:
    cursor.close()
    connection.close()