# pip  ---- preffered installer program (pip install packages)  

# to check installed packages on device

# pip list

# pip install package_name   # to install a module 

# pip install pillow  

# -----------------------------------------------------------------------------

# pip install mysqlclient  ---- to connect with mysql


import MySQLdb

try:

    connector=MySQLdb.connect(user='root',
                              
                              password='password123',

                              host='localhost')

    print('mysql connected')

    handler=connector.cursor()  

    handler.execute('create database if not exists wonders_db;')

    # handler.execute('show databases;') 

    # databases=handler.fetchall()  #[('wonders_db'),('colours_db')]

    # # print(databases)

    # # (('birds_db',), ('colour_db',), ('colours_db',), ('employee_db',), ('expense_db',), ('fruits_db',), ('information_schema',), ('movie_db',), ('mysql',), ('performance_schema',), ('student_db',), ('sys',), ('wonders_db',))
  
    # for database in databases:

    #     print(database)

    handler.execute('use wonders_db;')

    handler.execute('''create table  if not exists wonders (id int not null auto_increment primary key,
                                                            name varchar(50) not null,
                                                            country varchar(25) not null);
    #                                                         ''')

    
    
    # handler.execute('desc wonders;')

    # description=handler.fetchall()


    # for field in description:

    #     print (field)
    
    # handler.execute ('insert into wonders (name,country) values ("tajmahal","india");')  #dml  

    # connector.commit()


    # handler.execute('select * from wonders;')

    # table=handler.fetchall()

    # for tab in table:

    #     print(tab)

    # handler.execute('update wonders set name = "The Great Wall of china ",country ="China" where id = 1;')

    # connector.commit()

    '''handler.execute('delete from wonders where id = 2;')

    connector.commit()'''

    
    
except MySQLdb.Error as e:

    print(e)

finally:

    if 'connector ' in locals():

        connector.close()


# if 10 > 5:

#     a = 'yes'

# else:

#     b = 'no'

# print(locals())




# zero_division ,      TypeError ,                 ValueError

# 10 / 0              int + string            int(string)




