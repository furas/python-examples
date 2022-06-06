# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.06
# [html - Problem with outputting text (Python, Beautifulsoup) - Stack Overflow](https://stackoverflow.com/questions/72518061/problem-with-outputting-text-python-beautifulsoup/72518812#72518812)

# it needs `User-Agent` to get Chinese data in encoding `utf-8`

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
}

url = 'https://www.hko.gov.hk/cis/front_uc.xml'

response = requests.get(url, headers=headers)
data = response.json()

#print(response.text)

print('Min:', data['temp']['currentMin'])
print('Max:', data['temp']['currentMax'])
print('Festival:', data['festival']['engName'])
print('Festival:', data['festival']['chiName'])
