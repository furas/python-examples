
#
# https://stackoverflow.com/a/47716786/1832058
#

import requests
from bs4 import BeautifulSoup

def drug_data():
    url = 'https://www.drugbank.ca/drugs/'

    while url:
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text ,"lxml")

        #data = soup.select('name-head a')
        #for link in data:
        #    href = 'https://www.drugbank.ca/drugs/' + link.get('href')
        #    pages_data(href)

        # next page url
        url = soup.findAll('a', {'class': 'page-link', 'rel': 'next'})
        print(url)
        if url:
            url = 'https://www.drugbank.ca' + url[0].get('href')
        else:
            break

drug_data()
