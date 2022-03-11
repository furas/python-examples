# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.09
# [beautifulsoup - Beautiful soup articles scraping - Stack Overflow](https://stackoverflow.com/questions/71410983/beautiful-soup-articles-scraping/71415359#71415359)

import urllib.parse
import requests
from bs4 import BeautifulSoup
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'https://www.15min.lt/tags/ajax/list/svietimas-24297?tag=24297&type=&offset={}&last_row=2&iq=L&force_wide=true&cachable=1&layout%5Bw%5D%5B%5D=half_wide&layout%5Bw%5D%5B%5D=third_wide&layout%5Bf%5D%5B%5D=half_wide&layout%5Bf%5D%5B%5D=third_wide&cosite=default'

offset = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for _ in range(5):
    print('=====', offset, '=====')
    
    offset = urllib.parse.quote_plus(offset)
    
    response = requests.get(url.format(offset), headers=headers)
    
    data = response.json()
    
    soup = BeautifulSoup(data['rows'], 'html.parser')
    antrastes = soup.find_all('h3', {'class': 'vl-title'})
    
    for item in antrastes:
        print(item.text.strip())
        print('---')
    
    offset = data['offset']  # offset for next data

