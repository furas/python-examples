#!/usr/bin/env python3 

# date: 2019.12.30
# https://stackoverflow.com/questions/59535798/python-webscraping-with-beautifulsoup-not-displaying-full-content/59536553#59536553

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.forexfactory.com/#detail=108867")
# page uses JavaScript to redirect page so browser may shows different results.

soup = BeautifulSoup(r.text, 'lxml')

table = soup.find("table", class_="calendar__table")

for row in table.find_all('tr', class_='calendar__row--grey'):
    
    currency = row.find("td", class_="currency")
    #print(currency.prettify()) # before get text
    currency = currency.get_text(strip=True)

    actual = row.find("td", class_="actual")
    actual = actual.get_text(strip=True)

    forecast = row.find("td", class_="forecast")
    forecast = forecast.get_text(strip=True)
    
    print(currency, actual, forecast)


