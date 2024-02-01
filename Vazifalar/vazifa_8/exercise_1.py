from config import *
import psycopg2
try :
    connection = psycopg2.connect(
        dbname = dbname,
        port = port,
        host = host,
        password = password,
        user = user
    )

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    select name from students
    intersect
    select name from teachers
    """)
    for i in cursor.fetchall():
        print(i)
    
    
except Exception as ex:
    print(ex)
finally :
    cursor.close()
    
