


# import psycopg2
# from config import *
# try:
#     connection = psycopg2.connect(
#         host = host,
#         user = user,
#         password = password,
#         port = port,
#         dbname = dbname

#     )
#     connection.autocommit = True
#     cursor = connection.cursor()
#     cursor.execute("""
#     create table  online_shop(
#         id serial primary key,
#         product_name varchar(50),
#         price decimal);

#     insert into online_shop(product_name,price) 
#     values ('olma',3000.00),('nok',6543.90),('apelsin',8734.34),('kiwi',9843.90);
                        

# """)
    

