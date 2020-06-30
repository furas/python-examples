#!/usr/bin/env python3 

# date: 2019.11.24
# https://stackoverflow.com/questions/59019810/python-web-scraping-ahref-link-and-articles-not-showing-up-in-source-code

import selenium.webdriver
        
url = 'https://corporate.dow.com/en-us/news.html'
driver = selenium.webdriver.Firefox()
driver.get(url)

all_items = driver.find_elements_by_xpath('//ul[@class="results__list"]/li')
for item in all_items:
    print(item.find_element_by_xpath('.//h3').text)
    print(item.find_element_by_xpath('.//a').get_attribute('href'))
    print('---')

