#!/usr/bin/env python3

# date: 2020.01.07
# ???

from bs4 import BeautifulSoup
import requests
#import webbrowser

#s = requests.Session()

#headers = {
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
#}

#response = s.get("https://www.bing.com", headers=headers)
#print(response.status_code)

params = {
    'q': 'james',
#    'go': 'Wyszukaj',
#    'qs': 'ds',
#    'form': 'QBRE'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
#    'User-Agent': 'Mozilla/5.0',
#    'Referer': 'https://www.bing.com',
}

response = requests.get("https://www.bing.com/search", params=params, headers=headers)
html = response.text

#with open('temp.html', 'w') as f:
#    f.write(html)
#webbrowser.open('temp.html')

soup = BeautifulSoup(html, 'html.parser')
cites = soup.find_all('cite')
print(cites)
