
# date: 2019.05.20
# author: bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/56219520/peewee-how-do-i-execute-raw-query-and-map-it-to-the-dictionary/56219996#56219996

import peewee

db = peewee.MySQLDatabase('my_database', user='my_user', password='my_password')

cursor = db.execute_sql('show table status from my_database')

column_names = [x[0] for x in cursor.description]
all_tables = [dict(zip(column_names, row)) for row in cursor.fetchall()]

print(all_tables) 



