# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.08
# [web scraping - How to find only filtered postings and not "similar searches" elements when using Python and BeautifulSoup in Zillow - Stack Overflow](https://stackoverflow.com/questions/72538706/how-to-find-only-filtered-postings-and-not-similar-searches-elements-when-usin/)

import requests
from bs4 import BeautifulSoup

#link = 'https://www.zillow.com/homes/for_rent/3-_beds/2.0_baths/searchQueryState=%7B%22usersSearchTerm%22%3A%22North%20Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.29284112255858%2C%22east%22%3A-80.0628148774414%2C%22south%22%3A25.805781778630376%2C%22north%22%3A26.005282046378984%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2800%7D%2C%22price%22%3A%7B%22max%22%3A654591%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22customRegionId%22%3A%2275b80629a8X1CR16lm2ocepiiri_11uj8n%22%7D'
link = 'https://www.zillow.com/north-miami-fl/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22North%20Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.27824990551758%2C%22east%22%3A-80.07740609448243%2C%22south%22%3A25.836299974370615%2C%22north%22%3A25.974807540895462%7D%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6229%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A1000%7D%2C%22price%22%3A%7B%22max%22%3A232720%7D%7D%2C%22isListVisible%22%3Atrue%7D'
#link = 'https://www.zillow.com/north-miami-fl/rent-houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22North%20Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.23404710095215%2C%22east%22%3A-80.12160889904786%2C%22south%22%3A25.860013745504325%2C%22north%22%3A25.95111683678202%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6229%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3500%7D%2C%22price%22%3A%7B%22max%22%3A814148%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

response = requests.get(link, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

filtered = soup.find('div', {'id': 'grid-search-results'}).find('ul')

offers = filtered.find_all('article')

for item in offers:
    price = item.find('div', {'class':'list-card-price'}).text
    print(price)
    details = item.find('ul').get_text(strip=True, separator="|")
    print(details)
    print('---')

