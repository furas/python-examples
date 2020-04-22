#!/usr/bin/env python3

# date: 2020.04.19
# https://stackoverflow.com/questions/61298422/extracting-specific-elements-in-a-table-with-selenium-in-python/

import selenium.webdriver
        
driver = selenium.webdriver.Firefox()

# --- video ---

url = 'https://fileinfo.com/filetypes/video'
driver.get(url)

all_items = driver.find_elements_by_xpath('//td/a')

for item in all_items:
    print(item.text)
    #print(item.get_attribute('href'))
    
# --- audio ---    
    
url = 'https://fileinfo.com/filetypes/audio'
driver.get(url)

all_items = driver.find_elements_by_xpath('//td/a')

for item in all_items:
    print(item.text)
    #print(item.get_attribute('href'))     
