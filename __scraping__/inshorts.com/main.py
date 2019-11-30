#!/usr/bin/env python3 

# date: 2019.11.29
# https://stackoverflow.com/questions/59109679/how-to-scrap-1000-news-from-https-inshorts-com-en-read-data-using-beautiful-so

import requests
from bs4 import BeautifulSoup as BS

# --- first page ---

r = requests.get('https://inshorts.com/en/read')
soup = BS(r.text, 'html.parser')

for item in soup.find_all('span', {'itemprop': 'headline'}):
    print(item.get_text(strip=True))
    print('---')

# searching "news_offset" in HTML

start = r.text.find('var min_news_id = "')
start += len('var min_news_id = "')

end = r.text.find('";', start)
end -= len('";')

news_offset = r.text[start:end]
print('news_offset:', news_offset)

# --- next pages ---

#while True:
for _ in range(3):

    params = {'news_offset': news_offset}
    
    r = requests.post('https://inshorts.com/en/ajax/more_news', data=params)
    data = r.json()
    
    soup = BS(data['html'], 'html.parser')
    
    for item in soup.find_all('span', {'itemprop': 'headline'}):
        print(item.get_text(strip=True))
        print('---')
    
    # getting "news_offset" from JSON

    news_offset = data['min_news_id']
    print('news_offset:', news_offset)
    
