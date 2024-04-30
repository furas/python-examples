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

# --- first get all HREF as srtings ---

data = []

for index, div in enumerate(divs):
    text = div.text.strip()
    
    if not text:
        print(f'{index} >>>  --- empty ---')
        continue

    url = div.find_element('xpath', './/a').get_attribute('href')
    print(f'{index} >>>', text)
    
    data.append( (text, url) ) 

# --- next visit all pages (wiithout going back to main page) ---

print('len(data):', len(data))
    
for index, (text, url) in enumerate(data):

    print(f'{index} >>>', text)
    
    driver.get(url)
    time.sleep(2)
    
    contacts = driver.find_elements('xpath', '//*[@id="cityDirectoryDepartmentDetails"]/tbody/tr')        
    for contact in contacts:
        print('  contact:', contact.text)

    # it doesn't need to go back to main page
    
input('Press ENTER to close')
