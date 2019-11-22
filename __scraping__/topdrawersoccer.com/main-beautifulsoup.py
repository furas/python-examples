#!/usr/bin/env python3

"""
date: 2019.10.29
link:  
"""

import bs4 as bs
import urllib.request
import csv

max_page_num = 15

url = "https://www.topdrawersoccer.com/search/?query=&divisionId=&genderId=m&graduationYear=2020&positionId=0&playerRating=&stateId=All&area=commitments&pageNo={}"

headers = ["Name", "Gender", "State", "Position", "Grad", "Club/HS", "Rating", "Commitment"]


fh = open('result.csv', "w", newline='')
csv_writer = csv.writer(fh)

csv_writer.writerow(headers)

for i in range(max_page_num):
    print('page:', i)

    html = urllib.request.urlopen(url.format(i)).read()    

    soup = bs.BeautifulSoup(html, 'lxml')
    
    table = soup.find('table')
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        #row = [i.text.strip() for i in td] # strip to remove spaces and '\n'
        row = [i.get_text(strip=True) for i in td] # strip to remove spaces and '\n'
    
        if row: # check if row is not empty
            #print(row)
            csv_writer.writerow(row)
        
fh.close()        
