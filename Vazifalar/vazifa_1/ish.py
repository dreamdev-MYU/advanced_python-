import psycopg2
from config import *
import csv 
try :

    connection = psycopg2.connect(
        host = host,
        dbname = dbname,
        password = password,
        user = user,
        port = port
    )

    cursor = connection.cursor()
    cursor.execute("""
    create table ish (
	id INT,
	first_name VARCHAR(50),
	company VARCHAR(50)
);
insert into ish (id, first_name, company) values (1, 'Enos', 'Geba');
insert into ish (id, first_name, company) values (2, 'Burnaby', 'Kayveo');
insert into ish (id, first_name, company) values (3, 'Ysabel', 'Camimbo');
insert into ish (id, first_name, company) values (4, 'Mel', 'Avamm');
insert into ish (id, first_name, company) values (5, 'Kristen', 'Aibox');
insert into ish (id, first_name, company) values (6, 'Joan', 'Kwideo');
insert into ish (id, first_name, company) values (7, 'Marlie', 'Youtags');
insert into ish (id, first_name, company) values (8, 'Boone', 'Youtags');
insert into ish (id, first_name, company) values (9, 'Valenka', 'Dabtype');
insert into ish (id, first_name, company) values (10, 'Shandeigh', 'Gigaclub');
insert into ish (id, first_name, company) values (11, 'Philippe', 'Fanoodle');
insert into ish (id, first_name, company) values (12, 'Torin', 'Yambee');
insert into ish (id, first_name, company) values (13, 'Lelah', 'Tazz');
insert into ish (id, first_name, company) values (14, 'Syd', 'Feedfire');
insert into ish (id, first_name, company) values (15, 'Meaghan', 'Rhyzio');
insert into ish (id, first_name, company) values (16, 'Janela', 'Thoughtstorm');
insert into ish (id, first_name, company) values (17, 'Mabel', 'Fanoodle');
insert into ish (id, first_name, company) values (18, 'Arlina', 'Tagfeed');
insert into ish (id, first_name, company) values (19, 'Algernon', 'Skyvu');
insert into ish (id, first_name, company) values (20, 'Kalvin', 'Tagfeed');
insert into ish (id, first_name, company) values (21, 'Jeremy', 'Oyoloo');
insert into ish (id, first_name, company) values (22, 'Ivette', 'Avavee');
insert into ish (id, first_name, company) values (23, 'Julianna', 'Layo');
insert into ish (id, first_name, company) values (24, 'Jada', 'Rhynoodle');
insert into ish (id, first_name, company) values (25, 'Brent', 'Ailane');
insert into ish (id, first_name, company) values (26, 'Edy', 'Skipstorm');
insert into ish (id, first_name, company) values (27, 'Frasier', 'Twitterbeat');
insert into ish (id, first_name, company) values (28, 'Fionna', 'Tagcat');
insert into ish (id, first_name, company) values (29, 'Carlee', 'Wordpedia');
insert into ish (id, first_name, company) values (30, 'Shara', 'Roomm');
insert into ish (id, first_name, company) values (31, 'Brendon', 'Skippad');
insert into ish (id, first_name, company) values (32, 'Roma', 'Youfeed');
insert into ish (id, first_name, company) values (33, 'Marchelle', 'Voomm');
insert into ish (id, first_name, company) values (34, 'Emery', 'Skaboo');
insert into ish (id, first_name, company) values (35, 'Sly', 'Brightbean');
insert into ish (id, first_name, company) values (36, 'Sadye', 'Babbleblab');
insert into ish (id, first_name, company) values (37, 'Trixi', 'Meembee');
insert into ish (id, first_name, company) values (38, 'Scarlet', 'Feednation');
insert into ish (id, first_name, company) values (39, 'Evey', 'Eabox');
insert into ish (id, first_name, company) values (40, 'Eartha', 'Aibox');
insert into ish (id, first_name, company) values (41, 'Kelli', 'Linklinks');
insert into ish (id, first_name, company) values (42, 'Alexandre', 'Dabshots');
insert into ish (id, first_name, company) values (43, 'Jordon', 'Dabfeed');
insert into ish (id, first_name, company) values (44, 'Aleda', 'Trudeo');
insert into ish (id, first_name, company) values (45, 'Crystal', 'DabZ');
insert into ish (id, first_name, company) values (46, 'Audrie', 'Twimbo');
insert into ish (id, first_name, company) values (47, 'Gan', 'Roodel');
insert into ish (id, first_name, company) values (48, 'Taddeusz', 'Rooxo');
insert into ish (id, first_name, company) values (49, 'Lurline', 'Abata');
insert into ish (id, first_name, company) values (50, 'Paquito', 'Zoombeat');
insert into ish (id, first_name, company) values (51, 'Clari', 'Skinder');
insert into ish (id, first_name, company) values (52, 'Barth', 'Oyope');
insert into ish (id, first_name, company) values (53, 'Judas', 'Zoombeat');
insert into ish (id, first_name, company) values (54, 'Ann', 'Tambee');
insert into ish (id, first_name, company) values (55, 'Monty', 'Rhyzio');
insert into ish (id, first_name, company) values (56, 'Lotty', 'Blognation');
insert into ish (id, first_name, company) values (57, 'Esme', 'Zoomcast');
insert into ish (id, first_name, company) values (58, 'Jessamine', 'Geba');
insert into ish (id, first_name, company) values (59, 'Cordell', 'Rhybox');
insert into ish (id, first_name, company) values (60, 'Rora', 'Linklinks');
insert into ish (id, first_name, company) values (61, 'Antin', 'Jabberstorm');
insert into ish (id, first_name, company) values (62, 'Aharon', 'Aimbu');
insert into ish (id, first_name, company) values (63, 'Caterina', 'Pixonyx');
insert into ish (id, first_name, company) values (64, 'Eada', 'Meemm');
insert into ish (id, first_name, company) values (65, 'Carmelia', 'InnoZ');
insert into ish (id, first_name, company) values (66, 'Townie', 'Oodoo');
insert into ish (id, first_name, company) values (67, 'Fredra', 'Skyba');
insert into ish (id, first_name, company) values (68, 'Pattie', 'Jaxbean');
insert into ish (id, first_name, company) values (69, 'Flemming', 'Flipstorm');
insert into ish (id, first_name, company) values (70, 'Lilli', 'Kamba');
insert into ish (id, first_name, company) values (71, 'Diandra', 'Oyonder');
insert into ish (id, first_name, company) values (72, 'Dennie', 'Yakidoo');
insert into ish (id, first_name, company) values (73, 'Boyce', 'Photobug');
insert into ish (id, first_name, company) values (74, 'Evonne', 'Twiyo');
insert into ish (id, first_name, company) values (75, 'Constantia', 'Viva');
insert into ish (id, first_name, company) values (76, 'Jaime', 'Gigazoom');
insert into ish (id, first_name, company) values (77, 'Raymund', 'Oodoo');
insert into ish (id, first_name, company) values (78, 'Shurlocke', 'Skipfire');
insert into ish (id, first_name, company) values (79, 'Standford', 'Tagtune');
insert into ish (id, first_name, company) values (80, 'Herrick', 'Shuffletag');
insert into ish (id, first_name, company) values (81, 'Salmon', 'Yacero');
insert into ish (id, first_name, company) values (82, 'Aridatha', 'Eamia');
insert into ish (id, first_name, company) values (83, 'Donavon', 'Twitterworks');
insert into ish (id, first_name, company) values (84, 'Sayre', 'Gabvine');
insert into ish (id, first_name, company) values (85, 'Tonye', 'Eidel');
insert into ish (id, first_name, company) values (86, 'Ruggiero', 'Edgewire');
insert into ish (id, first_name, company) values (87, 'Bary', 'Eimbee');
insert into ish (id, first_name, company) values (88, 'Arly', 'Photobug');
insert into ish (id, first_name, company) values (89, 'Corty', 'Bubblemix');
insert into ish (id, first_name, company) values (90, 'Cesare', 'Nlounge');
insert into ish (id, first_name, company) values (91, 'Kermit', 'Devbug');
insert into ish (id, first_name, company) values (92, 'Myrtice', 'Jayo');
insert into ish (id, first_name, company) values (93, 'Sophronia', 'Jabberbean');
insert into ish (id, first_name, company) values (94, 'Tarra', 'Browsecat');
insert into ish (id, first_name, company) values (95, 'Tiffany', 'Thoughtbridge');
insert into ish (id, first_name, company) values (96, 'Ronna', 'Wordify');
insert into ish (id, first_name, company) values (97, 'Cullin', 'Chatterbridge');
insert into ish (id, first_name, company) values (98, 'Jacinta', 'Photojam');
insert into ish (id, first_name, company) values (99, 'Laura', 'Minyx');
    
                   select * from ish;
    """)

    with open('ish.csv',mode= "w",newline="")as file:
            writer = csv.writer(file)
            count = 0
            for i in cursor.fetchall():
                count+=1
                if count<=50:
                  writer.writerow(i)

except Exception as ex:
 print(ex)
