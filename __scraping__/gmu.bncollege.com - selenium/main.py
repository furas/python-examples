# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.26
# [python - Selenium Selector is not consistent returning all options sometimes and other times not? - Stack Overflow](https://stackoverflow.com/questions/71610209/selenium-selector-is-not-consistent-returning-all-options-sometimes-and-other-ti/)

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

from pprint import pprint
import time

# --- functions ---

def select_campus(driver, word="Tech"):
    print('[select_campus] start')
    
    try:
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="bned-campus-select"]//span[@class="selection"]/span'))
        ).click()
        
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, f'//li[contains(text(), "{word}")]'))
        ).click()

        time.sleep(0.5)  # time for JavaScript to create `<select>`

    except Exception as ex:
        print('[select_campus] Exception:', ex)
        return False

    return True


def select_term(driver, term):
    print('[select_term] start')

    try:

        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "term")]//span[@class="selection"]/span'))
        ).click()

        time.sleep(0.5)  # time for JavaScript to create `<select>`
        
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(@class, "term")]//li[contains(text(), "{term}")]'))
        ).click()

        time.sleep(0.5)  # time for JavaScript to create `<select>`

    except Exception as ex:
        print('[select_term] Exception:', ex)
        return False

    return True
    
    
def get_all_departments(driver):
    print('[get_all_departments] start')

    departments = []   
     
    try:
        #select [2]
        all_options = driver.find_elements(By.XPATH, '((//div[@role="table"]//div[@role="row"])[2]//select)[2]//option')

        for index, option in enumerate(all_options[1:], 1):
            item = {"index": index, "department": option.text}
            departments.append(item)
        
        time.sleep(0.5)  # time for JavaScript to create `<select>`

    except Exception as ex:
        print('[get_all_departments] Exception:', ex)
        
    return departments


def select_department(driver, department):
    print('[select_department] start')

    try:
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@role="table"]//div[@role="row"])[2]//div[contains(@class, "department")]//span[@class="selection"]/span'))
        ).click()

        time.sleep(0.5)  # time for JavaScript to create `<select>`

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@role="table"]//div[@role="row"])[2]//div[contains(@class, "department")]//input'))
        )
        element.send_keys(department)
        element.send_keys(Keys.ENTER)
        
        time.sleep(1)
        
    except Exception as ex:
        print('[select_department] Exception:', ex)
        return False

    return True


def get_all_courses(driver):
    print('[get_all_courses] start')

    courses = []

    try:
        #select [3]
        all_options = driver.find_elements(By.XPATH, '((//div[@role="table"]//div[@role="row"])[2]//select)[3]//option')

        for index, option in enumerate(all_options[1:], 1):
            item = {"index": index, "course": option.text}
            courses.append(item)

    except Exception as ex:
        print('[get_all_courses] Exception:', ex)

    return courses

    
def select_course(driver, course):
    print('[select_course] start')
    
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@role="table"]//div[@role="row"])[2]//div[contains(@class, "course")]//span[@class="selection"]/span'))
        )
        element.click()

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@role="table"]//div[@role="row"])[2]//div[contains(@class, "course")]//input'))
        )
        element.send_keys(course)
        element.send_keys(Keys.ENTER)

        time.sleep(1)
        
    except Exception as ex:
        print('[select_course] Exception:', ex)
        return False

    return True


def get_all_sections(driver):
    print('[get_all_sections] start')

    sections = []

    try:
        #select [4]
        all_options = driver.find_elements(By.XPATH, '((//div[@role="table"]//div[@role="row"])[2]//select)[4]//option')


        for index, option in enumerate(all_options[1:], 1):
            #item = {"index": index, "course": option.text}
            sections.append(option.text)

    except Exception as ex:
        print('[get_all_sections] Exception:', ex)

    return sections


def clear_form(driver):
    print('[clear_form] start')
   
    try:
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,'//a[@class="js-clear-row"]'))
        ).click()
        
        time.sleep(0.5)
        
    except Exception as ex:
        print('[clear_form] Exception:', ex)
        return False

    return True
    
    
def main():

    URL = "https://gmu.bncollege.com/course-material/course-finder"

    options = webdriver.ChromeOptions()
    #options.headless = True
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    # options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    start = time.time()
    
    driver.get(URL)

    select_campus(driver)
    select_term(driver, "Spring")

    departments = get_all_departments(driver)
        
    print('departments:')
    pprint(departments[:4])        

    for dep in departments[:4]: #  3 to limit filling all courses for debugging purposes
        print(dep)

        select_department(driver, dep['department'])

        print(dep)
        dep['courses'] = get_all_courses(driver)

        print('departments:')
        pprint(departments[:4])        

        for course in dep['courses']:
            select_course(driver, course['course'])

            course['sections'] = get_all_sections(driver)

            print('departments:')
            pprint(departments[:4])        

        #clear_form(driver)   # DON'T use it

    # --- display ---
    
    for dep in departments[:4]:
        pprint(dep)

    end = time.time()
    print('time:', end - start)

    input('Press ENTER to close')  # to keep open browser and check elements in DevTools
    
    driver.close()

if __name__ == "__main__":
    main()

