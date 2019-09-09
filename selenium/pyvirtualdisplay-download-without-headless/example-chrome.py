from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from pyvirtualdisplay import Display

start_time = time.time()
print('[INFO] start', time.time() - start_time)

display = Display(visible=0, size=(1920,1080))
display.start()

options = Options()
#options.add_argument("--headless") # don't use it

options.add_experimental_option("prefs", {
  "download.default_directory": '/home/furas/projekty', # folder for downloaded file
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": False
})

#driver = webdriver.Chrome(executable_path=r'/home/user/bin/chromedriver', options=options)
# I have chromedriver in ~/bin which is in PATH so I don't have to use `executable_path`
driver = webdriver.Chrome(options=options) 

print('[INFO] loading', time.time() - start_time)
driver.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
time.sleep(5)

print('[INFO] closing', time.time() - start_time)
driver.close()
display.stop()

print('[INFO] end', time.time() - start_time)

