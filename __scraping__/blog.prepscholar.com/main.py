#!/usr/bin/env python3

# date: 2020.02.26
# https://stackoverflow.com/questions/60407196/creating-csv-spreadsheets-from-web-tables-acquired-through-beautifulsoup

# with pandas 

import pandas as pd

all_tables = pd.read_html('https://blog.prepscholar.com/act-to-sat-conversion')
all_tables[0].to_csv("output1.csv")
all_tables[1].to_csv("output2.csv") 

# with BeautifulSoup it would need more work.

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://blog.prepscholar.com/act-to-sat-conversion'

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

table = soup.find_all('table')[1]

fh = open('output.csv', 'w')
cvs_writer = csv.writer(fh)

all_data = []
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all(['td','th'])
    row_data = []
    for cell in cells:
        row_data.append(cell.get_text())
    all_data.append(row_data)
    cvs_writer.writerow(row_data)

print(all_data)
fh.close()
