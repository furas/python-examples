
# date: 2020.05.26
# https://stackoverflow.com/questions/61994836/bs4-web-scraping-searching-div-class/

import selenium.webdriver
        
url = 'https://www.google.com/search?q=titanic+movie'

driver = selenium.webdriver.Firefox()
driver.get(url)

item = driver.find_element_by_class_name('srBp4.Vrkhme')
print(item.text.strip())
        
