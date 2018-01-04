import requests
from bs4 import BeautifulSoup

url_id = 'aM7aW0G58CI'

s = requests.Session()
r = s.get('https://www.youtube.com/watch?v='+url_id)
soup = BeautifulSoup(r.text, 'lxml')

# to concatenate <br> 
br = ''

for p in soup.find_all('p', id='eow-description'):
    for child in p.children:
        if child.name == 'a':
            #print(' a:', child.text)
            print(br, child.text)
            br = '' # reset br
        elif child.name == 'br':
            if child.next_sibling.name != 'br': # skip <br/> ?
                #print('br:', child.next_sibling)
                br += str(child.next_sibling)
        else:
            print('>', child.name, child)
