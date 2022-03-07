# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.07
# [web scraping with python requests post request - Stack Overflow](https://stackoverflow.com/questions/71373590/web-scraping-with-python-requests-post-request/71384223#71384223)

import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()

# --- GET ---

headers = {
    "User-Agent": "Mozilla/5.0",
}

url = "https://vahaninfos.com/vehicle-details-by-number-plate"
res = session.get(url, headers=headers, verify=False)

token = re.findall('token = "([^"]*)"', res.text)[0]
print('token:', token)

# --- POST ---

headers = {
    "User-Agent": "Mozilla/5.0",
#    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
#    "X-Requested-With": "XMLHttpRequest",
    'num': token,
}

payload = {
    "number": "UP32AT5472",
    "g-recaptcha-response": "",
}

url = "https://vahaninfos.com/getdetails.php"
res = session.post(url, headers=headers, verify=False, data=payload)
print(res.text)

# --- SOUP ---

soup = BeautifulSoup(res.text, 'html.parser')

for row in soup.find_all('tr'):
    cols = row.find_all('td')

    key = cols[0].text
    val = cols[-1].text

    print(f'{key:22} | {val}')
