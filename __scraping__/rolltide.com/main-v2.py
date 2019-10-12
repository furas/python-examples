#!/urs/bin/env python3

# date: 2019.10.12
# https://stackoverflow.com/questions/58349843/im-trying-to-scrape-college-football-team-rosters-into-an-excel-file-and-need-h

from selenium import webdriver
import csv

url = 'https://rolltide.com/roster.aspx?roster=226&path=football'

driver = webdriver.Firefox()
driver.get(url)

all_rows = driver.find_elements_by_xpath('//ul[@class="sidearm-roster-players"]//li')

fh = open('output.csv', 'w')
csvwriter = csv.writer(fh)
#write headers
csvwriter.writerow(["Number", "Name", "Position", "Height", "Weight", "Hometown", "Highschool", "Academic year"])

for row in all_rows: #[:10]:
    number = row.find_element_by_xpath('.//div[@class="sidearm-roster-player-name"]//span').text
    print('number:', number)

    name = row.find_element_by_xpath('.//div[@class="sidearm-roster-player-name"]//p').text
    #print('name:', name)

    position = row.find_element_by_xpath('.//div[@class="sidearm-roster-player-position"]/span').text
    #print('position:', position)

    height = row.find_element_by_class_name('sidearm-roster-player-height').text
    #print('height:', height)

    weight = row.find_element_by_class_name('sidearm-roster-player-weight').text
    #print('weight:', weight)

    # it seems some classes have two elements in row - first probably always is empty but I join all elements 

    hometown = row.find_elements_by_class_name('sidearm-roster-player-hometown')
    hometown = ''.join(x.text for x in hometown)
    #print('hometown:', hometown)

    highschool = row.find_elements_by_class_name('sidearm-roster-player-highschool')
    highschool = ''.join(x.text for x in highschool)
    #print('highschool:', highschool)

    academic_year = row.find_elements_by_class_name('sidearm-roster-player-academic-year')
    academic_year = ''.join(x.text for x in academic_year)
    #print('academic_year:', academic_year)
    
    #print('---')
    csvwriter.writerow([number, name, position, height, weight, hometown, highschool, academic_year])
    
fh.close()    
