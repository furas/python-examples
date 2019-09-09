
# date: 2019.09.09
# link: https://stackoverflow.com/questions/57856461/python-run-search-function-on-net-web-page

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get('http://www.drugeye.pharorg.com/', headers=headers)
soup = BeautifulSoup(r.text,'lxml')

payload = {
    'ttt': 'asd',
    'b1': 'wait...',
    'Passgenericname': None,
    '__VIEWSTATE': soup.find('input', {'id':'__VIEWSTATE'})['value'],
    '__VIEWSTATEGENERATOR': soup.find('input', {'id':'__VIEWSTATEGENERATOR'})['value'],
    '__EVENTVALIDATION': soup.find('input', {'id':'__EVENTVALIDATION'})['value'],
}

r = requests.post('http://www.drugeye.pharorg.com/', data=payload, headers=headers)

soup = BeautifulSoup(r.text,'lxml')
print(soup.find_all('table')[1].prettify())
