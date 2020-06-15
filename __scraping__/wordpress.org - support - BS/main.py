#!/usr/bin/env python3

# date: 2020.06.14
# https://stackoverflow.com/questions/62373373/bs4-fetching-thread-titles-description-plus-more-from-wordpress-org-support-fo

import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'}) # this page needs header 'User-Agent` 

url = 'https://wordpress.org/support/plugin/advanced-gutenberg/page/{}/'

for page in range(1, 3):
    print('\n--- PAGE:', page, '---\n')
    
    # read page with list of posts
    r = session.get(url.format(page))

    soup = BS(r.text, 'html.parser')
    
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
            r = session.get(post_url)
            
            sub_soup = BS(r.text, 'html.parser')
            
            post_content = sub_soup.find(class_='bbp-topic-content').get_text(strip=True, separator='\n')
            print(post_content)

