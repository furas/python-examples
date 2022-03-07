# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.07
# [javascript - export gpx file with python? - Stack Overflow](https://stackoverflow.com/questions/71375579/export-gpx-file-with-python/71375874#71375874)


# doesn't work - page downloads data from `BLOB` in memory

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://routing.openstreetmap.de/?z=17&center=51.515199%2C-0.092772&loc=51.514739%2C-0.089800&loc=51.516214%2C-0.096656&hl=en&alt=0&srv=1'

directory = '/home/furas/'

options = webdriver.firefox.options.Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", directory)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # ?
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/gpx")          # ?

driver = webdriver.Firefox(options=options)
driver.get(url)

driver.find_element(By.XPATH, '//span[@title="Export GPX file"]').click()

