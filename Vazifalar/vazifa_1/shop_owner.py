import psycopg2
from config import *
try :
    connection = psycopg2.connect(
        user = user,
        port = port,
        host = host,
        dbname = dbname,
        password = password
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    
    create table owner(
                   id serial not null primary key,
                   name varchar(50) not null,
                   shop_id int references shop(id) unique);
    insert into owner(name,shop_id) values('ALI',2),('Komil',3),('vali',1);

      """)
    
except Exception as ex:
    print(ex)