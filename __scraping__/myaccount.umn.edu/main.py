#!/usr/bin/env python3

# date: 2020.02.26
# https://stackoverflow.com/questions/60406035/how-to-scrape-the-details-from-a-website-based-on-the-details-in-spread-sheet

# https://pastebin.com/evjdtpuA
# https://pastebin.com/J1UaYVzt

import selenium.webdriver
        
def scrape1(name):        
    url = 'https://myaccount.umn.edu/lookup?SET_INSTITUTION=UMNTC&type=name&campus=a&role=any&CN='

    driver = selenium.webdriver.Firefox()
    driver.get(url)
              
    driver.find_element_by_xpath('//input[@name="CN"]').send_keys(name)
    driver.find_element_by_xpath('//input[@type="submit"]').click()

    items = driver.find_elements_by_xpath('//table[@class="result__single-person"]//a')
    for item in items:
        print(item.text)
    
def scrape2(name):        
    url = 'https://myaccount.umn.edu/lookup?SET_INSTITUTION=UMNTC&type=name&campus=a&role=any&CN='

    driver = selenium.webdriver.Firefox()
    driver.get(url + name.replace(' ', '+'))
              
    items = driver.find_elements_by_xpath('//table[@class="result__single-person"]//a')
    for item in items:
        print(item.text)
    
# --- main ---                                                      

scrape1("Austin Westberg")    

scrape2("Austin Westberg")
