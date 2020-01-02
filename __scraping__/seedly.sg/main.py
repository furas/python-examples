#!/usr/bin/env python3 

# date: 2020.01.02
# ???

# count stars 

from selenium import webdriver 

browser = webdriver.Firefox()

url = 'https://seedly.sg/reviews/p2p-lending/funding-societies'
browser.get(url)

star_count_list = []

rating_column = browser.find_elements_by_xpath('//div[contains(@class,"qr0ren-7 euifNX")]')

for row in rating_column:
    stars = row.find_elements_by_xpath('.//span[contains(@style,"width:100%")]')
    star_count_list.append(len(stars))

for i, e in enumerate(star_count_list, 1):
    print('{}. {}'.format(i, e))
