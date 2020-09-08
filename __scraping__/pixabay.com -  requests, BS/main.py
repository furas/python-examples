
# date: 2020.09.07
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# https://stackoverflow.com/questions/63767927/cant-scrape-some-static-image-links-from-a-webpage-using-requests

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US;q=0.7,en;q=0.3",
    "Cache-Control": "no-cache",
    #"Connection": "keep-alive",
    #"Pragma": "no-cache",
}

s = requests.Session()
s.headers.update(headers)  # it will use there hearders in all requests

# --- get cookies ---

url = 'https://pixabay.com/'

r = s.get(url)
print(r.status_code)  # 403 but it is not problem

# only for test 
#r = s.get('https://pixabay.com/')
#print(r.status_code)  # 200

# --- get images ---

url = 'https://pixabay.com/images/search/office/'

r = s.get(url)
print(r.status_code)
#print(r.text)

results = []

soup = BeautifulSoup(r.text, "lxml")

for item in soup.select(".search_results a > img[src]"):
    src = item.get("src")
    if src is not None and 'blank.gif' not in src:
        print('src:', src)
        results.append(src)
    else:
        src = item.get("data-lazy")
        print('data-lazy:', src)
        results.append(src)

print('len:', len(results))
