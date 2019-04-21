# date: 2019.04.16
# https://stackoverflow.com/questions/55699472/web-scraping-python-indexing-issue-for-dataframe/55700180#55700180

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://spotifycharts.com/regional/global/daily/'

r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')

chart = soup.find('table', {'class': 'chart-table'})
tbody = chart.find('tbody')

all_rows = []

for tr in tbody.find_all('tr'):

    rank_text = tr.find('td', {'class': 'chart-table-position'}).text

    artist_text = tr.find('td', {'class': 'chart-table-track'}).find('span').text
    artist_text = artist_text.replace('by ','').strip()

    title_text = tr.find('td', {'class': 'chart-table-track'}).find('strong').text

    streams_text = tr.find('td', {'class': 'chart-table-streams'}).text

    all_rows.append([rank_text, artist_text, title_text, streams_text])

# after `for` loop

df = pd.DataFrame(all_rows, columns=['Rank','Artist','Title','Streams'])
print(df)#.head(15))
