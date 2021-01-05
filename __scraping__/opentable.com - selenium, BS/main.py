# date: 2020.12.30
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# https://stackoverflow.com/questions/65501642/scraping-opentable-website-using-python-beautifulsoup/

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
import re

def parse_html(html):
    data, item = pd.DataFrame(), {}
    soup = BeautifulSoup(html, 'lxml')
    for i, resto in enumerate(soup.find_all('div', class_='rest-row-info')):
        item['name'] = resto.find('span', class_='rest-row-name-text').text

        booking = resto.find('div', class_='booking')
        item['bookings'] = re.search('\d+', booking.text).group() if booking else 'NA'

        rating = resto.select('.star-rating .star-rating-score')
        #print(rating)
        item['rating'] = rating[0]['aria-label'] if rating else 'NA'

        reviews = resto.find('span', class_='star-rating-text--review-text')
        
        reviews = resto.select('div.review-rating-text span')
        #print(reviews)
        item['reviews'] = reviews[0].text if reviews else 'NA'

        item['price'] = int(resto.find('div', class_='rest-row-pricing').find('i').text.count('$'))
        
        item['cuisine'] = resto.find_all('span', class_='rest-row-meta--cuisine')[-1].text
        #print(item['cuisine'])
        
        item['location'] = resto.find('span', class_='rest-row-meta--location').text
        data[i] = pd.Series(item)
    return data.T


restaurants = pd.DataFrame()
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
url = "https://www.opentable.com/new-york-restaurant-listings"
driver.get(url)

while True:
    sleep(1)
    new_data = parse_html(driver.page_source)
    if new_data.empty:
        break
    restaurants = pd.concat([restaurants, new_data], ignore_index=True)
    print(len(restaurants))
   # driver.find_element_by_link_text('Next').click()
    break
        
#driver.close()
restaurants.to_csv('results.csv', index=False)
print(restaurants[['rating', 'reviews', 'cuisine']])


