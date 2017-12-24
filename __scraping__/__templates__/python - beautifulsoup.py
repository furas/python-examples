import requests
from bs4 import BeautifulSoup

url = ""

html = ''' '''
html = requests.get(url)

soup = BeautifulSoup(html)
divs = soup.find_all('div', {'class': 'xxx'}) 

for div in divs:
   print(div.text)
   
    
