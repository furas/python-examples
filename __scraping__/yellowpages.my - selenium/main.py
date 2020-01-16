#!/usr/bin/env python3

# date: 2020.01.16
# https://stackoverflow.com/questions/59762473/using-webdriver-in-beautifulsoup-for-web-scraping

from selenium import webdriver
import csv

MAX_PAGE_NUM = 5

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

with open('results.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Bussiness Name", "Phone Number", "Address"])

    for page_num in range(1, MAX_PAGE_NUM+1):
        #page_num = '{:03}'.format(page_num)
        url = 'https://www.yellowpages.my/listing/results.php?keyword=boutique&where=selangor&screen={}'.format(page_num)
        driver.get(url)
        for item in driver.find_elements_by_xpath('//div[@id="content_listView"]//li'):
            try:
                name = item.find_element_by_xpath('.//div[@class="cbp-vm-companytext"]').text
            except Exception as ex:
                #print('ex:', ex)
                name = item.find_element_by_xpath('.//a[@class="cbp-vm-image"]/img').get_attribute('alt')
                
            phone = item.find_element_by_xpath('.//div[@class="cbp-vm-cta"]//span[@data-original-title="Phone"]').text
            address = item.find_element_by_xpath('.//div[@class="cbp-vm-address"]').text
            address = address.split('\n')[-1]

            print(name, phone, address)
            csv_writer.writerow([name, phone, address])

