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
                   select * from person_table where id>='50' and id <='200' order by id;
                
                   """)
    


    with open('new_text.txt',mode= 'w', newline='') as file:
        for i in cursor.fetchall():
            file.writelines(str(i)+'\n')


except Exception as ex:
    print(ex)
 