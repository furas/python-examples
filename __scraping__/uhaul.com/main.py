#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47879161/1832058
#

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

urls = [
    'https://www.uhaul.com/Locations/Self-Storage-near-Charlotte-NC-28206/780052/',
    'https://www.uhaul.com/Locations/Self-Storage-near-Charlotte-NC-28212/780063/'
]

filename = 'u_haul.csv'

f = open(filename, 'a+') # a+ will create file
csv_writer = csv.writer(f) # use csv module because some data may have comma or enter.

headers = ['title', 'unit_size', 'unit_type', 'online_price', 'street_address']
csv_writer.writerow(headers)

for my_url in urls:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')


    street_address = page_soup.find("div", {"class": "address"}).text

    street_address = ' '.join(street_address.split())
    print('street_address>', street_address, '<')
    print('---------------------------------------------------')

    #store_city = page_soup.find("span", {"": ""}).text
    #store_postalcode = page_soup.find("span", {"": ""}).text     

    containers = page_soup.find('div', {'id': 'roomTypes'}).findAll("div", {"class": "row"}) # <-- changed 

    for container in containers:
        title_container = container.find("div", {"class": "medium-4 medium-offset-2 small-7 columns"})
        unit_size = container.find("h4") # <-- changed 
        unit_type = container.find("p", {"class": "collapse"})
        online_price = container.find("strong", {"class": "text-large "}) # <-- changed 

        if title_container: # some rows doesn't have data 
            title = ' '.join(title_container.text.split())
            size = ' '.join(unit_size.text.split())
            unit = ' '.join(unit_type.text.split())
            price = online_price.text.strip()

            print('title>', title, '<')
            print('size>', size, '<')
            print('unit>', unit, '<')
            print('price>', price, '<')
            print('-----')

            csv_writer.writerow([title, size, unit, price, street_address])

f.close()

'''
Result:

street_address> 1224 N Tryon St Charlotte, NC 28206 <
---------------------------------------------------
title> 5' x 8' x 10' Drive Up 1st Floor Outside Level No Climate Miscellaneous Storage (up to 2 rooms) <
size> 5' x 8' x 10' <
unit> Drive Up 1st Floor Outside Level No Climate Miscellaneous Storage (up to 2 rooms) <
price> $74.95 <
-----
title> 4' x 12' x 10' Interior 1st Floor Street Level No Climate 1-2 Bedroom Home (up to 1,200 sq. ft.) <
size> 4' x 12' x 10' <
unit> Interior 1st Floor Street Level No Climate 1-2 Bedroom Home (up to 1,200 sq. ft.) <
price> $79.95 <
-----
title> 5' x 10' x 10' Interior 1st Floor Street Level No Climate 1-2 Bedroom Home (up to 1,200 sq. ft.) <
size> 5' x 10' x 10' <
unit> Interior 1st Floor Street Level No Climate 1-2 Bedroom Home (up to 1,200 sq. ft.) <
price> $84.95 <
-----
title> 5' x 14' x 10' Interior 1st Floor Street Level No Climate 1-2 Bedroom Home (up to 1,200 sq. ft.) <
size> 5' x 14' x 10' <
unit> Interior 1st Floor Street Level No Climate 1-2 Bedroom Home (up to 1,200 sq. ft.) <
price> $89.95 <
'''
