
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.12
#
# title: Can anybody help me with an integer problem?
# url: https://stackoverflow.com/questions/70326175/can-anybody-help-me-with-an-integer-problem/70326848#70326848

# [Can anybody help me with an integer problem?](https://stackoverflow.com/questions/70326175/can-anybody-help-me-with-an-integer-problem/70326848#70326848)

# [Exchange Rates API](https://www.iban.com/exchange-rates-api)

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.iban.com/exchange-rates')
soup = BeautifulSoup(r.content, 'html.parser')

data = dict()

table = soup.find('table', class_='table table-bordered table-hover downloads')

trs = table.find_all('tr')

for tr in trs[1:]:
    name  = tr.find('img')['alt'].lower()
    value = float(tr.find('strong').text)
    data[name] = value
    
# ---

name  = input('Name: ').lower()
value = int(input('Value: '))

print(data[name] * value)
