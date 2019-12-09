#!/usr/bin/env python3 

# date: 2019.12.09
# ?

from selenium import webdriver

url = 'https://www.google.com/finance'
#driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get(url)

all_tables = driver.find_elements_by_css_selector('.mod')

for table in all_tables[1:]:
    print('====== TABLE ======')
    try:
        for item in table.find_elements_by_css_selector('a'):
            divs = item.find_elements_by_css_selector('div > div > div')
            spans = item.find_elements_by_css_selector('div > div > span')
            
            symbol = divs[0]
            volume = spans[0] 
            name = spans[1] 
            price = spans[2]
            
            print('Symbol:', symbol.text)
            print('Volume:', volume.text)
            print('Name:', name.text)
            print('Price:', price.text)
            
            print('---')
    except Exception as ex:
        print('EX:', ex)
    
