#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import csv

filename = "output.csv"

f = open(filename, 'w', newline="", encoding='utf-8')

csvwriter = csv.writer(f)

csvwriter.writerow( ["Date", "Location", "Title", "Price"] )

offset = 0

while True:
    print('offset:', offset)

    url = "https://portland.craigslist.org/search/sss?query=xbox&sort=date&s={}".format(offset)
        
    response = requests.get(url)
    if response.status_code != 200:
        print('END: request status:', response.status)
        break
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = soup.select('.result-info')
    if not data:
        print('END: no data:')
        break
    
    for container in data:
        date = container.select('.result-date')[0].text

        try:
            location = container.select('.result-hood')[0].text
        except:
            try:
                location = container.select('.nearby')[0].text 
            except:
                location = 'NULL'
        #location = location.replace(","," ") # don't need it with `csvwriter`
        
        title = container.select('.result-title')[0].text

        try:
            price = container.select('.result-price')[0].text
        except:
            price = "NULL"
        #title.replace(",", " ") # don't need it with `csvwriter`
        
        print(date, location, title, price)
        
        csvwriter.writerow( [date, location, title, price] )

    offset += 120

f.close()
