#!/usr/bin/env python3 

# date: 2019.11.30
# https://stackoverflow.com/questions/59113577/selenium-in-python-finding-an-element-via-relative-xpath

import selenium.webdriver

driver = selenium.webdriver.Firefox()

driver.get('https://travel.padi.com/s/liveaboards/caribbean/')

all_cards = driver.find_elements_by_xpath('//div[@class="boat search-page-item-card "]')

for card in all_cards:
    title = card.find_element_by_xpath('.//a[@class="shop-title"]/span')
    desc  = card.find_element_by_xpath('.//p[@class="shop-desc-text"]')
    price = card.find_element_by_xpath('.//p[@class="cur-price"]/strong/span')

    print('title:', title.text)
    print('desc:',  desc.text)
    print('price:', price.text)
                              
    all_dates = card.find_elements_by_css_selector('.cell.date')
    
    for date in all_dates:
        day, month = date.find_elements_by_tag_name('span')
        print('date:', day.text, month.text)
        
    print('---')
