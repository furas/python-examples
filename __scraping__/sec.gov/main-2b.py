
#
# https://stackoverflow.com/a/47614478/1832058
#

#import urllib.request as urllib2 # Python 3
import urllib2
import re
import bs4 as bs

url='https://www.sec.gov/Archives/edgar/data/1580608/000158060817000015/santander201610-k.htm'

html = urllib2.urlopen(url).read().decode('utf8')
soup = bs.BeautifulSoup(html,'lxml')
text = soup.get_text()
text = text.lower()

from html import unescape

search = unescape('item&nbsp;7(a)')

# find every occurence in text    
pos = 0
while True:
    pos = text.find(search, pos)
    if pos == -1:
        break
    #print(pos, ">"+text[pos-1]+"<", ord(text[pos-1]))
    print(text[pos:pos+20])
    pos += 1
