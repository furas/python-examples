#!/usr/bin/env python3

# date: 2020.01.06

import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get('https://books.toscrape.com')

all_items = driver.find_elements_by_class_name('product_pod')

data = []

for item in all_items:
    try:
        name = item.find_element_by_xpath('.//h3/a').get_attribute('title')
    except Exception as ex:
        #print('[Exception] name:', ex)
        name = ''
        
    try:    
        price = item.find_element_by_class_name('price_color').text.strip()
    except Exception as ex:
        #print('[Exception] price:', ex)
        price = ''

    # there is no class `other` on page so it will add `NAN`    
    try:    
        other = item.find_element_by_class_name('other').text.strip()
    except Exception as ex:
        #print('[Exception] other:', ex)
        other = 'NAN'

    data.append([name, price, other])

for row in data:
    print(row)
