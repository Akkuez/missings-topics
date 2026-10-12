import MySQLdb

try:

    connector = MySQLdb.connect(user='root',
                                password='password123',
                                host='localhost')

    print('*********** MySQLdb connected ***********\n')

    handler = connector.cursor()

    handler.execute('create database if not exists birds_db;')

    handler.execute('use birds_db;')

    # handler.execute('show databases;')

    # a = handler.fetchall()

    # for i in a:

    #     print(i)


    handler.execute('''create table if not exists birds(id int not null auto_increment unique primary key,
                                                        name varchar(50) not null,
                                                        colour varchar(20) not null,
                                                        type enum ('domestic','wild') not null);''')

    # handler.execute('''insert into birds(name,colour,type)  values ('Pigeon', 'Grey', 'domestic'),
    #                                                                 ('Hen', 'Brown', 'domestic'),
    #                                                                 ('Duck', 'White', 'domestic'),
    #                                                                 ('Turkey', 'Black', 'domestic'),
    #                                                                 ('Canary', 'Yellow', 'domestic'),
    #                                                                 ('Eagle', 'Brown', 'wild'),
    #                                                                 ('Peacock', 'Blue', 'wild'),
    #                                                                 ('Owl', 'Grey', 'wild'),
    #                                                                 ('Flamingo', 'Pink', 'wild'),
    #                                                                 ('Kingfisher', 'Blue', 'wild');''')

    # connector.commit()

    print('\n----------Display All Records----------\n')

    handler.execute('select * from birds;')

    display = handler.fetchall()

    for i in display:

        print(i)

    print('\n----------Display Wild Birds----------\n')

    handler.execute('''select * from birds where type = 'wild';''')

    wild = handler.fetchall()


    for i in wild:

        print(i)


    print('\n----------Display Count of all records----------\n')

    handler.execute('select count(name) from birds;')

    count = handler.fetchall()

    print(count)

    print('\n----------Update a record in id = 3----------\n')

    handler.execute('''update birds set colour = 'Yellow' where id = 3;''')

    handler.execute('select * from birds where id = 3;')

    a = handler.fetchall()

    print(a)

    print('\n----------delete a record in id 7----------\n')

    handler.execute('delete from birds where id = 7;')

    handler.execute('select * from birds where id = 7')

    a = handler.fetchall()

    print(a)



    


 


except MySQLdb.Error as e:

    print(e)

finally:

    if 'connector' in locals():

        connector.close()

        print('\n*********** MySQLdb disconnected ***********')