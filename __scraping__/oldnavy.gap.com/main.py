#!/usr/bin/env python3

# date: 2016.11.24 (update: 2020.06.13)
# https://stackoverflow.com/questions/40777864/retrieving-all-information-from-page-beautifulsoup/

from selenium import webdriver
from bs4 import BeautifulSoup
import time

# --- get page ---

link = 'http://oldnavy.gap.com/browse/category.do?cid=1035712&sop=true'

#driver = webdriver.PhantomJS() # deprecated
driver = webdriver.Firefox()
driver.get(link)
time.sleep(3)

# --- scrolling ---

#size = driver.get_window_size()
#print(size)
#window_height = size['height']
#print('window_height:', window_height) # webpage + toolbars + border

# https://stackoverflow.com/questions/1248081/how-to-get-the-browser-viewport-dimensions

# this may give too big value because it includes scrollbar's height (ie. 962 = 950+22)
#viewport_height = driver.execute_script('return window.innerHeight;')
#print('viewport_height:', viewport_height)

# this gives correct value without scrollbar (ie. 950)
viewport_height = driver.execute_script('return document.documentElement.clientHeight;')
print('viewport_height:', viewport_height)

y = 0  # position to scroll

# at start it has to bigger then `y` to run `while y < page_height:`
page_height = 1 
#page_height = driver.execute_script('return document.body.scrollHeight;')

while y < page_height:
    y += viewport_height  # move only visible height
    print('y:', y, 'page_height:', page_height)

    # scroll
    driver.execute_script(f'window.scrollTo(0, {y});')

    # browser may need time to update page
    time.sleep(0.5)

    # get page height (it can change when JavaScript adds elements)
    page_height = driver.execute_script('return document.body.scrollHeight;')

# --- get data with BeautifulSoup ---

base_url = 'http://www.oldnavy.com'

html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')

all_divs = soup.find_all('div', class_='product-card')  # new layout
print('len(all_divs):', len(all_divs))

#for div in all_divs:
#    link = div.find('a')
#    print(link.text)
#    print(base_url + link['href'])

# --- get data with Selenium ---

all_products  = driver.find_elements_by_class_name('product-card')
print('len(all_products):', len(all_products))

for product in all_products:
    link = product.find_element_by_tag_name('a')
    print(link.text)
#   print(base_url + link['href'])
    

