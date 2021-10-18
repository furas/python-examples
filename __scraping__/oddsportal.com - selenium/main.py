
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.18
#
# title: Unpacking pands read_HTML dataframe
# url: https://stackoverflow.com/questions/69608885/unpacking-pands-read-html-dataframe/69610319#69610319

# [Unpacking pands read_HTML dataframe](https://stackoverflow.com/questions/69608885/unpacking-pands-read-html-dataframe/69610319#69610319)

import selenium.webdriver
import pandas as pd

driver = selenium.webdriver.Firefox()
driver.get('https://www.oddsportal.com/american-football/usa/nfl')

# --- 

all_results = []
date = None

all_rows = driver.find_elements_by_xpath('//table[@id="tournamentTable"]//tr')

for row in all_rows:
    classes = row.get_attribute('class')
    print('classes:', classes)
    
    if classes == 'center nob-border':
        date = row.find_element_by_tag_name('span').text.strip()
        print('date:', date)
    elif (classes == 'table-dummyrow') or ('hidden' in classes):
        pass   # skip empty rows
    else:
        if date:
            all_cells = row.find_elements_by_xpath('.//td')
            print('len(all_cells):', len(all_cells))
            teams = all_cells[1].text.split(' - ')
            if len(all_cells) == 5: 
                # row without score
                row_values = [
                    date,
                    all_cells[0].text.strip(),
                    teams[0].strip(),
                    teams[1].strip(),
                    '',
                    all_cells[2].text.strip(),
                    all_cells[3].text.strip(),
                    all_cells[4].text.strip(),
                ]
            else: 
                # row with score
                row_values = [
                    date,
                    all_cells[0].text.strip(),
                    teams[0].strip(),
                    teams[1].strip(),
                    all_cells[2].text.strip(),
                    all_cells[3].text.strip(),
                    all_cells[4].text.strip(),
                    all_cells[5].text.strip(),
                ]

            print('row:', row_values)
            all_results.append(row_values)
            
print('-----------------------')

df = pd.DataFrame(all_results, columns=['date', 'game_time', 'Team1', 'Team2', 'Score', '1', '2', 'B'])

print(df)
