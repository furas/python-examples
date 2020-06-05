from bs4 import BeautifulSoup
import requests
import re

url = 'https://tienda.mimo.com.ar/mimo/junior/ropa-para-ninas.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
#    'Accept-Encoding': 'gzip, deflate, br',
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

#-------------------------------

all_products = []

for product in soup.find('ul', {'class': 'listado'}).find_all('li'):
    name = product.find('h3')
    
    # skip advertisement
    if not name:
        continue
    
    print('name:', name.text)
    
    price = product.find('span', {'class': 'price'})
    price = float(price.text.strip()[2:].replace('.', ''))
    print('price:', price)

    discont_image = product.find('div', {'data-posicion': 'derecha'}).find('img')
    #print('discont_image:', discont_image)
    discont = discont_image['src'].split('/')[-1].split('_')[0]
    discont = int(discont)
    print('discont (%):', discont)
    
    new_price = price * (100-discont)/100
    print('new price:', new_price)
    
    all_products.append( (name, price, discont, new_price) )
    
    print('---')
    break
#-----------------------    

    
