import MySQLdb

data = []

class APIView:

    connector : None
    handler : None

    def __init__(self):                 #connect MySQLdb & create database and table

        self.connector = MySQLdb.connect(user='root',password='password123',host='localhost')

        self.handler = self.connector.cursor()

        self.handler.execute('create database if not exists colours_db;')

        self.handler.execute('use colours_db;')

        self.handler.execute('''create table if not exists colours (id int not null auto_increment unique primary key,
                                                        name varchar(20) not null,
                                                        status enum ('primary','secondary') not null,
                                                        hex_code varchar(15) not null );''')

    def close_db(self):         #close MySQLdb

        self.connector.close()


class ColoursListCreateView(APIView):   #no need for constructor

    def get(self,request,*args,**kwargs):   #display table records

        self.handler.execute('select * from colours;')

        colours = self.handler.fetchall()

        for id,name,status,hex_code in colours:

            dictionary = {'id':id,'name':name,'status':status,'hex_code':hex_code}

            data.append(dictionary)

        return data

    def post(self,request,*args,**kwargs):   # insert into table

        data = {'name':'red','status':'Primary','hex_code' : '#ff0000'}

        self.handler.execute(f'insert into colours (name,status,hex_code) values ("{data["name"]}","{data["status"]}","{data["hex_code"]}");')  

        self.connector.commit()

        data = {'msg':'colour added successfully'}

        return data



# [
#     {'id':1,'name':'red','status':'Primary','hexcode' : '#ff0000'}
#     {'id':2,'name':'green','status':'Primary','hexcode' : '#00ff00'}
    
# ]

class ColourRetriveUpdateDestroyView(APIView):    # retrive update destroy

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        self.handler.execute(f'select * from colours where id = {id};')

        id,name,status,hex_code = self.handler.fetchone()

        data = {'id':id,'name':name,'status':status,'hex_code':hex_code}

        return data

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')

        data = {'name':'Blue','hex_code':'#0000ff'}

        for key in data:

            self.handler.execute(f'update colours set {key}="{data[key]}" where id={id};')

            self.connector.commit()

        data = {'msg':'colour updated successfully'}

        return data

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        self.handler.execute(f'delete from colours where id = {id};')

        self.connector.commit

        data = {'msg':'colour deleted successfully'}

        return data





# list_create = ColoursListCreateView()

# list_create.post(request=None)   # insert into table

# print(list_create.get(request=None))      #display table records

# list_create.close_db()

retrive_update_destroy = ColourRetriveUpdateDestroyView()

# print(retrive_update_destroy.get(request=None,id=1))

# print(retrive_update_destroy.patch(request=None,id=1))

print(retrive_update_destroy.delete(request=None,id=1))


retrive_update_destroy.close_db()