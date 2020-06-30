#!/usr/bin/env python3

# date: 2020.02.26
# 

import selenium.webdriver
        
def scrape(last_name, first_name):        
    url = 'https://directory.apps.upenn.edu/directory/jsp/fast.do'
    
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    
    inputs = driver.find_elements_by_tag_name('input')

    #for item in inputs:
    #    print(item.get_attribute('name'))
              
    inputs[2].send_keys(last_name)
    inputs[3].send_keys(first_name)
    
    driver.find_element_by_class_name('submitButton').click()

    items = driver.find_elements_by_xpath('//tr[@class="lookupbody"]//a[@class="linkText"]')
    for item in items:
        print(item.text)

# --- main ---
                                        
scrape("Tomasco", "Lauretta")
#scrape("Austin", "Westberg")
