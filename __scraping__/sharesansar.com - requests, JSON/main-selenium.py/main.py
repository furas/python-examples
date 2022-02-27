from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import time

url = 'https://www.sharesansar.com/company/shl'

cdm = ChromeDriverManager().install()
driver = webdriver.Chrome(cdm)

driver.maximize_window()
driver.get(url)
time.sleep(10)

data = []

driver.find_element_by_link_text('Price History').click()
time.sleep(3)

select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="myTableCPriceHistory_length"]'))))
select.select_by_visible_text("50")

while True:
    
    soup = BeautifulSoup(driver.page_source, 'lxml')

    tables = soup.select('#myTableCPriceHistory tbody tr')

    for table in tables:
        _open = table.select_one('td:nth-child(3)').text
        high = table.select_one('td:nth-child(4)').text
        low = table.select_one('td:nth-child(5)').text
        close = table.select_one('td:nth-child(6)').text

        print(f"Opening: {_open}\nHigh: {high}\nLow: {low}\n")

    print("-" * 85)
    
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="paginate_button next"]'))).click()
        print("Clicked on Next Page »")
        time.sleep(5)  # page needs time to load new data
    except TimeoutException:
        print("No more Next Page »")
        break
        
driver.quit()
