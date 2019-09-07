import requests
from bs4 import BeautifulSoup
import urllib.parse

url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for a in soup.find_all('a'):
    if a.img:
        src = a.img['src']
        print(urllib.parse.urljoin('https://en.wikipedia.org', src))

urllib.parse.urljoin(


#------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for a in soup.find_all('a'):
    if a.img:
        src = a.img['src']
        if src.startswith('http'):
            print(src)
        elif src.startswith('//'):
            print('https:' + src)
        elif src.startswith('/'):
            print('https://en.wikipedia.org' + src)
        else:
            print('https://en.wikipedia.org/w/' + src)
