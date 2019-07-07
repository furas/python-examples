
# date: 2019.05.20
# author: bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/56219520/peewee-how-do-i-execute-raw-query-and-map-it-to-the-dictionary/56219996#56219996

# DOESN"T WORK

import peewee

database = peewee.MySQLDatabase('information_schema', user='my_user', password='my_password')

class BaseModel(peewee.Model):
    class Meta:
        database = database
        
class Tables(BaseModel):
    class Meta:
        table_name = 'TABLES'
        #fields = {'Name':{'column_name': 'Name'}, 'Engine':{'column_name': 'Engine'}}
        primary_key = False

    Name = peewee.CharField(column_name="TABLE_NAME")
    Engine = peewee.CharField(column_name="ENGINE")
    
#results = Abc.raw('show table status from my_database')
results = Tables.select()

for row in results:
    print(row)
