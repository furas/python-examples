# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.08.11
# [web scraping - Python - Xpath with module requests_html to get value of "a href" - Stack Overflow](https://stackoverflow.com/questions/73309271/python-xpath-with-module-requests-html-to-get-value-of-a-href/)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#import time

url = 'https://www.maison-objet.com/en/paris/les-exposants'

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get(url)
#time.sleep(5)

all_items = driver.find_elements(By.XPATH, '//*[@class="descBloc"]/h3/a')
print('len(all_items):', len(all_items))

for item in all_items:
    print('text:', item.text)
    print('url :', item.get_attribute('href'))
    print('---')

