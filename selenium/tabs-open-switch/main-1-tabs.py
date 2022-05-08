# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.05
# [selenium - How to Open 20+ window in chrome using webDriver (python) - Stack Overflow](https://stackoverflow.com/questions/71745733/how-to-open-20-window-in-chrome-using-webdriver-python/)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=ChromeDriverManager().install())

time.sleep(2)

driver.switch_to.new_window('tab')
driver.get("https://books.toscrape.com/")
tab1_id = driver.current_window_handle

time.sleep(2)

driver.switch_to.new_window('tab')
driver.get("https://quotes.toscrape.com/")
tab2_id = driver.current_window_handle

time.sleep(2)

driver.switch_to.window(tab1_id)

time.sleep(2)

driver.switch_to.window(tab2_id)

time.sleep(2)

driver.switch_to.window(tab1_id)

