# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.24
# 

import requests
from bs4 import BeautifulSoup
#import urllib.parse

# PEP8: `lower_case_names` for functions and variables

def get_data(url):   
    
    response = requests.get(url)
    #print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    
    listings = soup.find_all('div', class_='row property results')
    for listing in listings:
        address = listing.find('a', class_='address').text.strip()  # PEP8: `=` without spaces inside `()`
        price = listing.find('a', class_='price').text.replace('▲', '').replace('▼', '').strip()
        print('address:', address)
        print('price  :', price)
        print('---')

    # find next page
    next_link = soup.find('a', string='Next »')
    if next_link:
        #return urllib.parse.urljoin('https://www.vancouverforsale.ca', next_link['href'])
        return 'https://www.vancouverforsale.ca' + next_link['href']
    
# --- main ---

page_link = 'https://www.vancouverforsale.ca/search/results/?city=Langley&region=all&list_price_min=50000&list_price_max=all&beds_min=all&baths_min=all&type=con'

while True:
#for count in range(3):
    print(page_link)
    page_link = get_data(page_link)
    if not page_link:
        break

