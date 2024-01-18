import psycopg2
from config import *

try:
    connection = psycopg2.connect( 
        host = host,
        port = port,
        dbname = dbname,
        user = user,
        password = password
    )
    
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    create table Category(
                   id serial not null primary key, 
                   name varchar(50) not null);
    
                   insert into category(name)
                   values('mevalar'),('sabzavotlar'),('ichimliklar');
                   
    create table Products(
                   id bigint not null, 
                   name varchar(50) not null,
                   expire date not null,
                   name_id int references Category(id) );

    insert into Products(id,name,expire, name_id)
    values(3, 'olma', '2020-09-12',1),(1, 'sabzi', '2023-09-12',2),(2, 'FANTA', '2024-03-02',3),(4, 'nok', '2020-09-12',1);               
                   """)

except Exception as ex:
    print(ex)