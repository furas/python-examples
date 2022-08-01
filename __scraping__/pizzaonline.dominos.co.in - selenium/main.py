# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.08.01
# [python - Web scraping gives outdated values - Stack Overflow](https://stackoverflow.com/questions/73184566/web-scraping-gives-outdated-values?noredirect=1#comment129269669_73184566)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

import time

# start web browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# get source code
driver.get('https://pizzaonline.dominos.co.in/menu')

# it would need to scroll page by page to get images
#driver.execute_script("var scrollingElement = (document.scrollingElement || document.body); scrollingElement.scrollTop = scrollingElement.scrollHeight;")

time.sleep(3)

html = driver.page_source

all_items = driver.find_elements(By.XPATH, '//div[@class="itm-wrppr"]/div')
print('len(all_items):', len(all_items))

for number, item in enumerate(all_items, 1):
    name = item.get_attribute('data-label')
    # get `data-src` instead of `src` because it uses `lazy-loading`
    image = item.find_element(By.XPATH, './/div[@class="img-cvr"]//img').get_attribute('data-src')  
    print(f' {number:3} | {name:60} | {image}')

# close web browser
driver.close()

