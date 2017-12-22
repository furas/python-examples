#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup

headers = {
    #'User-Agent': 'Mozilla/5.0',

    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0',

    #'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
    #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    #'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; EN; rv:11.0) like Gecko',
    #'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    #'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
}  

all_urls = [
    'https://fr.aliexpress.com/category/205000316/men-clothing-accessories.html',
]   

for url in all_urls:
    print('url:', url)
    
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf8', 'ignore')

    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', class_='item')

    for item in products:
        print(' item:', item.find(class_='info').find('a').text)
        print('price:', item.find(class_='price').find(class_='value').text)
        print('image:', item.find(class_='pic').find('img')['src'])
        print('---')

'''
Result:

 item: Rocksir punisher t chemises pour hommes t-shirt Coton de mode marque t shirt hommes Casual Manches Courtes le punisher T-shirt h...
price: € 12,05 - 12,92
image: //ae01.alicdn.com/kf/HTB1ByVZSpXXXXcxaXXXq6xXFXXXW/New-Design-Male-Novelty-Men-T-shirt-Fashion-Cotton-O-neck-Hip-Hop-T-shirt-.jpg_220x220.jpg
--
 item: DIFFELEMENT 2017 Nouveau style long Manteau Hommes marque vêtements mode Long Vestes Manteaux marque-vêtements hommes Pardessus ...
price: € 44,82
image: //ae01.alicdn.com/kf/HTB12IqMXEAKL1JjSZFkq6y8cFXa2/DIFFELEMENT-2017-New-style-long-Coat-Men-brand-clothing-fashion-Long-Jackets-Coats-brand-clothing-mens.jpg_220x220.jpg
--
'''
