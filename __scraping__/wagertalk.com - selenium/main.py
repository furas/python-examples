
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.05.30
#
# title: Scrape table in nested page appears after click using selenium
# url: https://stackoverflow.com/questions/67765270/scrape-table-in-nested-page-appears-after-click-using-selenium/67766355#67766355


from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import time

url = 'https://www.wagertalk.com/freeOddsPage/page.html?sport=S8&date=2021-05-27&cb=0.6242232189793953'

options = Options()
options.add_argument("--headless")
#options.add_argument('--no-sandbox')
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')   

#driver = webdriver.Chrome(executable_path=r"C:/chromedriver.exe", options=options)
#driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox(options=options)

driver.get(url)

driver.maximize_window()
driver.implicitly_wait(60)

for row in driver.find_elements_by_css_selector('tr[id^="g"]'):
    
    date_time = row.find_elements_by_css_selector('.time-started')
    match_date = date_time[0].text 
    match_time = date_time[1].text
    print('date:', match_date, '| time:', match_time)
    
    teams = row.find_elements_by_css_selector('.team div')
    A_team = teams[0].text
    H_team = teams[1].text
    print('A_team:', A_team)
    print('H_team:', H_team)

    books = row.find_elements_by_css_selector('.book')
    for b in books:
        print('--- popup ---')

        # open .popupDiv
        b.click()
        
        time.sleep(1)
        # ... scrape table from .popupDiv ...
        tds = driver.find_elements_by_css_selector('.popupDiv table td')
        for t in tds:
            print(t.text)
        
        # close .popupDiv
        driver.find_element_by_css_selector('.popupDiv button').click()
        
    print('--- end row ---')
    
driver.quit()


