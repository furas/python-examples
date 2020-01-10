#!/usr/bin/env python3

# date: 2020.01.10
# https://stackoverflow.com/questions/59674049/multiple-pages-web-scraping-with-python-and-beautiful-soup/

import requests
from bs4 import BeautifulSoup # HTML data structure
import pandas as pd

def get_page_data(number):
    print('number:', number)
    
    url = 'https://e-turysta.pl/noclegi-krakow/?page={}'.format(number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    container = soup.find(id='nav-lista-obiektow')
    items = container.find_all(class_='et-list__details flex-grow-1 d-flex d-md-block flex-column')

    # better group them - so you could add default value if there is no nazwa or adres
    dane = []
    
    for item in items:
        nazwa = item.find(class_='h3 et-list__details__name').get_text(strip=True)
        adres = item.find(class_='et-list__city').get_text(strip=True)
        dane.append([nazwa, adres])
        
    return dane

# --- main ---

wszystkie_dane = []
for number in range(1, 23):
    dane_na_stronie = get_page_data(number)
    wszystkie_dane.extend(dane_na_stronie)

dane = pd.DataFrame(wszystkie_dane, columns=['nazwa', 'adres'])

dane.to_csv('noclegi.csv', index=False)
