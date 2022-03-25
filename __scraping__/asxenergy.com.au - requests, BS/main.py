# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.18
# [html - How to extract a table from website without specifying the web browser in python - Stack Overflow](https://stackoverflow.com/questions/71522775/how-to-extract-a-table-from-website-without-specifying-the-web-browser-in-python/)

import requests
from bs4 import BeautifulSoup

headers = {
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0', 
    'X-Requested-With': 'XMLHttpRequest'     
}

URL = "https://www.asxenergy.com.au/futures_nz/dataset"
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
market_dataset = soup.findAll("div", attrs={'class':'market-dataset'})

print('len(market_dataset):', len(market_dataset))


