
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

def test0():
    elements = driver.find_elements_by_xpath("//strong")
    for item in elements:
        print(item.text)

    print('---')

    item = driver.find_element_by_xpath("//strong[contains(text(), 'cubic')]")
    print(item.text)

def test1a():
    from selenium.webdriver.common.action_chains import ActionChains

    actions = ActionChains(driver)
    element = driver.find_element_by_xpath("//div[contains(@class,'MuiTypography-body1')][last()]//div")
    actions.move_to_element(element).build().perform()
    text = element.text
    print(text)
    
def test1b():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    text = driver.find_element_by_xpath("//div[contains(@class,'MuiTypography-body1')][last()]//strong").text
    print(text)
    
def test2():
    from bs4 import BeautifulSoup
    import re
    soup = BeautifulSoup(driver.page_source, "html.parser")
    soup.find_all(string=re.compile(r"\d+ cubic meters"))
    
def test3():
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

#test0()
#test1a()
#test1b()
#test2()
test3()
