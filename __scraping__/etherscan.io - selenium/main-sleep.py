
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.06
#
# title: Can't get size of elements and the classes in selenium
# url: https://stackoverflow.com/questions/69458094/cant-get-size-of-elements-and-the-classes-in-selenium/69459487#69459487

# [Can't get size of elements and the classes in selenium](https://stackoverflow.com/questions/69458094/cant-get-size-of-elements-and-the-classes-in-selenium/69459487#69459487)

from selenium import webdriver
import time

url = 'https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52#readContract'

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get(url)

print('wait for: frame')
time.sleep(5)  # it needs some time to add elements on page
frame = driver.find_element_by_id('readcontractiframe')
driver.switch_to.frame(frame)

print('wait for: Expand all')
#time.sleep(0.5)  # it works without sleep 
driver.find_element_by_xpath('//a[text()="[Expand all]"]').click()

print('wait for: readCollapse1')
time.sleep(0.5)  # it needs some to expand all

for i in range(1, 9):
    print('---', i, '---')
    print(driver.find_element_by_id(f"readHeading{i}").text)
    print(driver.find_element_by_id(f"readCollapse{i}").text)

