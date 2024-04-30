#!/usr/bin/env python3

"""
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2024.04.30
# [Refresh page after double for loop, selenium with python - Stack Overflow](https://stackoverflow.com/questions/78405333/refresh-page-after-double-for-loop-selenium-with-python)
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.elizabethnj.org/Directory.aspx")
time.sleep(3)

divs = driver.find_elements('xpath', '//div[@class="topmenu"]/div')
print('len(divs):', len(divs))

#for index, div in enumerate(divs):
#    print(f'{index} >>>', div.text)
    
for index in range(len(divs)):

    divs = driver.find_elements('xpath', '//div[@class="topmenu"]/div')
    div = divs[index]
    
    text = div.text.strip()
    
    if not text:
        print(f'{index} >>>  --- empty ---')
        continue
        
    print(f'{index} >>>', div.text)
    div.click()
    time.sleep(2)
    
    contacts = driver.find_elements('xpath', '//*[@id="cityDirectoryDepartmentDetails"]/tbody/tr')        
    for contact in contacts:
        print('  contact:', contact.text)

    print('<<< back')
    # ... some pages don't have contacts and link is in `[2]` instead of `[3]`        
    #back = driver.find_element('xpath', '//*[@id="CityDirectoryLeftMargin"]/div[3]/span')
    #back.click()
    # ... or ...    
    driver.back()
    # ... or ...
    #driver.get("https://www.elizabethnj.org/Directory.aspx")

    time.sleep(2)

input('Press ENTER to close')
