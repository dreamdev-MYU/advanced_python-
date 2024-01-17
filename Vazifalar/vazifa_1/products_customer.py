import psycopg2
from config import * 
try:
      connection = psycopg2.connect(
            port = port,
            host = host,
            password = password,
            user = user,
            dbname = dbname 
      )
      connection.autocommit = True
      cursor = connection.cursor()
      cursor.execute("""
        create table customer(
                    id serial not null primary key,
                    name varchar(50) not null);
        
        create table prod_cust(
                     products_id int,
                     customer_id int,
                     primary key(products_id, customer_id),
                     foreign key (products_id) references products(id),
                     foreign key (customer_id) references customer(id)
        );         
            """)
      
except Exception as ex:
      print(ex)