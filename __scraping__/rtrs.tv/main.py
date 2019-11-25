from requests import session

from bs4 import BeautifulSoup

url = r'https://www.rtrs.tv/vijesti/index.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

with session() as c:

    r = c.get(url, headers=headers)

    print(r)

    soup = BeautifulSoup(r.text, 'html.parser')

    all_h2 = soup.find_all('h2')
    for item in all_h2:
        print(item.text)
