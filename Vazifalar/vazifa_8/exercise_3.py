import psycopg2
from config import *
try :
    connection = psycopg2.connect(
        dbname = dbname,
        port = port,
        user = user,
        password = password,
        host = host
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    select name from students
    union 
    select name from teachers;

    """)
    for i in cursor.fetchall():
        print(i)

except Exception as ex:
    print(ex)

finally :
    cursor.close()
    connection.close()