#!/usr/bin/env python3 

# date: 2019.11.23
# https://stackoverflow.com/questions/59008426/python-web-scrapping-if-using-all-scalar-values-you-must-pass-an-index

import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.medindia.net/doctors/drug_information/abacavir.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
drug = soup.find(class_='mi-container__fluid')
#print(drug)

# whole page contain drug content
items = drug.find_all(class_='report-content drug-widget')
#print(items)

# extract drug information from drug content into individual variable
trade_name = items[0].find(class_='drug-content').get_text()
function = items[1].find(class_='drug-content').get_text()
contraindications = items[2].find(class_='drug-content').get_text()
dosage = items[3].find(class_='drug-content').get_text()
how_to_use = items[4].find(class_='drug-content').get_text()
warnings = items[5].find(class_='drug-content').get_text()
storage = items[7].find(class_='drug-content').get_text()


drug_stuff = pd.DataFrame({
    'trade_name': [trade_name],
    'function': [function],
    'contraindications': [contraindications],
    'dosage': [dosage],
    'how_to_use': [how_to_use],
    'warnings': [warnings],
    'storage': [storage],
})

print(drug_stuff)
