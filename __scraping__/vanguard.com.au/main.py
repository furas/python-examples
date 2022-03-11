# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.10
# [python - BeautifulSoup not working on this website - Stack Overflow](https://stackoverflow.com/questions/71418546/beautifulsoup-not-working-on-this-website/)

from selenium import webdriver
from selenium.webdriver.common.by import By
             
url = 'https://www.vanguard.com.au/personal/products/en/overview'

lists = []

driver = webdriver.Firefox()
driver.get(url)

title = driver.find_element(By.XPATH, '//h1[@class="heading2 gbs-font-vanguard-red"]')
print(title.text)

all_items = driver.find_elements(By.XPATH, '//a[@style="padding-bottom: 1px;"]')

for links in all_items:
    link_text = links.get_attribute('href')
    print(link_text)
    lists.append(link_text)


