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
               create table market (
	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	date DATE
);
insert into market (id, first_name, last_name, date) values (1, 'Sabine', 'Griswaite', '2017-08-22');
insert into market (id, first_name, last_name, date) values (2, 'Cairistiona', 'Jeans', '2011-05-13');
insert into market (id, first_name, last_name, date) values (3, 'Elena', 'Marlon', '2022-07-02');
insert into market (id, first_name, last_name, date) values (4, 'Hyacintha', 'Ogger', '2013-11-28');
insert into market (id, first_name, last_name, date) values (5, 'Arnie', 'Elkins', '2016-02-05');
insert into market (id, first_name, last_name, date) values (6, 'Lacy', 'Tewkesberry', '2023-05-14');
insert into market (id, first_name, last_name, date) values (7, 'Tobit', 'Head', '2017-07-22');
insert into market (id, first_name, last_name, date) values (8, 'Ag', 'Coggell', '2023-08-12');
insert into market (id, first_name, last_name, date) values (9, 'Lucais', 'Kenefick', '2019-06-03');
insert into market (id, first_name, last_name, date) values (10, 'Eddy', 'Moth', '2011-12-30');
insert into market (id, first_name, last_name, date) values (11, 'Ase', 'Espy', '2022-11-30');
insert into market (id, first_name, last_name, date) values (12, 'Gaston', 'Jaffrey', '2011-09-04');
insert into market (id, first_name, last_name, date) values (13, 'Dorolisa', 'Sacaze', '2011-02-01');
insert into market (id, first_name, last_name, date) values (14, 'Gennifer', 'Walthew', '2012-11-02');
insert into market (id, first_name, last_name, date) values (15, 'Hagan', 'Plowright', '2018-12-11');
insert into market (id, first_name, last_name, date) values (16, 'Marcela', 'Pauer', '2020-10-22');
insert into market (id, first_name, last_name, date) values (17, 'Svend', 'Lace', '2018-06-26');
insert into market (id, first_name, last_name, date) values (18, 'Victoria', 'Abele', '2012-06-28');
insert into market (id, first_name, last_name, date) values (19, 'Min', 'Stonnell', '2015-11-07');
insert into market (id, first_name, last_name, date) values (20, 'Auberon', 'Cromer', '2019-01-21');
insert into market (id, first_name, last_name, date) values (21, 'Dmitri', 'Maghull', '2015-06-15');
insert into market (id, first_name, last_name, date) values (22, 'Reamonn', 'Garrud', '2012-01-02');
insert into market (id, first_name, last_name, date) values (23, 'Arte', 'Weben', '2019-04-11');
insert into market (id, first_name, last_name, date) values (24, 'Aldo', 'Melmar', '2019-11-27');
insert into market (id, first_name, last_name, date) values (25, 'Kakalina', 'Jeroch', '2020-09-11');
insert into market (id, first_name, last_name, date) values (26, 'Fiona', 'Sprowle', '2014-08-25');
insert into market (id, first_name, last_name, date) values (27, 'Gare', 'Mattessen', '2019-02-20');
insert into market (id, first_name, last_name, date) values (28, 'Claudie', 'Newtown', '2020-09-22');
insert into market (id, first_name, last_name, date) values (29, 'Marne', 'Barosch', '2019-03-27');
insert into market (id, first_name, last_name, date) values (30, 'Gwynne', 'Penas', '2023-12-11');
insert into market (id, first_name, last_name, date) values (31, 'Saloma', 'Nuccii', '2022-06-11');
insert into market (id, first_name, last_name, date) values (32, 'Adena', 'Eble', '2016-05-29');
insert into market (id, first_name, last_name, date) values (33, 'Laurette', 'Cavil', '2019-08-24');
insert into market (id, first_name, last_name, date) values (34, 'Andrea', 'Cordeix', '2015-05-03');
insert into market (id, first_name, last_name, date) values (35, 'Ilyse', 'Ryves', '2011-08-21');
insert into market (id, first_name, last_name, date) values (36, 'Pennie', 'Robertet', '2018-06-24');
insert into market (id, first_name, last_name, date) values (37, 'Leia', 'Simoncelli', '2019-05-01');
insert into market (id, first_name, last_name, date) values (38, 'Amerigo', 'Heed', '2017-03-19');
insert into market (id, first_name, last_name, date) values (39, 'Barry', 'Radband', '2018-05-07');
insert into market (id, first_name, last_name, date) values (40, 'Lottie', 'McMychem', '2020-02-19');
insert into market (id, first_name, last_name, date) values (41, 'Ardath', 'Reddihough', '2011-12-15');
insert into market (id, first_name, last_name, date) values (42, 'Augustina', 'Cattemull', '2019-02-02');
insert into market (id, first_name, last_name, date) values (43, 'Web', 'Krojn', '2012-10-03');
insert into market (id, first_name, last_name, date) values (44, 'Ricky', 'Vaughn', '2014-12-11');
insert into market (id, first_name, last_name, date) values (45, 'Rea', 'Rawood', '2021-09-02');
insert into market (id, first_name, last_name, date) values (46, 'Harv', 'Stubs', '2022-10-15');
insert into market (id, first_name, last_name, date) values (47, 'Parrnell', 'Champness', '2018-05-03');
insert into market (id, first_name, last_name, date) values (48, 'Keane', 'Cruise', '2019-04-30');
insert into market (id, first_name, last_name, date) values (49, 'Connie', 'Milner', '2015-01-12');
insert into market (id, first_name, last_name, date) values (50, 'Morey', 'Ruseworth', '2023-09-27');
insert into market (id, first_name, last_name, date) values (51, 'Drusilla', 'McCowen', '2014-03-28');
insert into market (id, first_name, last_name, date) values (52, 'Alanna', 'Banger', '2023-03-17');
insert into market (id, first_name, last_name, date) values (53, 'Tessie', 'Fitton', '2019-05-03');
insert into market (id, first_name, last_name, date) values (54, 'Bert', 'Roofe', '2014-10-24');
insert into market (id, first_name, last_name, date) values (55, 'Gloriana', 'Cantor', '2012-10-02');
insert into market (id, first_name, last_name, date) values (56, 'Rikki', 'Baudts', '2011-10-30');
insert into market (id, first_name, last_name, date) values (57, 'Kelci', 'Wookey', '2018-06-26');
insert into market (id, first_name, last_name, date) values (58, 'Bastien', 'Albers', '2016-01-08');
insert into market (id, first_name, last_name, date) values (59, 'Salmon', 'Lande', '2021-04-24');
insert into market (id, first_name, last_name, date) values (60, 'Kim', 'Marrion', '2012-11-26');
insert into market (id, first_name, last_name, date) values (61, 'Blakeley', 'Hould', '2023-04-08');
insert into market (id, first_name, last_name, date) values (62, 'Cathee', 'Squirrel', '2016-09-22');
insert into market (id, first_name, last_name, date) values (63, 'Kip', 'Rossin', '2017-03-12');
insert into market (id, first_name, last_name, date) values (64, 'Rahel', 'Baud', '2019-07-30');
insert into market (id, first_name, last_name, date) values (65, 'Rebecca', 'Anderl', '2015-09-20');
insert into market (id, first_name, last_name, date) values (66, 'Fanni', 'Holgan', '2013-05-08');
insert into market (id, first_name, last_name, date) values (67, 'Artair', 'Dombrell', '2016-11-12');
insert into market (id, first_name, last_name, date) values (68, 'Flemming', 'Rahl', '2011-12-23');
insert into market (id, first_name, last_name, date) values (69, 'Ruprecht', 'Peschka', '2016-10-31');
insert into market (id, first_name, last_name, date) values (70, 'Porter', 'Aishford', '2013-01-07');
insert into market (id, first_name, last_name, date) values (71, 'Brigham', 'Duthie', '2019-05-07');
insert into market (id, first_name, last_name, date) values (72, 'Freeland', 'Sisse', '2012-05-02');
insert into market (id, first_name, last_name, date) values (73, 'Gerianne', 'Greenham', '2023-07-11');
insert into market (id, first_name, last_name, date) values (74, 'Stephani', 'Maling', '2021-08-24');
insert into market (id, first_name, last_name, date) values (75, 'Mada', 'Gladebeck', '2016-03-12');
insert into market (id, first_name, last_name, date) values (76, 'Osbert', 'Casterot', '2020-11-16');
insert into market (id, first_name, last_name, date) values (77, 'Willette', 'Mayward', '2017-06-16');
insert into market (id, first_name, last_name, date) values (78, 'Katti', 'Sudell', '2014-12-17');
insert into market (id, first_name, last_name, date) values (79, 'Rebbecca', 'Seabourne', '2022-01-24');
insert into market (id, first_name, last_name, date) values (80, 'Jeanne', 'Samson', '2019-04-03');
insert into market (id, first_name, last_name, date) values (81, 'Gerianna', 'Pibworth', '2019-08-20');
insert into market (id, first_name, last_name, date) values (82, 'Cosme', 'Whymark', '2013-06-16');
insert into market (id, first_name, last_name, date) values (83, 'Datha', 'Florez', '2018-12-24');
insert into market (id, first_name, last_name, date) values (84, 'Andre', 'Lemme', '2020-08-21');
insert into market (id, first_name, last_name, date) values (85, 'Sebastiano', 'Huggin', '2023-02-28');
insert into market (id, first_name, last_name, date) values (86, 'Rodolphe', 'Cadman', '2019-04-21');
insert into market (id, first_name, last_name, date) values (87, 'Payton', 'Roscoe', '2014-03-20');
insert into market (id, first_name, last_name, date) values (88, 'Roderigo', 'Fiorentino', '2018-04-14');
insert into market (id, first_name, last_name, date) values (89, 'Claudelle', 'Kleehuhler', '2011-11-03');
insert into market (id, first_name, last_name, date) values (90, 'Dyanne', 'Libri', '2015-09-28');
insert into market (id, first_name, last_name, date) values (91, 'Clare', 'Janoch', '2014-06-11');
insert into market (id, first_name, last_name, date) values (92, 'Dulciana', 'Melloy', '2014-12-31');
insert into market (id, first_name, last_name, date) values (93, 'Skipper', 'Tuffell', '2013-03-04');
insert into market (id, first_name, last_name, date) values (94, 'Shanda', 'Harteley', '2020-10-28');
insert into market (id, first_name, last_name, date) values (95, 'Lauree', 'Woolpert', '2013-10-14');
insert into market (id, first_name, last_name, date) values (96, 'Gaye', 'Caslett', '2012-09-11');
insert into market (id, first_name, last_name, date) values (97, 'Lane', 'Payle', '2023-01-28');
insert into market (id, first_name, last_name, date) values (98, 'Tess', 'Mecco', '2015-01-06');
insert into market (id, first_name, last_name, date) values (99, 'Patin', 'Freegard', '2011-03-28');
insert into market (id, first_name, last_name, date) values (100, 'Dur', 'Bacup', '2014-09-23');
insert into market (id, first_name, last_name, date) values (101, 'Charlotta', 'Colrein', '2019-09-05');
insert into market (id, first_name, last_name, date) values (102, 'Vida', 'Bosche', '2023-08-22');
insert into market (id, first_name, last_name, date) values (103, 'Joelynn', 'Pre', '2022-06-30');
insert into market (id, first_name, last_name, date) values (104, 'Jared', 'Wilkennson', '2013-10-31');
insert into market (id, first_name, last_name, date) values (105, 'Kath', 'Kwiek', '2012-08-30');
insert into market (id, first_name, last_name, date) values (106, 'Anabelle', 'Jentin', '2022-08-19');
insert into market (id, first_name, last_name, date) values (107, 'Rock', 'Lohmeyer', '2011-11-20');
insert into market (id, first_name, last_name, date) values (108, 'Lacy', 'Danielli', '2015-03-20');
insert into market (id, first_name, last_name, date) values (109, 'Mickie', 'Parkman', '2013-04-20');
insert into market (id, first_name, last_name, date) values (110, 'Francesco', 'Quartermain', '2012-07-28');
insert into market (id, first_name, last_name, date) values (111, 'Gisela', 'Peckitt', '2015-07-26');
insert into market (id, first_name, last_name, date) values (112, 'Meryl', 'Garforth', '2021-04-26');
insert into market (id, first_name, last_name, date) values (113, 'Jenda', 'Rozet', '2020-05-03');
insert into market (id, first_name, last_name, date) values (114, 'Aindrea', 'O''Kuddyhy', '2015-06-17');
insert into market (id, first_name, last_name, date) values (115, 'Roi', 'Janek', '2019-07-19');
insert into market (id, first_name, last_name, date) values (116, 'Alanah', 'Hanbury-Brown', '2012-03-18');
insert into market (id, first_name, last_name, date) values (117, 'Courtney', 'McCart', '2016-09-19');
 
     select * from market;              
                   """)
    with open('ted.csv',mode= "w",encoding="utf-8")as file:
        writer = csv.writer(file)
        for i in cursor.fetchall():
            writer.writerow(i)

except Exception as ex:
    print(ex)

    