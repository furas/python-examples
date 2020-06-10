
# date: 2020.06.10
# https://stackoverflow.com/questions/62293949/web-scraping-with-bs4-pyhton3-cant-find-elements/62294633#62294633

import requests
import bs4 as bs

#url = 'https://www.flashscore.com/field-hockey/netherlands/hoofdklasse/standings/'

url = 'https://d.flashscore.com/x/feed/ss_1_INmPqO86_GOMWObX1_table_overall'

headers = {
#    'User-Agent': 'Mozilla/5.0'
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
#    'X-Referer': 'https://www.flashscore.com/field-hockey/netherlands/hoofdklasse/standings/',
    'X-Fsign': 'SW9D1eZo',
#    'X-Requested-With': 'XMLHttpRequest',
#    'Referer': 'https://d.flashscore.com/x/feed/proxy-local',
}

r = requests.get(url, headers=headers)
#print(r.text)

soup = bs.BeautifulSoup(r.text, 'lxml')

for item in soup.find_all('span', class_='team_name_span'):
    print(item.text)


