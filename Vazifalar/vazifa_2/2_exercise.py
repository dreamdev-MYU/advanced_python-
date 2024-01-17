import psycopg2
from config import *
import csv
try:
    connection = psycopg2.connect(
        host = host,
        dbname = dbname,
        port = port,
        user = user,
        password = password
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(""" 
                   select * from person_table where id>='300' and id<='600' order by id desc;
                   
                   """)
    with open('new.csv',mode= 'w', newline='') as file:
        writer = csv.writer(file)
        for i in cursor.fetchall():
            writer.writerow(i)
            


except Exception as ex:
    print(ex)
 