#!/usr/bin/env python3

# date: 2020.05.25
# https://stackoverflow.com/questions/62000520/extracting-html-data-using-python/

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.marketscreener.com/MICROSOFT-CORPORATION-4835/company/'

r = requests.get(url) #, headers={'user-agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content, 'html.parser')

all_tables = []

for table in soup.select("table table.nfvtTab"):
    table_rows = []
    for tr in table.select('tr'):
        row = []
        for td in tr.select('td'):
            #print(td)
            item = td.get_text(strip=True, separator=' ')
            #print(item)
            row.append(item)
        table_rows.append(row)
    all_tables.append(table_rows)

# add headers for nested columns

#Sales per Business     
all_tables[0][0].insert(2, '2018')
all_tables[0][0].insert(4, '2019')
all_tables[0][1].insert(0, '')
all_tables[0][1].insert(5, '')

# create one row with headers
headers = [f'{a} {b}'.strip() for a,b in zip(all_tables[0][0], all_tables[0][1])]
print('new:', headers)
all_tables[0][0] = headers  # set new headers in first row
del all_tables[0][1]        # remove second row

#Sales  per region
all_tables[1][0].insert(2, '2018')
all_tables[1][0].insert(4, '2019')
all_tables[1][1].insert(0, '')
all_tables[1][1].insert(5, '')

# create one row with headers
headers = [f'{a} {b}'.strip() for a,b in zip(all_tables[1][0], all_tables[1][1])]
print('new:', headers)
all_tables[1][0] = headers  # set new headers in first row
del all_tables[1][1]        # remove second row

#Equities
all_tables[3][0].insert(4, 'Free-Float %')
all_tables[3][0].insert(6, 'Company-owned shares %')

for number, table in enumerate(all_tables, 1):
    print('---', number, '---')
    for row in table:
        print(row)

for number, table in enumerate(all_tables, 1):
    with open(f'table{number}.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(table)

