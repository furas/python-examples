
# author: https://blog.furas.pl
# date: 2020.07.09
# https://stackoverflow.com/questions/62805708/how-can-i-get-a-data-from-specific-text-in-div-class-using-a-beautifulsoup/

import selenium.webdriver

url = "https://www.douglascollege.ca/programs-courses/catalogue/programs"

driver = selenium.webdriver.Firefox()
driver.get(url)

all_div = driver.find_elements_by_xpath('//div[contains(@class, "ui-accordion-content")]')

for div in all_div:
    all_items = div.find_elements_by_tag_name("a")

    for item in all_items:
        print(item.get_attribute('textContent'))
        #print(item.text) # doesn't work for hidden element
