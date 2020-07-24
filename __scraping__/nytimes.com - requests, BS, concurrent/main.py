
# date: 2020.07.16
# link: https://stackoverflow.com/questions/62941657/how-can-i-return-the-data-im-scraping-when-using-beautifulsoup-and-concurrent-f/

import requests
from bs4 import BeautifulSoup
import concurrent.futures

# --- constants ---

MAX_THREADS = 30

# --- functions ---

# grab all of the recipe cards on each search page
def extract_recipe_urls(url):
    """returns a list of recipe urls"""
    
    session = requests.Session()

    recipe_cards = []
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for rs in soup.find_all("article",{"class":"card recipe-card"}):
        recipe_cards.append(rs.find('a')['href'])
    
    return recipe_cards

def async_scraping(scrape_function, urls):
    threads = min(MAX_THREADS, len(urls))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(scrape_function, urls)
        
    return results

# --- main ---

urls = ['https://cooking.nytimes.com/search?q=&page={page_number}'.format(page_number=p) for p in range(1,5)]

results = async_scraping(extract_recipe_urls, urls)

#for item in results:
#    print(item)

# `results` is a generator so better get as list to use it with many `for`-loops
all_items = list(results)
print('len(all_items):', len(all_items))
      
for item in all_items:
    print('len(item):', len(item))

# flatten list
all_items = sum(all_items, [])
print('len(all_items):', len(all_items))


