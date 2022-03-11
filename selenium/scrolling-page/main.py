# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.11
# [python - I can't get all product from page website ( scraping aliexpress using pyhon selenium) - Stack Overflow](https://stackoverflow.com/questions/71422193/i-cant-get-all-product-from-page-website-scraping-aliexpress-using-pyhon-sele/71433142#71433142)

from selenium import webdriver  
from lxml import html 
from time import sleep
import csv


#driver = webdriver.Edge(executable_path=r"C:/Users/OUISSAL/Desktop/wscraping/XEW/scraping/codes/msedgedriver")
driver = webdriver.Firefox()

url = 'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=bluetooth+earphones&ltype=wholesale&SortType=default&page={}'
    
with open ("data.csv", "w", encoding="utf-8") as csvfile:

    wr = csv.writer(csvfile)
    wr.writerow(["Title","Price", "Currency", "Reviews", "Number of orders"])

    for page_nb in range(1, 4):
        print('---', page_nb, '---')
        
        driver.get(url.format(page_nb))
        sleep(2)
        
        # jump to the end
        #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
        # scroll partially
        
        current_offset = 0
        while True:
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            sleep(.5)  # JavaScript has time to add elements
            
            new_offset = driver.execute_script("return window.pageYOffset;")
            #print(new_offset, current_offset)
            if new_offset <= current_offset:
                break
                
            new_offset = current_offset
        
        sleep(3)
        
        tree = html.fromstring(driver.page_source)
        
        results = []
        
        for product in tree.xpath('//div[@class="JIIxO"]//a'):
            title = product.xpath('.//h1/text()')
            #print('[DEBUG] title:', title)
            
            if title:
                title = title[0]
                #print('[DEBUG] title:', title)
                
                price = product.cssselect('div.mGXnE._37W_B span')
                price = [x.text for x in price]

                # for `$ 35.00`
                currency = price[0]
                price = ''.join(price[1:])
                
                # for `35.00 zł`
                #currency = price[-1]
                #price = ''.join(price[:-1])
                
                #print('[DEBUG] price:', price)
                #print('[DEBUG] currency:', currency)

                review = product.xpath('.//span[@class="eXPaM"]/text()')
                if review:
                    review = review[0]
                else:
                    review = ''
                #print('[DEBUG] review:', review)
                    
                nb_sold = product.xpath('.//span[@class="_1kNf9"]/text()')
                if nb_sold:
                    nb_sold = nb_sold[0]
                else:
                    nb_sold = ''
                #print('[DEBUG] nb_sold:', nb_sold)
                    
                row = [title, price, currency, review, nb_sold]
                results.append(row)
                #print('[DEBUG] row:', row)
            
        print('len(results):', len(results))
        wr.writerows(results)  

driver.close()
