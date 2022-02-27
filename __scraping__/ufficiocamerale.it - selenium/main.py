# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.24
# [python - Insert a code, click on a button and extract the result with Scrapy - Stack Overflow](https://stackoverflow.com/questions/71251118/insert-a-code-click-on-a-button-and-extract-the-result-with-scrapy/)

from selenium import webdriver
import time

url =  'https://www.ufficiocamerale.it/'

driver = webdriver.Firefox()
driver.get(url)

time.sleep(5)  # JavaScript needs time to load code

item = driver.find_element_by_xpath('//form[@id="formRicercaAzienda"]//input[@id="search_input"]')
#item = driver.find_element_by_id('search_input')
item.send_keys('06655971007')

time.sleep(1)

button = driver.find_element_by_xpath('//form[@id="formRicercaAzienda"]//p//button[@type="submit"]')
button.click()

time.sleep(5)  # JavaScript needs time to load code

item = driver.find_element_by_tag_name('h1')
print(item.text)
print('---')

all_items = driver.find_elements_by_xpath('//ul[@id="first-group"]/li')
for item in all_items:
    if '@' in item.text:
        print(item.text, '<<< found email:', item.text.split(' ')[1])
    else:
        print(item.text)
print('---')

"""
DATI DELLA SOCIETÀ - ENEL ENERGIA S.P.A.
---
Partita IVA: 06655971007 - Codice Fiscale: 06655971007
Rag. Sociale: ENEL ENERGIA S.P.A.
Indirizzo: VIALE REGINA MARGHERITA 125 - 00198 - ROMA
Rea: 1150724
PEC: enelenergia@pec.enel.it <<< found email: enelenergia@pec.enel.it
Fatturato: € 13.032.695.000,00 (2020)
ACQUISTA BILANCIO
Dipendenti : 1666 (2021)
---
"""

