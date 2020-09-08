
# date: 2020.08.25
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# link: (stackoverflow) https://stackoverflow.com/questions/63578552/having-trouble-interpreting-website-source-code/

import selenium.webdriver

url = ' https://www.footywire.com/afl/footy/dream_team_breakevens'
search = 'Kennedy'

driver = selenium.webdriver.Firefox()
driver.get(url)

#print('get rows')

#all_rows = driver.find_elements_by_xpath('//tr[@onmouseover]')
all_rows = driver.find_elements_by_css_selector('tr[onmouseover]')

for row in all_rows:
    #print('get columns')
    
    #all_cols = row.find_elements_by_xpath('.//td')  # start with `.` to use relative xpath and search only inside `row`
    #all_cols = row.find_elements_by_tag_name('td')
    all_cols = row.find_elements_by_css_selector('td')
    
    #for idx, item in enumerate(all_cols):
    #    print(idx, item.text)
    
    name = all_cols[0].find_element_by_tag_name('a').text
    breakeven = all_cols[5].text
    
    if search in name:
        print(name, breakeven)
        break # exit loop and don't check other rows
    
driver.close()