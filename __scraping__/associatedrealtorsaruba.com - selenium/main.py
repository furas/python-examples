#!/usr/bin/env python3

# date: 2020.01.07
# https://stackoverflow.com/questions/59632031/how-to-extract-href-when-href-element-is-a-hyperlink?noredirect=1#comment105434826_59632031

import selenium.webdriver
        
url = 'https://associatedrealtorsaruba.com/index.php?option=com_ezrealty&Itemid=11&task=results&cnid=0&custom7=&custom8=&parking=&type=0&cid=0&stid=0&locid=0&minprice=&maxprice=&minbed=&maxbed=&min_squarefeet=&max_squarefeet=&bathrooms=&sold=0&lug=0&featured=0&custom4=&custom5=&custom6=&postcode=&radius=&direction=DEFAULT&submit=Search'

driver = selenium.webdriver.Firefox()
driver.get(url)

while True:

    all_items = driver.find_elements_by_xpath('//span[@class="h3"]')
    for item in all_items:
        print(item.text)
        
    try:    
        # find link to next page
        all_items = driver.find_element_by_xpath('//a[@title="next page"]')

        # click link to load next page
        all_items.click()
    except Exception as ex:
        print('ex:', ex)
        break
