# author: https://blog.furas.pl
# date: 2020.08.04
# link: https://stackoverflow.com/questions/63246707/python-scraping-create-payload-cnmv-es-and-render-javascript/

import requests
from bs4 import BeautifulSoup

url = 'https://www.cnmv.es/portal/Consultas/BusquedaPorEntidad.aspx' # '?lang=en'
search_text = 'aaa' # 'abc'

r = requests.get(url)
#print(response.text)

soup = BeautifulSoup(r.content, 'html.parser')

payload = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': soup.find(id="__VIEWSTATE")['value'],
    '__VIEWSTATEGENERATOR': soup.find(id="__VIEWSTATEGENERATOR")['value'],
    '__EVENTVALIDATION': soup.find(id="__EVENTVALIDATION")['value'],
    'ctl00$wBusqueda$txtBusqueda': '',
    'ctl00$ContentPrincipal$txtBusqueda': search_text,
    'ctl00$ContentPrincipal$btnBuscar': 'Buscar', #'Search'
}        

headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#    'Accept-Language': 'en-US,en;q=0.9',
#    'Content-Type': 'application/x-www-form-urlencoded',
#    'Referer': 'https://www.cnmv.es/portal/Consultas/BusquedaPorEntidad.aspx',
#    'Connection': 'keep-alive',
#    'Cache-Control': 'max-age=0',
#    'Upgrade-Insecure-Requests': '1',
#    'Origin': 'https://www.cnmv.es',
#    'Sec-Fetch-Site': 'same-origin',
#    'Sec-Fetch-Mode': 'navigate',
#    'Sec-Fetch-User': '?1',
#    'Sec-Fetch-Dest': 'document',
}

r = requests.post(url, headers=headers, data=payload)
#print(response.text)

soup = BeautifulSoup(r.content, 'html.parser')

for item in soup.find_all('option'):
    print(item['value'], '|', item.text)
