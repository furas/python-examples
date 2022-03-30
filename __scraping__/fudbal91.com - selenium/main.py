# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.30
# [web scraping - Xpath select with two conditions - Stack Overflow](https://stackoverflow.com/questions/71670362/xpath-select-with-two-conditions)

from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

url = 'https://www.fudbal91.com/previews/2022-03-30'

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)

time.sleep(2)

all_items = driver.find_elements(By.XPATH, '//a[not(contains(@class,"inprogress"))]//span[contains(@itemprop,"name")]')
print('len(all_items):', len(all_items))
for item in all_items:
    print(item.text)

 
