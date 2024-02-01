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
SELECT product_id, AVG(amount) AS average_amount
FROM sales
GROUP BY product_id;
    """)
    
    
    
except Exception as ex:
    print(ex)
finally :
    cursor.close()
    
