# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.25

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://messari.io/governor/daos'

options = Options()
options.headless = True
options.add_argument("--window-size=1920, 1200")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get('https://messari.io/governor/daos')

try:
    matches = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "h4")))
    
    #matches = driver.find_elements(By.TAG_NAME, "h4")
    
    for match in matches:
        if match.text:
            print(match.text)
finally:
    driver.quit()
