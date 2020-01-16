#!/usr/bin/env python3

# date: 2020.01.16
# https://stackoverflow.com/questions/59762473/using-webdriver-in-beautifulsoup-for-web-scraping

import requests
from bs4 import BeautifulSoup as BS
import csv
#import webbrowser

MAX_PAGE_NUM = 5

#headers = {
#  "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0"
#}

with open('results.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Bussiness Name", "Phone Number", "Address"])

    for page_num in range(1, MAX_PAGE_NUM+1):
        #page_num = '{:03}'.format(page_num)
        url = 'https://www.yellowpages.my/listing/results.php?keyword=boutique&where=selangor&screen={}'.format(page_num)

        response = requests.get(url)#, headers=headers)
        soup = BS(response.text, 'lxml')
        #soup = BS(response.text, 'html.parser')

        #with open('temp.html', 'w') as fh:
        #    fh.write(response.text)
        #webbrowser.open('temp.html')
    
        #all_items = soup.find('div', {'id': 'content_listView'}).find_all('li')
        #print('len:', len(all_items))
        
        #for item in all_items:
        for item in soup.find('div', {'id': 'content_listView'}).find_all('li'):
            try:
                name = item.find('div', {'class': 'cbp-vm-companytext'}).text
            except Exception as ex:
                #print('ex:', ex)
                name = item.find('a', {'class': 'cbp-vm-image'}).find('img')['alt']
           
            phone = item.find('div', {'class': 'cbp-vm-cta'}).find('span', {'data-original-title': 'Phone'})['data-content']
            phone = phone[:-4].split(">")[-1].strip()
                
            address = item.find('div', {'class': 'cbp-vm-address'}).text
            address = address.split('\n')[-1].strip()

            print(name, '|', phone, '|', address)
            csv_writer.writerow([name, phone, address])

