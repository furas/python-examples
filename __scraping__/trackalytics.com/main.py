#!/usr/bin/env python3.7

# date: 2020.05.06
# ???

import requests
from bs4 import BeautifulSoup
import csv

# --- functions ---

def get_page(number):
    url = 'https://www.trackalytics.com/the-most-followed-instagram-profiles/page/{}/'.format(number)
    headers= {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    return soup

def get_data(soup):
    table = soup.find('table')

    results = []
    
    for row in table.find_all('tr'):
        all_cells = row.find_all('td')

        # skip empty rows
        if all_cells:
            a = all_cells[0].find('span').text.strip()
    
            b = all_cells[1].text.strip()
    
            c = all_cells[2].text.strip().split('\n')
            c = [clean(item) for item in c]
    
            d = all_cells[3].text.strip().split('\n')
            d = [clean(item) for item in d]
    
            e = all_cells[3].text.strip().split('\n')
            e = [clean(item) for item in e]
    
            f = all_cells[3].text.strip().split('\n')
            f = [clean(item) for item in f]

            results.append([a,b,c[0],c[1],d[0],d[1],e[0],e[1],f[0],f[1]])

    return results
                
def clean(text):
    return text.strip().replace(' ', '').replace(',', '').replace('(', '').replace(')', '')

def write_data(data):

    with open ("instagram.txt", 'w') as writer:
        cvs_writer = csv.writer(writer)
        
        # write header
        cvs_writer.writerow([
            'Rank',
            'Profile',
            'Total Followers',
            'Total Followers today',
            'Total Following',
            'Total Following today',
            'Total Posts',
            'Total Posts today',
            'Total Influence',
            'Total Influence today'
        ])
        
        cvs_writer.writerows(data)
                
# --- main ---

all_data = []

for number in range(1, 10):
    print('page:', number)
    soup = get_page(number)
    data = get_data(soup)
    all_data.extend(data)

write_data(all_data)

