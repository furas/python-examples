
# date: 2019.09.16
# https://stackoverflow.com/questions/57950834/dynamic-web-scrapping-in-python-with-unchanging-url

import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.todywallaauctions.com/Results.aspx/getSearchResult'

payload = {
    'pageSize':'15',
    'pageTop': '1',
    'whereCondition':'; @MotherCategory = Coins & Paper Money'
}

for page in range(1, 2):
    print('---', page, '---')

    payload['pageTop'] = str(page)
    r = requests.post(url, json=payload)
    #print(r.status_code)

    data = r.json()
    #print(data.keys())

    text = data['d']
    #print(text[:1500])

    soup = BS(text)
    for item in soup.find_all('dtlotdata'):
        #print(''.join(str(x) for x in item.contents))
        
        shortdesc = item.find('shortdesc').get_text(strip=True).strip()
        print('> shortdesc:', shortdesc)
        
        listnumber = item.find('listnumber').get_text(strip=True).strip()
        print('> listnumber:', listnumber)
        
        lotno = item.find('lotno').get_text(strip=True).strip()
        print('> lotno:', lotno)
        
        imagecount = item.find('imagecount').get_text(strip=True).strip()
        print('> imagecount:', imagecount)

        number = int(imagecount)
        for x in range(1, number+1):
            filename = '{:>04s}-{:>04s}-{:>02d}.jpg'.format(listnumber,lotno,x)
            url = 'https://www.todywallaauctions.com/PhotosThumb/' + filename
            print(url)
            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
            
