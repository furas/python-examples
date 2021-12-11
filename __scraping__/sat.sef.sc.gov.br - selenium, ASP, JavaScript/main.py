
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.01
#
# title: Selenium Loop through table pages
# url: https://stackoverflow.com/questions/70184561/selenium-loop-through-table-pages/70186153#70186153

# [Selenium Loop through table pages](https://stackoverflow.com/questions/70184561/selenium-loop-through-table-pages/70186153#70186153)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math

path_driver = "C:/Users/CS330584/Documents/Documentos de Defesa da Concorrência/Automatização de Processos/chromedriver.exe"
website = "https://sat.sef.sc.gov.br/tax.NET/Sat.Dva.Web/ConsultaPublicaDevedores.aspx"
value_search = 300

#driver = webdriver.Chrome(path_driver)
driver = webdriver.Firefox()
driver.get(website)

search_max = driver.find_element_by_id("Body_Main_Main_ctl00_txtTotalDevedores")
search_max.send_keys(value_search)

btn_consult = driver.find_element_by_id("Body_Main_Main_ctl00_btnBuscar")
btn_consult.click()

driver.implicitly_wait(10)


pages = math.ceil(value_search/50)
print('pages:', pages)

for i in range(2, pages+1):
    try:
        time.sleep(2)
        #all_links = driver.find_elements_by_xpath('//tr[@class="sat-gv-pagination-row"]//li//a')
        #all_links[i+1].click()

        next_link = driver.find_element_by_xpath(f'//tr[@class="sat-gv-pagination-row"]//li[{i+1}]//a')
        next_link.click()
        
        #driver.execute_script(f"javascript:GridView_ScrollToTop('Body_Main_Main_grpDevedores_gridView');__doPostBack('ctl00$ctl00$ctl00$Body$Main$Main$grpDevedores$gridView','Page${i}')")
        
    except Exception as ex:
        print(ex)
        break 



