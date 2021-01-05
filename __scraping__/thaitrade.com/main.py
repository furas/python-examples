
# date: 2020.12.30
# https://stackoverflow.com/questions/65503481/scraping-hidden-link-using-selenium-or-requests#65503481

from selenium import webdriver
import time

link = 'https://www.thaitrade.com/store/9chemical'
driver = webdriver.Chrome()#executable_path=r"C:/chromedriver.exe")    #, options=chrome_options)
driver.maximize_window()
driver.get(link)
#soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep(5)
website = driver.find_element_by_id('seller_website').text
print(website)
