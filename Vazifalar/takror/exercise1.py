from config import *
import csv
import psycopg2
try:
    connection = psycopg2.connect(
        port = port,
        dbname = dbname,
        host = host,
        password = password,
        user = user        
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    select name ,age from qariyalar where age between 60 and 70;      
  
    select * from qariyalar;
""")
    with open ('new.csv',mode='w',encoding='utf-8',newline='') as file:
        writer =csv.writer(file)
        for i in file:
         cursor.fetchall()
         writer.writerow(i)

except Exception as ex:
   print(ex)
    
