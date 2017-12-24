
#
# https://stackoverflow.com/a/47744797/1832058
#

from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.cnbc.com/2017/12/07/pinterest-hires-former-facebook-exec-gary-johnson-to-run-corporate-dev.html").text
soup = BeautifulSoup(html, 'html5lib')

all_paragraphs = soup.find_all('p')

for p in all_paragraphs:
    #print(p) # all HTML
    print(p.get_text()) # p.get_text(strip=True)
    # or
    print(p.text)
