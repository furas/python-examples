
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.08.18
#
# title: How can I get the Changing Data Values from website with Beautiful Soup?
# url: https://stackoverflow.com/questions/68831680/how-can-i-get-the-changing-data-values-from-website-with-beautiful-soup/68832090#68832090

# [How can I get the Changing Data Values from website with Beautiful Soup?](https://stackoverflow.com/questions/68831680/how-can-i-get-the-changing-data-values-from-website-with-beautiful-soup/68832090#68832090)


from selenium import webdriver
import time
             
url = 'https://www.binance.com/tr/trade/BTC_USDT'  # PEP8: spaces around =

driver = webdriver.Firefox()
driver.get(url)

while True:
    try:
        #print(driver.title)
        print(driver.title.split(' ')[0].strip())
    except Exception as ex:
        print('Exception:', ex)
        
    time.sleep(5)
    
