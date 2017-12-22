#!/usr/bin/env python3

#
# attribute "rel" returns as list 
# see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#multi-valued-attributes
#
# https://stackoverflow.com/a/47940166/1832058
#

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

params = {
    'SchoolType': '',
    'Dist1': '',
    'Sch1': '',
    'SearchString': '',
}

r = requests.post('http://www.registration.pseb.ac.in/School/Schoollist', headers=headers, data=params)

soup = BeautifulSoup(r.text, 'html.parser')

all_a = soup.find_all('a', {'class':'tip'})

for items in all_a:
    print('text:', item.text)
    print(' rel:', item['rel'])
    print(' rel:', ' '.join(item['rel']))
    print('-----')
