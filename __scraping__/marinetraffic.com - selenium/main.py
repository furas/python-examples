
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.06.23
#
# title: Get element text with a partial string match using selenium (python)
# url: https://stackoverflow.com/questions/68106875/get-element-text-with-a-partial-string-match-using-selenium-python/

from selenium import webdriver
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

url = "https://www.marinetraffic.com/en/ais/details/ships/imo:9854612"
driver.get(url)
time.sleep(3)

from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
elements = driver.find_elements_by_xpath("//span[@class='lazyload-wrapper']")

for number, item in enumerate(elements, 1):
    print('--- number', number, '---')
    #print('--- before ---')
    #print(item.text)
    
    actions.move_to_element(item).perform()
    time.sleep(0.1)
    
    #print('--- after ---')
    #print(item.text)
    
    try:
        strong = item.find_element_by_xpath("//strong[contains(text(), 'cubic')]")
        print(strong.text)
        break
    except Exception as ex:
        #print(ex)
        pass

