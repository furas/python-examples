# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.02.06
# https://stackoverflow.com/questions/66074066/clicking-two-consecutive-buttons-while-scraping-a-website-with-selenium-in-pytho

import time
from selenium import webdriver

url   = 'https://www.morningstar.com/etfs/xnas/vnqi/portfolio'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)

country = driver.find_element_by_xpath('//input[@value="Country"]')
country.click()

time.sleep(1)
next_page = driver.find_element_by_xpath('//a[@aria-label="Go to Next Page"]')

while True:
    
    # get data
    table_rows = driver.find_elements_by_xpath('//table[@class="sal-country-exposure__country-table"]//tr')
    for row in table_rows[1:]:  # skip header 
        elements = row.find_elements_by_xpath('.//span')  # relative xpath with `.//`
        print(elements[0].text, elements[1].text, elements[2].text)

    # check if there is next page
    disabled = next_page.get_attribute('aria-disabled')
    #print('disabled:', disabled)
    if disabled:
        break

    # go to next page        
    next_page.click()
    
    time.sleep(1)

