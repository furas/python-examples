#!/usr/bin/env python3 

# date: 2019.12.14
# 

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains
    
import time
url = 'https://shopee.com.my/search?keyword=mattress'

driver = selenium.webdriver.Firefox()
driver.get(url)
time.sleep(1)

# select language
driver.find_element_by_xpath('//div[@class="language-selection__list"]/button').click()
time.sleep(3)

# scroll few times to load all items 
for x in range(10):
    driver.execute_script("window.scrollBy(0,300)")
    time.sleep(0.1)

# get all links
all_items = driver.find_elements_by_xpath('//a[@data-sqe="link"]')
print('len:', len(all_items))

all_urls = []

for item in all_items:
    url = item.get_attribute('href')
    all_urls.append(url)
    print(url)
    
# use links

#for item in all_urls:
#    driver.get(url)
