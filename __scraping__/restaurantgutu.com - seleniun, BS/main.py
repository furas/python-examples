# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.23
# [python - Create a webscraper with loop to search links - Stack Overflow](https://stackoverflow.com/questions/71239570/create-a-webscraper-with-loop-to-search-links/71240820#71240820)

from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import csv

try:
    restlist = []

    #driver_service = Service(executable_path="C:/webdrivers/chromedriver.exe")
    #driver = webdriver.Chrome(service=driver_service)
    driver = webdriver.Firefox()
    
    driver.get('https://restaurantguru.com/restaurant-Poland-t1')

    print('[DEBUG] productlist ...')
    #soup = BeautifulSoup(driver.page_source, 'lxml')
    #productlist = soup.find_all('div', class_='wrapper_info')
    productlist = driver.find_elements_by_xpath('//div[@class="wrapper_info"]')
    
    #print(productlist)

    print('[DEBUG] productlinks ...')
    productlinks = []
    for item in productlist:
        #for link in item.find_all('a', href=True):
        #    productlinks.append(link['href'])
        for link in item.find_elements_by_xpath('.//a[@href]'):
            productlinks.append(link.get_attribute('href'))

    print('len(productlinks):', len(productlinks))

    for number, link in enumerate(productlinks, 1):
        print('---', number, '---')
        
        print('[DEBUG] link:', link)
        
        driver.get(link)
        
        print('[DEBUG] soup ...')
        #soup = BeautifulSoup(driver.page_source, 'lxml')

        print('[DEBUG] name ...')
        #name = soup.find('h1', class_='notranslate').text.strip()
        #print(name)
        name = driver.find_element_by_xpath('//h1[@class="notranslate"]').text.strip()
        print(name)

        print('[DEBUG] address ...')
        #address = soup.find('div', class_='address').find('div', class_=False).text.strip()
        #print(address)
        address = driver.find_element_by_xpath('//div[@class="address"]/div[2]').text.strip()
        print(address)

        print('[DEBUG] website ...')
        try:
            #website = soup.find('div', class_='website').find('a').text #get('href')
            #print(website)
            website = driver.find_element_by_xpath('//div[@class="website"]//a').text #get('href')
            print(website)
        except Exception as ex:
            print('[DEBUG] Exception:', ex)
            website = ''
            print(website)
        
        rest = {
            'name': name,
            'website': website,
            'address': address,
        }

        print('[DEBUG] rest ...')
        print(rest)

        restlist.append(rest)
        
    print(restlist)
    
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:    
    driver.quit()

    # open only once
    with open('output.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['name', 'website', 'address'])
        csv_writer.writeheader()
        csv_writer.writerows(restlist)

