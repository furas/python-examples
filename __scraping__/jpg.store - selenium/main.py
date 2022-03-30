# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.26
# [python - How would I get all elements with a specific XPATH, get the lowest price among them, then get the title of it? [Using Selenium] - Stack Overflow](https://stackoverflow.com/questions/71624938/how-would-i-get-all-elements-with-a-specific-xpath-get-the-lowest-price-among-t/)

from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

url = "https://www.jpg.store/collection/cardano4speed?filters=%257B%2522engine%2522%253A%255B%2522v8%2520special%2520edition%2522%255D%257D"

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(url)

data = []

all_elements = driver.find_elements(By.XPATH, '//*[@id="asset-card"]')
for element in all_elements:
    title = element.find_element(By.XPATH, './/h4').text
    price = element.find_element(By.XPATH, './/span[@id="asset-price"]').text
    number = int(title.replace("CARdano4SPEED", ""))

    if number <= 1000:
        print('title:', title)
        print('price:', price)
        print('number:', number)
        print('---')
        data.append( [number, title, price] )

# ---

number, title, price = min(data)
print('min:', number, title, price)
