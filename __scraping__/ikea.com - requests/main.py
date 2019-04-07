
# date: 2019.04.07
# https://stackoverflow.com/questions/55541971/image-src-text-scrap-and-tablescrap-from-a-webpage-using-beautifulsoup/55542309?noredirect=1#comment97819263_55542309

#------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ikea.com/sa/en/catalog/products/00361049/")

soup = BeautifulSoup(r.text, "html.parser")

html = soup.select('div#productDimensionsContainer div#metric')[0].encode_contents().decode().strip()
data = list(filter(None, html.split('<br/>')))
print(data)

# ['Width: 82 cm', 'Depth: 96 cm', 'Height: 101 cm', 'Seat width: 49 cm', 'Seat depth: 54 cm', 'Seat height: 45 cm']

html = soup.select('div#custMaterials')[0].encode_contents().decode().strip()
data = list(filter(None, html.split('<br/>')))
print(data)

# ['Total composition: 100% polyester', 'Frame: Solid wood, Plywood, Particleboard, Polyurethane foam 25 kg/cu.m., Polyurethane foam 35 kg/cu.m., Polyester wadding', 'Seat cushion: Polyurethane foam 35 kg/cu.m., Polyester wadding', 'Leg: Solid beech, Clear lacquer']

#------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import json

r = requests.get("https://www.ikea.com/sa/en/catalog/products/00361049/")
soup = BeautifulSoup(r.text, "html.parser")

# var jProductData = {"product":{"items": ... }};

all_scripts = soup.select('script')#[0].encode_contents().decode().strip()

for script in all_scripts:
    script = script.encode_contents().decode().strip()
    if 'var jProductData' in script:
        for row in script.split('\n'):
            if 'var jProductData' in row:
                data = json.loads(row.strip()[19:-1])
                for item in data['product']['items']:
                    #print(item['pkgInfoArr'][0])
                    print('articleNumber:', item['pkgInfoArr'][0]['articleNumber'])
                    print('weightMet:', item['pkgInfoArr'][0]['pkgInfo'][0]['weightMet'])
                    print('widthMet:', item['pkgInfoArr'][0]['pkgInfo'][0]['widthMet'])
                    print('quantity:', item['pkgInfoArr'][0]['pkgInfo'][0]['quantity'])
                    print('consumerPackNo:', item['pkgInfoArr'][0]['pkgInfo'][0]['consumerPackNo'])
                    print('lengthMet:', item['pkgInfoArr'][0]['pkgInfo'][0]['lengthMet'])
                    print('heightMet:', item['pkgInfoArr'][0]['pkgInfo'][0]['heightMet'])
                    print('---')
                    
#------------------------------------------------------------------------------

import requests

url = 'https://www.ikea.com/sa/en/iows/catalog/products/?catalog=departments&category=10687&type=json&dataset=small,allImages,prices&count=11&sort=relevance&sortorder=ascending&startIndex=0'

r = requests.get(url)

data = r.json()

for item in data['products']:
    print(item['item']['name'])
    for image in item['item']['images']['large']:
        print(image)
        
                            
