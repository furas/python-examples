import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://www.deezer.com/en/profile/1589856782/loved'

r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')

all_scripts = soup.find_all('script')

data = json.loads(all_scripts[6].get_text()[27:])

print('key:', data.keys())
print('key:', data['TAB'].keys())
print('key:', data['DATA'].keys())
print('---')

for item in data['TAB']['loved']['data']:
    print('ART_NAME:', item['ART_NAME'])
    print('SNG_TITLE:', item['SNG_TITLE'])
    print('---')
