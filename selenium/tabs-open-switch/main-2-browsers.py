# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.05
# [selenium - How to Open 20+ window in chrome using webDriver (python) - Stack Overflow](https://stackoverflow.com/questions/71745733/how-to-open-20-window-in-chrome-using-webdriver-python/)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
import time

# all browsers in separated variables - to have access to all browsers
# (`Chrome` closes previous browser when it assigns new browser to the same variable)
# (`Firefox` doesn't close previous browser)

all_drivers = []

for i in range(20):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #driver = webdriver.Firefox(executable_path=ChromeDriverManager().install())

    all_drivers.append(driver)

    driver.get("https://books.toscrape.com/")

