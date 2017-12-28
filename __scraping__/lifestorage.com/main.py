from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

urls = [
    'https://www.lifestorage.com/storage-units/florida/orlando/32810/610-near-lockhart/?size=5x5'
]

filename = 'life_storage.csv'

f = open(filename, 'a+')
csv_writer = csv.writer(f) 

headers = ['unit_size', 'unit_type', 'description', 'online_price', 'reg_price', 'store_address', 'store_city', 'store_state', 'store_postalcode' ]

##unit_size = 5'x10' withouth the '
##unit_type = climate controlled or not (this could be blank if non-climate)
##descirption = the level it's on and type of access.
##online_price = $##/mo text
##reg_price = the scratched off $## text

csv_writer.writerow(headers)

for my_url in urls:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')   

    store_location = page_soup.find("div", {"itemprop": "address"})
    
    # need `li`
    containers = page_soup.find("ul", {"id": "spaceList"}).findAll('li')
    print('len(containers):', len(containers))

    item = store_location.find("span", {"itemprop": "streetAddress"})
    store_address = item.text.strip()
    
    item = store_location.find("span", {"itemprop": "addressLocality"})
    store_city = item.text.strip()
    
    item = store_location.find("span", {"itemprop": "addressRegion"})
    store_state = item.text.strip()
    
    item = store_location.find("span", {"itemprop": "postalCode"})
    store_postalcode = item.text.strip()
    
    for container in containers:
        item = container.find("div", {"class": "storesRow"})

        if item and item.strong:
            text = item.strong.text.strip()
            parts = text.split('-')
            if len(parts) > 0:
                unit_size = parts[0].strip().replace('*', "")
            else:
                unit_size = ''
                
            if len(parts) > 1:
                unit_type = parts[1].strip()
            else:
                unit_type = ''
        else:
            continue

        item = container.find("ul", {"class": "features"})

        if item:
            description = item.text.strip().replace("\n", ',')
        else:
            description = ''
                
        item = container.find("div", {"class": "priceBox"})

        if item and item.i:
            reg_price = item.i.text.strip()
        else:
            reg_price = ''

        if item and item.strong:
            if item.i:
                item.i.extract() # remove <i>`
            online_price = item.strong.text.strip()
        else:
            online_price = ''
        
        csv_writer.writerow([unit_size, unit_type, description, online_price, reg_price, store_address, store_city, store_state, store_postalcode])

f.close()
