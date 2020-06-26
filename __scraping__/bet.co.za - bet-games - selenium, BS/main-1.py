
# date: 2020.06.26
# https://stackoverflow.com/questions/62586100/hidden-element-can-not-found-by-beautifulsoup/

import selenium.webdriver
from bs4 import BeautifulSoup
import time

driver = selenium.webdriver.Firefox()
driver.get("https://www.bet.co.za/bet-games/")

time.sleep(10)

all_iframes = driver.find_elements_by_tag_name('iframe')
print('len(all_iframes):', len(all_iframes))

for number, iframe in enumerate(all_iframes):
    print('--- iframe', number, '---')
    
    driver.switch_to.frame(iframe)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    samples = soup.find_all('div', {'class': 'game-result'})
    print('len(samples):', len(samples))

    for item in samples:
        print(item.get_text(separator=','))
    
    driver.switch_to.default_content()


import selenium.webdriver
import time

driver = selenium.webdriver.Firefox()
driver.get("https://www.bet.co.za/bet-games/")

time.sleep(10)

all_iframes = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(all_iframes[1])

samples = driver.find_elements_by_css_selector('div.game-result')
print('len(samples):', len(samples))

for item in samples:
    print(item.get_text(separator=','))

