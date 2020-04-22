#!/usr/bin/env python3

# date: 2020.03.30

import selenium.webdriver
        
url = 'https://www.amazon.com/international-sales-offers/b/?ie=UTF8&node=15529609011&ref_=nav_cs_gb_intl'

driver = selenium.webdriver.Firefox()
driver.get(url)

for x in range(10):
    deal = driver.find_element_by_id('100_dealView_' + str(x))
    
    image = deal.find_element_by_id('dealImage')
    print('href:', image.get_attribute('href'))

    title = deal.find_element_by_id('dealTitle')
    print('title:', title.text)
    
    price = deal.find_element_by_xpath('.//span[contains(@class, "dealPriceText")]')
    print('price:', price.text)
    
    print('---')
