from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
 
#--| Setup
options = Options()
#options.add_argument("--headless")
#options.add_argument("--window-size=1980,1020")
#options.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path=r'C:\chrome\chromedriver.exe', options=options)
#browser = webdriver.Firefox()

# --- login ---

browser.get("https://login.wordpress.org/?locale=en_US")
time.sleep(2)

user_name = browser.find_element_by_css_selector('#user_login')
user_name.send_keys("my_login")
password = browser.find_element_by_css_selector('#user_pass')
password.send_keys("my_password")
#time.sleep(5)
submit = browser.find_elements_by_css_selector('#wp-submit')[0]
submit.click()
 
# Example send page source to BeautifulSoup or selenium for parse
soup = BeautifulSoup(browser.page_source, 'lxml')
use_bs4 = soup.find('title')
print(use_bs4.text)
#print('*' * 25)
#use_sel = browser.find_elements_by_css_selector('div > div._1vC4OE')
#print(use_sel[0].text)

# --- pages ---

url = 'https://wordpress.org/support/plugin/advanced-gutenberg/page/{}/'
 
for page in range(1, 3):
    print('\n--- PAGE:', page, '---\n')
 
    # read page with list of posts
    browser.get(url.format(page))
    soup = BeautifulSoup(browser.page_source, 'html.parser') # 'lxml'
 
    all_uls = soup.find('li', class_="bbp-body").find_all('ul')
 
    for number, ul in enumerate(all_uls, 1):
 
        print('\n--- post:', number, '---\n')
 
        a = ul.find('a')
        if a:
            post_url = a['href']
            post_title = a.text
 
            print('text:', post_url)
            print('href:', post_title)
            print('---------')
 
            # read page with post content
            browser.get(post_url)
            sub_soup = BeautifulSoup(browser.page_source, 'html.parser')
 
            post_content = sub_soup.find(class_='bbp-topic-content').get_text(strip=True, separator='\n')
            print(post_content)
