#!/usr/bin/env python3

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")

elements = driver.find_elements_by_xpath('//div[@class="quote"]')

for item in elements:
    print('text:', item.find_element_by_class_name('text').text[:20] + ' ...')
    print('author:', item.find_element_by_class_name('text').text)
    
    all_tags = item.find_elements_by_class_name('tag')
    print('tags:', ', '.join(tag.text for tag in all_tags))

    print('-----')
