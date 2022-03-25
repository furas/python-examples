# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.11
# [Scraping Investopedia using selenium python - Stack Overflow](https://stackoverflow.com/questions/71443533/scraping-investopedia-using-selenium-python/71444720#71444720)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
import time

# --- functions ---  # PEP8: `lower_case_names`

def login():
    driver.get(r'https://www.investopedia.com/simulator/home.aspx')
    driver.implicitly_wait(10)
    
    driver.find_element(By.ID, 'username').send_keys('xxx@xxx.com')
    time.sleep(0.5)
    
    driver.find_element(By.ID, 'password').send_keys('hello-world')
    time.sleep(0.5)
    
    driver.find_element(By.ID, 'login').click()

def get_trade_page():
    url = 'https://www.investopedia.com/simulator/trade/stocks'
    driver.get(url)

def set_stock(ticker):
    driver.find_element(By.XPATH, '//input[@placeholder="Look up Symbol/Company Name"]').send_keys(ticker)
    
    #driver.find_element(By.XPATH, '//div[@role="option"]').click()
    
    option = driver.find_element(By.XPATH, '//div[@role="option"]')
    driver.execute_script('arguments[0].click()', option)

# --- main ---

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

login()
get_trade_page()
set_stock('hvt')

#driver.close()

