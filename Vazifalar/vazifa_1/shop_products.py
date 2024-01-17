import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        host = host,
        password = password,
        user = user,
        dbname = dbname,
        port = port
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""
    create table shop(
                   id serial not null primary key,
                   name varchar(50) not null
    );
    
    create table shop_products(
                   shop_id int,
                   products_id int,

                   primary key(shop_id, products_id),
                   foreign key (shop_id) references shop(id),
                   foreign key (products_id) references products(id)
    );
    """)
    
except Exception as ex:
    print(ex)
