# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.06

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#url = input('Enter url: ')
url = 'http://py4e-data.dr-chuck.net/comments_1547077.xml'
print('Retrieving:', url)

# ---

response = urllib.request.urlopen(url)
data = response.read()
print('Retrieved :', len(data), 'characters')

# ---

tree = ET.fromstring(data)
all_items = tree.findall('comments/comment')
all_values = []

for item in all_items:
    text = item.find('count').text
    all_values.append( float(text) )
    
print('Count:', len(all_values))
print('  Sum:', sum(all_values))
