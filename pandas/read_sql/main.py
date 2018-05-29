#!/usr/bin/env python3

import pandas as pd
import pymysql

HOST     = input('host [localhost]: ') or 'localhost'
LOGIN    = input('login []: ')
PASSWORD = input('password []: ')
DATABASE = input('database [my_database]: ') or 'my_database'
TABLE    = input('table [my_table]: ') or 'my_table'

conn = pymysql.connect(HOST, LOGIN, PASSWORD, DATABASE)

query = 'SELECT * FROM {};'.format(TABLE)
df = pd.read_sql(query, conn)

print('len:', len(df))

print( df.head() )


