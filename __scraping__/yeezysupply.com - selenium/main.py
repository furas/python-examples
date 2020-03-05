#!/usr/bin/env python3

# date: 2020.02.27
# 

import selenium
import selenium.webdriver
import time

options = selenium.webdriver.chrome.options.Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument("--headless")

driver = selenium.webdriver.Chrome(options=options)

driver.get("https://www.yeezysupply.com")
time.sleep(2)

all_articles = driver.find_elements_by_xpath('//div[@class="main___2aRHM"]//article')

for article in all_articles:
    for i, p in enumerate(article.find_elements_by_xpath('.//p'), 1):
        print(i, p.text)
    print('---')
