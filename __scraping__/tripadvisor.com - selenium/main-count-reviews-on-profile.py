# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.11

from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

url = 'https://www.tripadvisor.com/Profile/yes2luvtravel?tab=reviews'
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)

time.sleep(3)

# accept cookies
buttons = driver.find_elements(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
if buttons:
    print('click Accept')
    buttons[0].click()

# click `Show More`
while True:
    time.sleep(3)
    buttons = driver.find_elements(By.XPATH, '//div[@id="content"]//button')
    if not buttons:
        break
    print('click button')
    buttons[0].click()
    
all_items = driver.find_elements(By.XPATH, '//div[@id="content"]//div[contains(@class, "section")]')
print('len(all_items):', len(all_items))

 

