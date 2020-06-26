
# date: 2020.06.26
# https://stackoverflow.com/questions/62586100/hidden-element-can-not-found-by-beautifulsoup/

import selenium.webdriver
import time

driver = selenium.webdriver.Firefox()
driver.get("https://www.bet.co.za/bet-games/")

time.sleep(10)

all_iframes = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(all_iframes[1])

all_samples = driver.find_elements_by_css_selector('div.game-result')
print('len(all_samples):', len(all_samples))

for sample in all_samples:
    all_balls = sample.find_elements_by_css_selector('span.ball-item')
    all_text = [ball.text for ball in all_balls]
    print(','.join(all_text))

