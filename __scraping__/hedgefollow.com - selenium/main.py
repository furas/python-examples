#!/usr/bin/env python3

# date: 2020.05.25
# https://stackoverflow.com/questions/62003463/web-scraping-hedge-fund-data-with-beautifulsoup

import selenium.webdriver
import time

url = 'https://hedgefollow.com/funds/Duquesne+Family+Office'

driver = selenium.webdriver.Firefox()
driver.get(url)

time.sleep(3)

table = driver.find_element_by_id('dgtopHolders')

print('--- headers ---')

row = table.find_elements_by_tag_name('tr')[0]
for cell in row.find_elements_by_tag_name('th'):
    print(cell.text)
    
print('--- data ---')

for row in table.find_elements_by_tag_name('tr')[1:]:
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)
    print('---')

