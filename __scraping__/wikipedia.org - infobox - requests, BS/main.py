
# 2020.06.30
# https://stackoverflow.com/questions/62632892/extracting-table-data-from-wikipedia-api/

import urllib3
import requests
from bs4 import BeautifulSoup
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://en.wikipedia.org/wiki/Rahul_Gandhi'
#url = 'https://en.wikipedia.org/wiki/Sonia_Gandhi'

session = requests.Session()

html = session.get(url, verify=False).content

soup = BeautifulSoup(html, 'lxml')

table = soup.find('table', {'class': 'infobox vcard'})

# --- 

content = {}
header1 = None
header2 = None
current = content

for row in table.find_all('tr'):
    
    children = list(row.children)
    
    # replace '<br>' with '\n'
    for item in children:
        for br in item.find_all('br'):
            br.replace_with('\n' + br.text)

    # headers/subheaders (sections/subsections)
    if len(children) == 1:

        #html = str(children[0]).strip()
        
        # skip empty rows
        inner_html = children[0].decode_contents().strip()
        if not inner_html:
            continue
        #print(inner_html)
        
        text = children[0].get_text().strip() # don't `get_text(strip=True)` to keep `\n`

        # clean text - replace non-breaking space         
        text = text.replace('\u00a0', ' ')
        #print(item.name, '|', text)

        images = [{
                    'src': x.get('src'),
                    'width': x.get('width', ''),
                    'height': x.get('height', ''),
                    'alt': x.get('alt'),
                  } for x in children[0].find_all('img')]

        links  = [{
                    'text': x.text,
                    'href': x.get('href', ''),
                    'title': x.get('title', ''),
                  } for x in children[0].find_all('a')]
        
        # create headers / section
        if children[0].name == 'th':
            header1 = text
            
            section = {
                'type': 'header',
                #'html': html,
                'key' : text,
                'text': text,   # text in header
                'links': links, # links in header
                'images': images,
                'items': {},    # items in section
            }
            
            content[header1] = section  # add section to content
            current = section['items']  # keep access to add items later

        # create subheaders / subsection
        if children[0].name == 'td':
            header2 = text

            section = {
                'type': 'header',
                #'html': html,
                'key' : text,
                'text': text,   # text in subheader
                'links': links, # links in subheader
                'images': images,
                'items': {},    # items in subsection
            }
            
            content[header1]['items'][header2] = section  # add section to content
            current = section['items']  # keep access to add items later
            
    # items in sections/sections
    if len(children) == 2:
        #html   = str(children[1])

        # skip empty rows
        #inner_html = children[0].decode_contents().strip()
        #if not inner_html:
        #    continue
        #print(inner_html)
        
        key    = children[0].get_text().strip()
        text   = children[1].get_text().strip()
        
        links  = [{
                    'text': x.text,
                    'href': x.get('href', ''),
                    'title': x.get('title', ''),
                  } for x in children[1].find_all('a')]
        
        images = [{
                    'src': x.get('src'),
                    'width': x.get('width', ''),
                    'height': x.get('height', ''),
                    'alt': x.get('alt'),
                  } for x in children[1].find_all('img')]

        # clean text - replace non-breaking space 
        text = text.replace('\u00a0', ' ')

        current[key] = {
            'type': 'item',
            #'html': html,
            'key': key,
            'text': text,
            'links': links,
            'images': images,
            'items': {}
        }

        #print(content[key])

#first_key = list(content.keys())[0]
#print(first_key)
#print(json.dumps(content[first_key], indent=2))

print(json.dumps(content, indent=2))


