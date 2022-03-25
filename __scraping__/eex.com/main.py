# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.11
# [javascript - Selenium Python: Cannot click on class="mv-button-base mv-hyperlink-button" - Stack Overflow](https://stackoverflow.com/questions/71442966/selenium-python-cannot-click-on-class-mv-button-base-mv-hyperlink-button/71443746#71443746)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.firefox import GeckoDriverManager

url = 'https://www.eex.com/de/marktdaten/strom/futures#%7B%22snippetpicker%22%3A%22EEX%20German%20Power%20Future%22%7D'

##driver = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox()

driver.get(url)
time.sleep(3) 

abrechnungspreis = driver.find_element(By.XPATH, '//div[@id="snippet-8"]//table[1]//tr[1]/td[4]')
price = abrechnungspreis.text

header = driver.find_element(By.XPATH, '//div[@id="symbolheader_pfpde"]')

input_date = header.find_element(By.XPATH, './/input')
date = input_date.get_attribute('value')
print(f'Tages Abrechnungspreis vom {date} ist {price}')

# delete old date and put yesterday

input_date.send_keys(Keys.BACKSPACE*5)
input_date.send_keys("03-09")
input_date.send_keys(Keys.ENTER)

#input_date.clear()
#input_date.send_keys("2022-03-01")
#input_date.send_keys(Keys.ENTER)

time.sleep(3)  # javascript may need time to update HTML

# find again after updating HTML 
abrechnungspreis = driver.find_element(By.XPATH, '//div[@id="snippet-8"]//table[1]//tr[1]/td[4]')
price = abrechnungspreis.text

date = input_date.get_attribute('value')
print(f'Tages Abrechnungspreis vom {date} ist {price}')

# --- Jahr ---

button_Jahr = header.find_element(By.XPATH, './/div[text()="Jahr"]')
driver.execute_script('arguments[0].click()', button_Jahr)
time.sleep(3)  # javascript may need time to update HTML

# find again after updating HTML 
abrechnungspreis = driver.find_element(By.XPATH, '//div[@id="snippet-8"]//table[1]//tr[1]/td[4]')
price = abrechnungspreis.text

print(f'Jahres Abrechnungspreis vom {date} ist {price}')
time.sleep(10)

#driver.quit()


