from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
import datetime as dt
import pandas as pd

# - before loop -

all_rows = []

#driver = webdriver.Firefox(executable_path='C:\\Downloads\\webdrivers\\geckodriver.exe')
driver = webdriver.Firefox()

for page in range(1):
    print('--- page:', page, '---')
    
    url = f'https://www.flipkart.com/search?q=sony+headphones&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=sony+headphones&requestId=ad797917-16ae-401e-98df-1c79a43d40c3&as-backfill=on&page={page}'

    driver.get(url)
    time.sleep(3)  

    soup = BS(driver.page_source, 'html5lib')

    all_containers = soup.find_all('div', {'class': '_4ddWXP'})
    
    for container in all_containers:
        find_url = container.find('a')['href']
        print('find_url:', find_url)
        item_url = 'https://www.flipkart.com' + find_url

        driver.get(item_url)
        time.sleep(3)
        
        item_soup = BS(driver.page_source, 'html.parser')
        
        try:
            product_name = item_soup.find('span', {'class': 'B_NuCI'}).text.strip()
            price = item_soup.find('div', {'class': "_30jeq3 _16Jk6d"}).text.strip()

            print('product_name:', product_name)
            print('price:', price)
            print('item_url:', item_url)
            print('---')
            
            row = [product_name, price, item_url]
            all_rows.append(row)
                
        except Exception as ex:
            print('Not Available:', ex)
        
# - after loop -

filename = dt.datetime.now().strftime("amazon_data_%d_%b_%y_%I_%M_%p.csv")

df = pd.DataFrame(all_rows)
df.to_csv(filename)

