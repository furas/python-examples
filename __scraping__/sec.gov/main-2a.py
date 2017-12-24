#import urllib.request as urllib2 # Python 3
import urllib2
import re
import bs4 as bs

url='https://www.sec.gov/Archives/edgar/data/1580608/000158060817000015/santander201610-k.htm'

html = urllib2.urlopen(url).read().decode('utf8')
soup = bs.BeautifulSoup(html,'lxml')
text = soup.get_text()
text = text.encode('utf-8') # only Python 2
text = text.lower()

#text = text.replace(chr(160), " ") # Python 3
text = text.replace(char(194)+chr(160), " ") # Python 2

search = 'item 7(a)'

# find every occurence in text    
pos = 0
while True:
    pos = text.find(search, pos)
    if pos == -1:
        break
    #print(pos, ">"+text[pos-1]+"<", ord(text[pos-1]))
    print(text[pos:pos+20])
    pos += 1
