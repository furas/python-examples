
# date: 2020.08.25
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# link: (stackoverflow) https://stackoverflow.com/questions/63578637/is-there-a-way-to-extract-date-along-with-link/

import requests
from bs4 import BeautifulSoup

# --- functions ---

def get_data(soup):
    """Get links and dates for one page"""
    
    results = []
    
    all_rows = soup.select('#release-items tr')
    
    for row in all_rows:
        date = row.select_one('.date_uploaded').text
        pdf_url = row.select_one('a[href$=".xls"]')

        if pdf_url:
            pdf_url = pdf_url['href']
            results.append([date, pdf_url])
            print(date, pdf_url)
        else:
            print(date, "Can't find XLS")
            
    return results

# --- main ---

url = 'https://usda.library.cornell.edu/concern/publications/3t945q76s?locale=en#release-items'

all_results = []

# - loop -

while True:
    print('url:', url)

    # get current page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # parse current page - get all needed data
    results = get_data(soup)
    if not results:  # there is no more XLS 
        break

    all_results += results
    
    # get link to next page
    url = soup.find('a', {'rel': 'next'})
    if not url or url['href'] == '#':  # there is no more pages
        break
    
    url = 'https://usda.library.cornell.edu' + url['href']

# - after loop -

print('--- results ---')
print('len:', len(all_results))
print('first:', all_results[0])
print('last :', all_results[-1])
