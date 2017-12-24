
#
# https://stackoverflow.com/a/47733374/1832058
#

import requests
from bs4 import BeautifulSoup

url = 'https://letterboxd.com/shesnicky/list/top-50-favourite-films/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

all_items = soup.find_all('div', {'data-target-link': True})

for item in all_items:
    print(item['data-target-link'])
