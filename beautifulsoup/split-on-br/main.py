
# date: 2019.08.07
# https://stackoverflow.com/questions/57392407/how-to-split-html-text-with-br-tags/57392710#57392603
# 
# https://stackoverflow.com/questions/30694558/beautifulsoup-split-text-in-tag-by-br
# [x for x in dt.find_next_sibling('dd').contents if getattr(x, 'name', None) != 'br']
# [x for x in dt.children if x.name != 'br']

BS removes all tags when you get .text so there is no <br> to split.

You can try .get_text(separator=...) to get it and it should add separtors between text from different tags. It should put separator instead of <br>. And then you can use split(separator)

words = text_tag.get_text(separator='|', strip=True).split('|')

or using more unique separtor if '|' is used in text

words = text_tag.get_text(separator='|br|', strip=True).split('|br|')

but it may put separator in place of other tags like <b> in 'Mémoire : <b>64 GO</b>'

You can replace all <br/> with separator in original HTML and then use split(separator)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.ouedkniss.com/telephones'

html = urlopen(url)
html = html.read()
html = html.replace(b'<br/>', b'|br|')

bs = BeautifulSoup(html, 'html.parser')

text_tag = bs.find('span', class_="annonce_get_description", 
itemprop="description")

words = text_tag.text.split('|br|')
print(words)

You can do it only with inner HTML

    get inner html as one string (bytes),
    replace '<br/>' with separator,
    parse it again,
    get text (already without find())
    split(separator)

Code:

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.ouedkniss.com/telephones'

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

text_tag = bs.find('span', class_="annonce_get_description", 
itemprop="description")

inner_html = text_tag.encode_contents()
inner_html = inner_html.replace(b'<br/>', b'|br|')

bs = BeautifulSoup(inner_html, 'html.parser')
words = bs.text.split('|br|')

print(words)


