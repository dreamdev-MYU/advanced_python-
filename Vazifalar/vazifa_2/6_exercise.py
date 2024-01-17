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
           select * from market  order by date  desc limit(5)                    
     """)
    

   

except Exception as ex:
    print(ex)
 