#!/urs/bin/env python3

# date: 2019.10.12
# https://stackoverflow.com/questions/58349843/im-trying-to-scrape-college-football-team-rosters-into-an-excel-file-and-need-h

from selenium import webdriver

url = 'https://rolltide.com/roster.aspx?roster=226&path=football'

#driver = webdriver.Firefox()
driver.get(url)

all_names = driver.find_elements_by_class_name('sidearm-roster-player-name')
all_positions = driver.find_elements_by_class_name('sidearm-roster-player-position')
all_hometowns = driver.find_elements_by_class_name('sidearm-roster-player-class-hometown')

#for name, position, hometown in zip(all_names, all_positions, all_hometowns):
#    print(name.text, "|", position.text, "|", hometown.text)

all_rows = driver.find_elements_by_xpath('//ul[@class="sidearm-roster-players"]//li')

for row in all_rows[:10]:
    number = row.find_element_by_xpath('.//div[@class="sidearm-roster-player-name"]//span')
    print('number:', number.text)

    name = row.find_element_by_xpath('.//div[@class="sidearm-roster-player-name"]//p')
    print('name:', name.text)

    position = row.find_element_by_xpath('.//div[@class="sidearm-roster-player-position"]/span')
    print('position:', position.text)

    height = row.find_element_by_xpath('.//span[@class="sidearm-roster-player-height"]')
    print('height:', height.text)

    weight = row.find_element_by_xpath('.//span[@class="sidearm-roster-player-weight"]')
    print('weight:', weight.text)

    academic_year = row.find_element_by_xpath('.//span[@class="sidearm-roster-player-academic-year"]')
    print('academic_year:', academic_year.text)

    hometown = row.find_element_by_xpath('.//span[@class="sidearm-roster-player-hometown"]')
    print('hometown:', hometown.text)

    highschool = row.find_element_by_xpath('.//span[@class="sidearm-roster-player-highschool"]')
    print('highschool:', highschool.text)

    print('---')
