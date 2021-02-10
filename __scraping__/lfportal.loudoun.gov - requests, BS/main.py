# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.02.10
# https://stackoverflow.com/questions/66136166/scraping-and-downloading-excel-files-using-python-from-url/

import requests
from bs4 import BeautifulSoup as bs
import os

# --- functions ---

def get_soup(url):
    response = requests.get(url)
    #print(response.status_code)
    #print(response.text)
    html = response.text

    soup = bs(html, 'html.parser')
    #soup = bs(html, 'lxml')
    #soup = bs(html, 'html5lib')

    return soup

# --- main ---

# - data - 

DOMAIN = 'https://lfportal.loudoun.gov/LFPortalinternet/'
URL = 'https://lfportal.loudoun.gov/LFPortalinternet/Browse.aspx?startid=213973&row=1&dbid=0'
FILETYPE = '.xls'

# - code -

soup = get_soup(URL)
for folder_link in soup.find_all('a', {'class': 'DocumentBrowserNameLink'}):
    folder_name = folder_link.get('aria-label').split(' ')[0]
    folder_link = folder_link.get('href')

    print('folder:', folder_name)
    os.makedirs(folder_name, exist_ok=True)
    
    subsoup = get_soup(DOMAIN + folder_link)
    for file_link in subsoup.find_all('a', {'class': 'DocumentBrowserNameLink'}):
        file_name = file_link.get('aria-label')[:-4]  # skip extra `.xls` at the end
        file_link = file_link.get('href')
        
        if file_link.endswith(FILETYPE):
            print('  file:', file_name)
            file_name = os.path.join(folder_name, file_name)
            with open(file_name, 'wb') as file:
                response = requests.get(DOMAIN + file_link)
                file.write(response.content)
