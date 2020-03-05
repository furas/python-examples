
# date: 2020.03.01
# https://stackoverflow.com/questions/60477459/how-to-scrape-table-from-livescore-in-using-python

import requests
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
#    'Accept': '*/*',
#    'Accept-Language': '*',
#    'Accept-Encoding': 'gzip, deflate, br',
#    'X-Referer': 'https://www.livescore.in/it/calcio/germania/bundesliga/classifiche/',
    'X-Fsign': 'SW9D1eZo',
#    'X-Requested-With': 'XMLHttpRequest',
#    'Connection': 'keep-alive',
#    'Referer': 'https://d.livescore.in/it/x/feed/proxy-local',
}

#url = 'https://d.livescore.in/it/x/feed/ss_4_UoXxkTs4_dAfCUJq0_over_under_overall'
url = 'https://d.livescore.in/it/x/feed/ss_4_UoXxkTs4_dAfCUJq0_over_under_home'
r = requests.get(url, headers=headers)

#print(r.status_code)
#print(r.text[:1000])

soup = BS(r.text, 'html.parser')

data = []
table = soup.find('div', {'class': 'table__body'})
for row in table.find_all('div', {'class': 'table__row'}):
    row_data = []
    for cell in row.find_all('div', {'class': 'table__cell'}):
        cell_data = cell.text.strip()
        row_data.append(cell_data)
    data.append(row_data)

for row in data:
    print(row)        

"""
Result:
    
['1.', 'Hoffenheim', '13', '13', '0', '19:31', '3.8', '?\n+\n+\n+\n+\n+']
['2.', 'Dortmund', '12', '12', '0', '41:10', '4.3', '?\n+\n+\n+\n+\n+']
['3.', 'Augusta', '12', '12', '0', '24:21', '3.8', '?\n+\n+\n+\n+\n+']
['4.', 'Paderborn', '12', '12', '0', '16:29', '3.8', '?\n+\n+\n+\n+\n+']
['5.', 'RB Lipsia', '12', '12', '0', '32:13', '3.8', '?\n+\n+\n+\n+\n+']
['6.', 'Francoforte', '12', '12', '0', '27:16', '3.6', '?\n+\n+\n+\n+\n+']
['7.', 'Dusseldorf', '12', '12', '0', '13:23', '3', '?\n+\n+\n+\n+\n+']
['8.', 'Colonia', '12', '12', '0', '20:16', '3', '?\n+\n+\n+\n+\n+']
['9.', 'Union Berlino', '12', '12', '0', '18:16', '2.8', '?\n+\n+\n+\n+\n+']
['10.', 'Bayern', '12', '11', '1', '36:11', '3.9', '?\n+\n-\n+\n+\n+']
['11.', 'Brema', '11', '11', '0', '8:26', '3.1', '?\n+\n+\n+\n+\n+']
['12.', 'Leverkusen', '12', '11', '1', '21:13', '2.8', '?\n+\n+\n+\n+\n+']
['13.', 'Schalke', '12', '11', '1', '17:17', '2.8', '?\n+\n+\n+\n+\n+']
['14.', 'Magonza', '12', '11', '1', '14:20', '2.8', '?\n+\n-\n+\n+\n+']
['15.', 'Wolfsburg', '12', '11', '1', '16:13', '2.4', '?\n+\n+\n+\n+\n+']
['16.', 'Friburgo', '11', '11', '0', '13:13', '2.4', '?\n+\n+\n+\n+\n+']
['17.', 'Monchengladbach', '11', '10', '1', '27:13', '3.6', '?\n+\n+\n+\n+\n+']
['18.', 'Hertha', '12', '10', '2', '12:26', '3.2', '?\n+\n+\n-\n+\n-']
"""
