#!/usr/bin/env python3

# date: 2016.11.24 (update: 2020.06.13)
# https://stackoverflow.com/questions/40777864/retrieving-all-information-from-page-beautifulsoup/

from selenium import webdriver
from bs4 import BeautifulSoup
import time

# --- get page ---

link = 'http://oldnavy.gap.com/browse/category.do?cid=1035712&sop=true'

#driver = webdriver.PhantomJS()
driver = webdriver.Firefox()
driver.get(link)

# --- scrolling ---

print(driver.get_window_size())

height = driver.execute_script('return document.body.scrollHeight')
print('height:', height)

scrollBy(x, y)

while True:
    # scroll
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
    
    # browser need time to update page
    time.sleep(2)
    
    # get new height
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    # if height did change then stop scrolling
    if new_height == height:
        break
        
    height = new_height
    print('height:', height)

driver.maximize_window()
time.sleep(2)

#print(size)
#driver.set_window_size(size['width'], height)
#size = driver.get_window_size()
#print(size)

# --- get data ---

base_url = 'http://www.oldnavy.com'

html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')

#driver.find_element_by_class_name

#all_divs = soup.find_all('div', class_='sp_sm spacing_small') 
all_divs = soup.find_all('div', class_='product-card')  # new layout

for div in all_divs:
    all_links = div.find_all('a')
    for link in all_links:
        print(base_url + link['href'])
