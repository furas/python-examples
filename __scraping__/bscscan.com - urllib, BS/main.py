
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.23
#
# title: How to properly extract data that returns None in Python Beautifulsoup
# url: https://stackoverflow.com/questions/68493228/how-to-properly-extract-data-that-returns-none-in-python-beautifulsoup/68493491?noredirect=1#comment121049699_68493491

from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen


url = 'https://bscscan.com/tx/0x1b6f00c8cd99e0daac5718c743ef9a51af40f95feae23bf29960ae1f66a1cff7'
#url = 'https://bscscan.com/tx/0xc54d83b870a1b4159f12bff092c8a24dfa045e133b07d3a3a41898293ac86c71'
headers = {'User-Agent': 'Mozilla/5.0'}

req = Request(url, headers=headers)
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

val = soup.find('span', class_='u-label u-label--value u-label--secondary text-dark rounded mr-1').text
transfee = soup.find('span', id='ContentPlaceHolder1_spanTxFee').text
fromaddr = soup.find('span', id='spanFromAdd').text
token = soup.find('span', class_='hash-tag text-truncate hash-tag-custom-from tooltip-address').text

print("From:            ", fromaddr)
print("Value:           ", val)
print("Transaction Fee: ", transfee)
print("Tokens:")

main_data = soup.select("ul#wrapperContent div.media-body")

for item in main_data:
    all_span = item.find_all("span", class_='mr-1')
    #for number, span in enumerate(all_span):
    #    print(number, span.get_text(strip=True))
    last_span = all_span[-1]
    
    all_a = item.find_all("a")
    last_a = all_a[-1]
    
    print("{:>35} | {:18} | https://bscscan.com{}".format(last_span.get_text(strip=True), last_a.get_text(strip=True), last_a['href']))

