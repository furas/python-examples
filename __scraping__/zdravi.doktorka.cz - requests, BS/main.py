
# date: 2020.07.01
# https://stackoverflow.com/questions/62667459/python-web-scraper-gives-the-same-page-as-the-response

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://zdravi.doktorka.cz/clanky?page=0'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

HOST = 'https://zdravi.doktorka.cz'

def get_soup(url, headers=HEADERS, params=None):
    r = requests.get(url, headers=headers, params=params)
    
    if r.status_code != 200:
        print('Error:', r.status_code, url)
        return

    return BeautifulSoup(r.text, 'html.parser')

def get_content(soup):
    
    data = []
    
    articles = soup.find_all('article', class_='node-teaser-display')

    for item in articles:
        url = HOST + item.find('a').get('href')
        print(url)
        
        soup = get_soup(url)
        if soup:
        
            paragraph = soup.find('p').get_text().strip()
            print(paragraph)
  
            data.append({
                'url': url,
                'paragraph': paragraph,
            })
    
        print('---')
        
    with open('output.csv', 'w') as fh:
        csv_writer = csv.DictWriter(fh, ['url', 'paragraph'])
        csv_writer.writeheader()
        csv_writer.writerows(data)           
        
def parse():
    soup = get_soup(URL)
    if soup:
        get_content(soup)
       
if __name__ == '__main__':        
    parse()
