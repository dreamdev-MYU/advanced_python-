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
           select * from market where date between '2023-01-01' and '2023-12-31' order by date desc;                   
                   """)
    

    with open('5_task.csv',mode= 'w', newline='') as file:
        writer = csv.writer(file)
        for i in cursor.fetchall():
            writer.writerow(i)
   

except Exception as ex:
    print(ex)
 