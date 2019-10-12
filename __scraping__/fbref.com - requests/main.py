#!/usr/bin/env python

# date: 2019.09.21
# 

from bs4 import BeautifulSoup as BS
import requests 

url = 'https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two'

response = requests.get(url)
soup = BS(response.content, 'html.parser')

stats = soup.find('div', id="team_stats")

data = []
for row in stats.find_all('td'):
    text = row.get_text(strip=True)
    data.append(text)
    
print('Possession:', data[0], '|', data[1])

text1, percent1 = data[2].split('—')
percent2, text2 = data[3].split('—')
text1 = text1.strip('\xa0')
text2 = text2.strip('\xa0')
print('Shots on Target:', text1, '|', percent1, '|', text2, '|', percent2)

text1, percent1 = data[4].split('—')
percent2, text2 = data[5].split('—')
text1 = text1.strip('\xa0')
text2 = text2.strip('\xa0')
print('Saves:', text1, '|', percent1, '|', text2, '|', percent2)

    
