#!/usr/bin/env python3


from selenium import webdriver
import urllib.parse

url = 'https://www.yelp.com/biz/daeho-kalbijjim-and-beef-soup-san-francisco-9?osq=Restaurants'
url = 'https://www.yelp.com/biz/san-tung-san-francisco-2?page_src=related_bizes'
url = 'https://www.yelp.com/biz/skool-san-francisco?page_src=related_bizes'

driver = webdriver.Firefox()

driver.get(url)

all_items = driver.find_elements_by_xpath('//div[contains(@class, "stickySidebar__")]/section/div/div')

try:
    link = all_items[0].find_element_by_xpath('.//a')
    link = link.get_attribute('href').split('url=')[1].split('&')[0]
#except selenium.common.exceptions.NoSuchElementException:
except:
    link = ''
print('link:', urllib.parse.unquote(link))

try:
    phone = all_items[1]
    phone = phone.text
#except selenium.common.exceptions.NoSuchElementException:
except:
    phone = ''
print('phone:', phone)


