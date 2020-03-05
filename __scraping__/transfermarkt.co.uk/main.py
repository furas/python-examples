#!/usr/bin/env python3

# date: 2020.03.05
# 

import requests
from bs4 import BeautifulSoup

url = "http://www.S/ederson/profil/spieler/238223"

response = requests.get(url, headers={'user-agent':"Mozilla/5.0"})

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'auflistung'})

data = [x.text.strip().replace('\xa0', ' ') for x in table.find_all('td')]

print(data)
