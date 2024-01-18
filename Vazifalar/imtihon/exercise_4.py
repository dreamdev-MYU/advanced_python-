import psycopg2
from config import *
import csv
try:
    connection = psycopg2.connect(
        host = host,
        port = port,
        dbname = dbname,
        user  = user,
        password = password
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    select * from persson where data_created between '2023-01-01' and '2023-06-30';
        select * from persson    ;

""")
    
    with open('person.csv', mode='w',encoding='utf-8') as file:
        writer=csv.writer(file)
        for i in cursor.fetchall():
            writer.writerow(i)

except Exception as ex:
    print(ex)

