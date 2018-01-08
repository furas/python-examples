
# 
# Web browsers create only screenshot of visible part.
# PantomJS can create full page screenshot,
# but it need correct window size and User-Agent.
#

import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import webbrowser
#import time

settings = dict(DesiredCapabilities.PHANTOMJS)
settings['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0') 
driver = selenium.webdriver.PhantomJS(desired_capabilities=settings)
driver.set_window_size(1200, 800)

driver.get('https://en.wikipedia.org/wiki/Screenshot')
#time.sleep(1)

driver.save_screenshot('output.png')
webbrowser.open('output.png')


