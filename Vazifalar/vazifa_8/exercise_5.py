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
    create table Employee (
    employee_id INT PRIMARY KEY,
    name VARCHAR(55),
    age INT);


    select count(*)
    FROM Employee
    WHERE age > 25;
    """)
    
    
    
except Exception as ex:
    print(ex)
finally :
    cursor.close()
    
