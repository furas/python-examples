# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.30
# [html - unable to send information or click specific buttons on the website(selenium python) - Stack Overflow](https://stackoverflow.com/questions/72065094/unable-to-send-information-or-click-specific-buttons-on-the-websiteselenium-pyt/)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, TimeoutException
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

url = 'https://fred.stlouisfed.org/series/DGS10'

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)

time.sleep(5)

#max_range_button = driver.find_element(By.XPATH, '//*[@id="zoom-all"]')
#max_range_button.click()

range_search_bar = driver.find_element(By.XPATH, '//*[@id="input-cosd"]')
range_search_bar.clear()

range_search_bar.send_keys("1980-10-10")
range_search_bar.send_keys(Keys.ENTER) # u'\ue007')


time.sleep(5)
#download_10_button = driver.find_element(By.XPATH, '//*[@id="download-button"]/span')
download_10_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="download-button"]/span')))
download_10_button.click()

#time.sleep(2)
#download_csv_button = driver.find_element(By.XPATH, '//*[@id="download-data-csv"]')
download_csv_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="download-data-csv"]')))
download_csv_button.click()

