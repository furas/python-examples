#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import unicodedata
from pandas import DataFrame

page = requests.get("http://properties.kimcorealty.com/property/output/find/search4/view:list/")
soup = BeautifulSoup(page.content, 'html.parser')

table_data = []

# all rows in table except first ([1:]) - headers
rows = soup.select('table tr')[1:]
for row in rows: 

    # link in first column (td[0] 
    link = row.select('td')[0].find('a')['href']
    print(link)
    
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    divs = soup.find_all('div', {'id':['units_box_1', 'units_box_2', 'units_box_3']})
    for div in divs:
        anchors = div.find_all('a')
        for anchor in anchors:
            lis = anchor.find_all('li')
            table_data.append([unicodedata.normalize("NFKD",lis[0].text).strip(), lis[1].text, lis[2].text.strip()])

    print('table_data size:', len(table_data))            
    
headers = ['Number', 'Tenant', 'Square Footage']
df = DataFrame(table_data, columns=headers)
print(df)
