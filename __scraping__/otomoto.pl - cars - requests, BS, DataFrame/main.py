# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.02.18
# link: (stackoverflow) https://stackoverflow.com/questions/66251528/how-to-sum-all-appearances-from-list-and-print-maximum-value-from-list/

import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.otomoto.pl/osobowe/seg-sedan/?search%5Bfilter_float_price%3Afrom%5D=3000&search%5Bfilter_float_price%3Ato%5D=5000&search%5Bfilter_float_engine_capacity%3Afrom%5D=2000&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D='

response = requests.get(url)
response.raise_for_status()

# check how many pages are there
soup = bs4.BeautifulSoup(response.text, "lxml")
last_page = int(soup.select('.page')[-1].text)

print('last_page:', last_page)

data = []

for page in range(1, last_page+1):

    print('--- page:', page, '---')

    response = requests.get(url + '&page=' + str(page))
    response.raise_for_status()
    
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    all_offers = soup.select('article.offer-item')

    for offer in all_offers:
        # get the interesting data and write to file

        title = offer.find('a', class_='offer-title__link').text.strip()
        price = offer.find('span', class_='offer-price__number').text.strip().replace(' ', '').replace('\nPLN', '')

        item = [title, int(price)]
        data.append(item)
        print(item)

# --- work with data ---

df = pd.DataFrame(data, columns=['title', 'price'])
df.to_csv('carData.csv')
df.to_excel('carData.xlsx')

for name in ['BMW', 'Audi', 'Opel', 'Mercedes']:
    print('---', name, '---')
    cars = df[ df['title'].str.contains(name) ]
    print('count:', len(cars))
    print('price min    :', cars['price'].min())
    print('price average:', cars['price'].mean())
    print('price max    :', cars['price'].max())        
    
    cars.plot.hist(title=name)
    plt.show()
