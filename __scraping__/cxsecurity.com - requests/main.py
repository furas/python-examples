# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.17
# [python - DevTools and browser show different response - Stack Overflow](https://stackoverflow.com/questions/71516548/devtools-and-browser-show-different-response/)

import requests
from bs4 import BeautifulSoup

params = {
    'database': 'wlb' # `wlb` for Bugtraq, 'cve' for CVE Content, 
    
    'query': 'google',
    'limit': 30,
    'sort': 'DESC',
    'dates': '2022.3.17.1999.1.1'
}    

url_pattern = 'https://cxsecurity.com/search/{database}/{sort}/AND/{dates}/{page}/{limit}/{query}/'

for number in range(5):
    print('\n--- page:', number, '---\n')
    
    params['page'] = number
    url = url_pattern.format(**params)
    print('url:', url)
    print()
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for url in soup.select('h6 a'):
        print(url.text)
