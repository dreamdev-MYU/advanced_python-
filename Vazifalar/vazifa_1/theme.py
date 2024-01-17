import psycopg2
from  config import *
import csv
try:
    connection = psycopg2.connect(
        host = host,
        password = password,
        dbname = dbname,
        user = user,
        port = port
    )
    cursor = connection.cursor()
    cursor.execute("""
           select * from market where first_name ilike 'b%' and  date between '2017-01-01' and '2020-01-01'  """)
    with open("new.csv",mode= "w",newline="")as file:
        writer = csv.writer(file)
        for i in cursor.fetchall():
            writer.writerow(i)

except Exception as  ex:
  print(ex)
