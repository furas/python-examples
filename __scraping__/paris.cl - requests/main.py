# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.16
# [python - web scrap from difrents links and run a routine to get the data - Stack Overflow](https://stackoverflow.com/questions/71476013/web-scrap-from-difrents-links-and-run-a-routine-to-get-the-data/)

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.paris.cl/tecnologia/consolas-videojuegos/'

params = {
    'start': 0,
    'sz': 40,
}

results = []

for offset in range(0, 21, 40):
    params['start'] = offset

    response = requests.get(url, params=params)
    print('url:', response.url)
                    
    soup = bs(response.text, "html.parser")

    all_products = soup.find_all('div', {'class': 'product-tile'})

    for product in all_products:
        itemid = product.get('data-itemid') 
        print('itemid:', itemid)

        data = product.get('data-product') 
        print('data:', data)
        
        name = product.find('span', {'itemprop': 'name'}).text
        print('name:', name)
        
        all_prices = product.find_all('div', {'class': 'price__text'})
        print('len(all_prices):', len(all_prices))
        
        price = all_prices[0].get('aria-label')
        print('price:', price)
        
        results.append( (itemid, name, price, data) )
        print('---')

# ---

# ... here you can save all `results` in file ...
        
