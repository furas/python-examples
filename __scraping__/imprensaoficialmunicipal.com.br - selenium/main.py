
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.11
#
# title: Selenium Python - Stale Element Reference Exception
# url: https://stackoverflow.com/questions/69921027/selenium-python-stale-element-reference-exception/69930616#69930616

# [Selenium Python - Stale Element Reference Exception](https://stackoverflow.com/questions/69921027/selenium-python-stale-element-reference-exception/69930616#69930616)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def info(driver, delay=5):
    next_page = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Pagination"]/a[@class="next"]')))

    all_elements = driver.find_elements_by_xpath('//*[@id="jornal"]/li[@class="lista"]')
    
    for item in all_elements:
        text = item.text 
        href = item.find_element_by_xpath('a').get_attribute('href')
        print(text)
        print('href:', href)
        print('---')
    
    next_page.click()
    sleep(delay)

def page(driver):
    for _ in range(5): 
        #info(driver)
        info(driver, 2)

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.imprensaoficialmunicipal.com.br/sao_joaquim_da_barra")
    driver.implicitly_wait(10)

    page(driver)

if __name__ == '__main__':
    main()


