
# date: 2019.05.20
# author: bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/56219520/peewee-how-do-i-execute-raw-query-and-map-it-to-the-dictionary/56219996#56219996

import peewee

db = peewee.MySQLDatabase('my_database', user='my_user', password='my_password')

cursor = db.execute_sql('show table status from my_database')

all_tables = []

for row in cursor.fetchall():
    table = dict()
    for column, value in zip(cursor.description, row):
        print(column)
        column_name = column[0]
        print(column_name, '=', value)
        table[column_name] = value
    all_tables.append(table)

print(all_tables) 
