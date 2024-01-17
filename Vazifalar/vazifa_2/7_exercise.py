import psycopg2
from config import *

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
                  SELECT * FROM market where date between '2022-01-01' and '2022-12-31' order by first_name ;
                
                   """)
    with open('2022_text.txt',mode= 'w', newline='') as file:
        for i in cursor.fetchall():
            file.writelines(str(i)+'\n')


except Exception as ex:
    print(ex)
 