from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

start_time = time.time()

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")

#driver = webdriver.Chrome(executable_path=r'/home/chromedriver/chromedriver',options=options)
driver = webdriver.Chrome(options=options)

params = {'behavior': 'allow', 'downloadPath': '/home/furas/projekty'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
# downloads are now enabled for this driver instance

driver.get('https://www.macrotrends.net/1476/copper-prices-historical-chart-data')
print('[INFO] loaded', time.time() - start_time)
time.sleep(5)

iframe = driver.find_element_by_xpath("//iframe[@id='chart_iframe']")
driver.switch_to.frame(iframe)
print('[INFO] switched', time.time() - start_time)

xpath = "//a[text()='All Years']"
driver.find_element_by_xpath(xpath).click()
xpath = "//button[@id='dataDownload']"
driver.find_element_by_xpath(xpath).click()
print('[INFO] clicked', time.time() - start_time)
time.sleep(10)

print('[INFO] closing', time.time() - start_time)
driver.close()

