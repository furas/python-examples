
#
# https://stackoverflow.com/a/47716786/1832058
#
# https://stackoverflow.com/a/48116666/1832058
#

import requests
from bs4 import BeautifulSoup

def get_details(url):
    print('details:', url)

    # get subpage
    r = requests.get(url)
    soup = BeautifulSoup(r.text ,"lxml")

    # get data on subpabe
    dts = soup.findAll('dt')
    dds = soup.findAll('dd')

    # display details
    for dt, dd in zip(dts, dds):
        print(dt.text)
        print(dd.text)
        print('---')

    print('---------------------------')

def drug_data():
    url = 'https://www.drugbank.ca/drugs/'

    while url:
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text ,"lxml")

        # get links to subpages
        links = soup.select('strong a')
        for link in links:
            # exeecute function to get subpage
            #get_details('https://www.drugbank.ca' + link['href'])
            

        # next page url
        url = soup.findAll('a', {'class': 'page-link', 'rel': 'next'})
        print(url)
        if url:
            url = 'https://www.drugbank.ca' + url[0].get('href')
        else:
            break

drug_data()
