import requests
from bs4 import BeautifulSoup 

headers = { 
    'User-Agent': 'Mozilla/5.0',
}
 
headers = {'Accept-Language': "lang=AR-DZ"}

s = requests.Session()

url = 'http://www.mae.gov.dz/select_language.aspx?language=ar&file=default_ar.aspx'
r = s.get(url)#, headers=headers)

url = 'http://www.mae.gov.dz/news_article/6396.aspx'
r = s.get(url)#, headers=headers)

soup = BeautifulSoup(r.content, "lxml")
print(soup.getText)

