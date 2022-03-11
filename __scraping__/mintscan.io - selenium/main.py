# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.10
# [AttributeError: 'NoneType' object has no attribute 'find' Web Scraping Python - Stack Overflow](https://stackoverflow.com/questions/71428976/attributeerror-nonetype-object-has-no-attribute-find-web-scraping-python/)

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, TimeoutException
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

url = "https://www.mintscan.io/cosmos/validators/cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw"

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(url)

#status = driver.find_element(By.XPATH, '//div[@class="ValidatorInfo_statusBadge__PBIGr"]')
wait = WebDriverWait(driver, 10)
status = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ValidatorInfo_statusBadge__PBIGr"]')))
print(status.text)

