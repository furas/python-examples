
# .rar    application/x-rar-compressed, application/octet-stream
# .zip    application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip
# .png    image/png
# .jpg    image/jpeg

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

from pyvirtualdisplay import Display

start_time = time.time()
print('[INFO] start', start_time - start_time)

#display = Display(visible=0, size=(1920,1080))
#display.start()

options = Options()
#options.add_argument("--headless") # don't use it

options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", "/home/furas/Downloads/")
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip") # text/csv image/png image/jpeg

#driver = webdriver.Chrome(executable_path=r'/home/user/bin/gekodriver', options=options)
# I have gekodriver in ~/bin which is in PATH so I don't have to use `executable_path`
driver = webdriver.Firefox(options=options)

print('[INFO] loading', time.time() - start_time)

# https://stackoverflow.com/questions/17533024/how-to-set-selenium-python-webdriver-default-timeout
driver.set_page_load_timeout(20) # to close connection because download doesn't inform about end of downloading
#driver.implicitly_wait(10)
try:
    driver.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
except Exception as ex:
    print('[EX]', ex)    
   
#time.sleep(5)

print('[INFO] closing', time.time() - start_time)
driver.close()
#display.stop()

print('[INFO] end', time.time() - start_time)

