
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.06
#
# title: Can't get size of elements and the classes in selenium
# url: https://stackoverflow.com/questions/69458094/cant-get-size-of-elements-and-the-classes-in-selenium/69459487#69459487

# [Can't get size of elements and the classes in selenium](https://stackoverflow.com/questions/69458094/cant-get-size-of-elements-and-the-classes-in-selenium/69459487#69459487)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52#readContract'

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get(url)

wait = WebDriverWait(driver, 30)

print('wait for: frame')
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'readcontractiframe')))

print('wait for: Expand all')
# it need sleep(1) - doesn't work with sleep(0.5)
#item = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="[Expand all]"]')))
#time.sleep(1)  # it still needs some time before click

# it need sleep(0.3) - doesn't work with sleep(0.2)
item = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="[Expand all]"]')))
time.sleep(0.3)  # it still needs some time before click

item.click()
#driver.find_element_by_xpath('//a[text()="[Expand all]"]').click()

print('wait for: readCollapse1')
wait.until(EC.visibility_of_element_located((By.ID, 'readCollapse1')))

for i in range(1, 9):
    print('---', i, '---')
    print(driver.find_element_by_id(f"readHeading{i}").text)
    print(driver.find_element_by_id(f"readCollapse{i}").text)


