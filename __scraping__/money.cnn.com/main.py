#!/usr/bin/env python3 

# date: 2019.11.23
# https://stackoverflow.com/questions/59004270/i-want-to-display-first-word-from-1st-list-and-display-10-words-from-2nd-list-an

from bs4 import BeautifulSoup
import urllib.request

url = 'https://money.cnn.com/data/hotstocks/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')

allbody = soup.find('div', class_='cnnBody_Left wsodContent') 
names = allbody.find_all('h3')   #I am finding the header tags text
names = [x.text for x in names]
#print(names)

contents = allbody.find_all('table', class_='wsod_dataTable wsod_dataTableBigAlt')

tables = [] # keep three tables

for item in contents:
    data = [] # list for single table

    for tr in item.find_all('tr')[1:]: # find rows in table - skip row with headers `[1:]`
        a = tr.find('a')  # get only from first column
        a = a.text.strip()

        span = tr.find('span')  # get only from first column
        span = span.text.strip()

        data.append( (a, span) )

    tables.append(data)


for name, table in zip(names, tables):
    print('-', name)
    for a, span in table:
        print(a, span)
