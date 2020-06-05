#!/usr/bin/env python3

# date: 2020.05.24
# https://stackoverflow.com/questions/61981006/extracting-p-from-div-class-python-to-get-addresses/

import requests
import BeautifulSoup
import csv
import urllib2
import time

initial_url = "https://www.lifetime.life"

response = requests.get("https://www.lifetime.life/view-all-locations.html")
soup = BeautifulSoup.BeautifulSoup(response.text)

with open('gyms2.csv', 'w') as gf:
    gymwriter = csv.writer(gf)
    for a in soup.findAll('a'):
        if '/life-time-locations/' in a['href']:
            gymurl = urllib2.urlparse.urljoin(initial_url, a.get('href'))
            print(gymurl)
            
            response = requests.get(gymurl)
            sub_soup = BeautifulSoup.BeautifulSoup(response.text)
            
            try:
                address_line = sub_soup.find('p', {'class': 'small m-b-sm p-t-1'}).find('span', {'class': 'btn-icon-text'})

                gymrow = [gymurl, address_line.text]
                print(gymrow)
                gymwriter.writerow(gymrow)
                time.sleep(3)
                continue # go back to `for`            
            except Exception as ex:
                print('ex:', ex)
                
            try:
                address_line = sub_soup.find('div', {'class': 'btn-resp-md'}).find('p')
                gymrow = [gymurl, address_line.text.strip()]
                print('type 2:', gymrow)
                gymwriter.writerow(gymrow)
                time.sleep(3)
                continue # go back to `for`            
            except Exception as ex:
                print('ex:', ex)

            try:
                address_line = sub_soup.find('p', {'class': 'm-b-grid'})
                gymrow = [gymurl, address_line.text.strip()]
                print('type 3:', gymrow)
                gymwriter.writerow(gymrow)
                time.sleep(3)
                continue # go back to `for`            
            except Exception as ex:
                print('ex:', ex)                
