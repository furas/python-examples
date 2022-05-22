from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time
#from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# ---

#original webscraping code to get the names of locations from page 1

url = 'https://autochek.africa/en/ng/fix-your-car/service/scheduled-car-service'
driver.get(url)

#xpath_get_locations = r'/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div/form/div[7]/div/label'
xpath_get_locations = '//label[text()="Drop-off at Autochek location"]'
driver.find_element(BY.XPATH, xpath_get_locations).click()

# ---

all_locations = []

While True:
    
    # --- get locations on page
    
    #time.sleep(1) # sometimes `JavaScript` may need time to add new items

    #items = soup.find_all('div', {'class': 'jsx-1642469937 state'})
    items = driver.find_elements(BY.XPATH, '//div[@class="jsx-1642469937 state"]')

    #soup = BeautifulSoup(driver.page_source, 'html.parser')

    locations = [i.text for i in items]

    print(locations)
    print('-------')

    all_locations += locations
    
    # --- find button `next >` and try to click it 
    
    #xpath_find_next_button = r'/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/ul/li[13]'
    xpath_find_next_button = '//span[@class="jsx-3027088489 next"]'

    try:
        driver.find_element(BY.XPATH, xpath_find_next_button).click()
    except:
        break # exit loop
    
# ---



