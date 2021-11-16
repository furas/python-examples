
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.03
#
# title: Multiple scraping: problem in the code. What am I doing wrong?
# url: https://stackoverflow.com/questions/69817631/multiple-scraping-problem-in-the-code-what-am-i-doing-wrong/69818379#69818379

# [Multiple scraping: problem in the code. What am I doing wrong?](https://stackoverflow.com/questions/69817631/multiple-scraping-problem-in-the-code-what-am-i-doing-wrong/69818379#69818379)

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.diretta.it/calcio/svezia/allsvenskan/risultati/")
driver.implicitly_wait(12)
#driver.minimize_window()

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='event__more event__more--static']"))).click()
except Exception as ex:
    print('EX:', ex)

all_rows = driver.find_elements(By.CSS_SELECTOR, "div[class^='event__round'],div[class^='event__match']")

results = []

current_round = '?'

for row in all_rows:
    classes = row.get_attribute('class')
    #print(classes)
    
    if 'event__round' in classes:
        #round = row.find_elements(By.CSS_SELECTOR, "[class^='event__round event__round--static']")
        #current_round = row.text  # full text `Round 20`
        current_round = row.text.split(" ")[-1]  # only `20` without `Round`
    else:
        datetime = row.find_element(By.CSS_SELECTOR, "[class^='event__time']")
        
        date, time = datetime.text.split(" ")
        date = date.rstrip('.')  # right-strip to remove `.` at the end of date
        
        team_home = row.find_element(By.CSS_SELECTOR, "[class^='event__participant event__participant--home']")            
        team_away = row.find_element(By.CSS_SELECTOR, "[class^='event__participant event__participant--away']")
        score_home = row.find_element(By.CSS_SELECTOR, "[class^='event__score event__score--home']")
        score_away = row.find_element(By.CSS_SELECTOR, "[class^='event__score event__score--away']")   

        # old version
        #row = [current_round, datetime.text, team_home.text, team_away.text, score_home.text, score_away.text]
    
        row = [current_round, date, time, team_home.text, team_away.text, score_home.text, score_away.text]
        results.append(row)
        print(row)

# --- database ---

import sqlite3

con = sqlite3.connect('database.db')
cursor = con.cursor()

query = 'DROP TABLE IF EXISTS All_Score;'
cursor.execute(query)

# old version - with only `date`
#query = 'CREATE TABLE IF NOT EXISTS All_Score(current_round, date, team_home, team_away, score_home, score_away);'
# new version - with `date` and `time`
query = 'CREATE TABLE IF NOT EXISTS All_Score(current_round, date, time, team_home, team_away, score_home, score_away);'
cursor.execute(query)

# old version - with only `date`
#query = 'INSERT INTO All_Score(current_round, date, team_home, team_away, score_home, score_away) VALUES (?, ?, ?, ?, ?, ?);'
# new version - with `date` and `time`
query = 'INSERT INTO All_Score(current_round, date, time, team_home, team_away, score_home, score_away) VALUES (?, ?, ?, ?, ?, ?, ?);'
cursor.executemany(query, results)

con.commit()  
