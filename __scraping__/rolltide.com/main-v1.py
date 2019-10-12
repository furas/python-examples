#!/urs/bin/env python3

# date: 2019.10.12
# https://stackoverflow.com/questions/58349843/im-trying-to-scrape-college-football-team-rosters-into-an-excel-file-and-need-h

from selenium import webdriver

url = 'https://rolltide.com/roster.aspx?roster=226&path=football'

driver = webdriver.Firefox()
driver.get(url)

all_names = driver.find_elements_by_class_name('sidearm-roster-player-name')
all_positions = driver.find_elements_by_class_name('sidearm-roster-player-position')
all_hometowns = driver.find_elements_by_class_name('sidearm-roster-player-class-hometown')

for name, position, hometown in zip(all_names, all_positions, all_hometowns):
    print(name.text, "|", position.text, "|", hometown.text)

