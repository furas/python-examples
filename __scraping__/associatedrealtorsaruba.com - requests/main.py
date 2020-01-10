#!/usr/bin/env python3

# date: 2020.01.07
# https://stackoverflow.com/questions/59632031/how-to-extract-href-when-href-element-is-a-hyperlink?noredirect=1#comment105434826_59632031

import requests
from bs4 import BeautifulSoup as BS

url = 'https://associatedrealtorsaruba.com/index.php?option=com_ezrealty&Itemid=11&task=results&cnid=0&custom7=&custom8=&parking=&type=0&cid=0&stid=0&locid=0&minprice=&maxprice=&minbed=&maxbed=&min_squarefeet=&max_squarefeet=&bathrooms=&sold=0&lug=0&featured=0&custom4=&custom5=&custom6=&postcode=&radius=&direction=DEFAULT&submit=Search'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0', # need full UA
}

for x in (0, 20, 40):
    r = requests.get(url + '&limitstart={}'.format(x), headers=headers)
    print('\n---', x, '---\n')

    soup = BS(r.text, 'html.parser')

    all_items = soup.find_all('span', {'class': 'h3'})
    for item in all_items:
        print(item.get_text(strip=True))
     

