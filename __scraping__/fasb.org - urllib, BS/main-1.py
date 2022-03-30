# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.29
# [python - Downloading pdf from URL with urllib (getting weird html output instead) - Stack Overflow](https://stackoverflow.com/questions/71657540/downloading-pdf-from-url-with-urllib-getting-weird-html-output-instead/)

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as BS

url = 'https://www.fasb.org/page/showpdf?path=0001-%201700-UFI%20AICPA%20ACSEC%20Hanson.pdf'

response = urllib.request.urlopen(url)

soup = BS(response.read(), 'html.parser')

iframe = soup.find('iframe')
url = iframe['src']

filename = urllib.parse.unquote(url)
filename = filename.rsplit('/', 1)[-1]

urllib.request.urlretrieve(url, filename)
