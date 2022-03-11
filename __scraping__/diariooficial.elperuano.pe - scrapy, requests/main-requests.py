# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.09
# [javascript - Web Scraping Journal "El Peruano" - Python/Scrapy - Stack Overflow](https://stackoverflow.com/questions/71402424/web-scraping-journal-el-peruano-python-scrapy/71403407#71403407)

import requests

# --- GET ---

headers = {
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
}

url = 'https://diariooficial.elperuano.pe/Normas'

response = requests.get(url, headers=headers)
print(response)

# --- POST ---

url = 'https://diariooficial.elperuano.pe/Normas/Filtro?dateparam=03/08/2022 00:00:00'

params = {
    'cddesde': '01/03/2022',
    'cdhasta': '03/03/2022',
#    'X-Requested-With': 'XMLHttpRequest',
}

headers = {
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
#    'Referer': "https://diariooficial.elperuano.pe/Normas",
#    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.post(url, data=params, headers=headers)
print(response)
print(response.text[:1000])
