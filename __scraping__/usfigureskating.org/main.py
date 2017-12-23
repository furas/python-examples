#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47849047/1832058
#

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['http://www.usfigureskating.org/leaderboard/results/2018/25073/SEGM001.html']

    def parse(self, response):
        print('url:', response.url)

        body = response.body.replace(b'<<+', b'&lt;&lt;+').replace(b'<+', b'&lt;+')
            
        selector = scrapy.Selector(text=body.decode('utf-8'))

        i = 1
        for x  in selector.css('.elem::text').extract():
            if 'Elements' in x:
                print('---', i, '---')
                i += 1
            else:
                print(x)

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in CSV or JSON
    #'FEED_FORMAT': 'csv',     # 'json
    #'FEED_URI': 'output.csv', # 'output.json
})
c.crawl(MySpider)
c.start()

'''
Results:

Executed
--- 1 ---
2Ab1+2T
ChSt1
2Ab1
2Lz+1Lo+2Lo
2Lz
FSSp4
2F
CCoSp4
Executed
--- 2 ---
2Ab1
ChSt1
2Ab1+1Lo+2F
CCoSp2V
2Lz+2Lo
2Lo
2Lz
LSp4
Executed
--- 3 ---
CCoSp4
ChSt1
2Ab1+2Lo
2Lz+1Lo+2Lo
2Ab1
2Lz
2Fe
FSSp4
Executed
--- 4 ---
2Ab1+1Lo+2Lo
2Ab1
LSp4
ChSt1
2Lz
2F
2Lz+2T
CCoSp4
Executed
--- 5 ---
2Ab1
LSp2
ChSt1
2Ab1+1Lo+1Lo
2Lz+2Lo
2Lz
2F
CCoSp3
Executed
--- 6 ---
2Lz
1A
SSp3
ChSt1
2Lz+1Lo+2Lo
CCoSp3
2F+2Lo
2F
Executed
--- 7 ---
2F
2Ab1
CCoSp4
2Lz
2Ab1<+2T
ChSt1
2Lz+1Lo+2F
LSp4
Executed
--- 8 ---
1A
LSp4
ChSt1
2Lz
2Lz+2T
2Lo+2T+1Lo
2F
CCoSp4
Executed
--- 9 ---
2A<<
CCoSp4
ChSt1
2F+1Lo+2Lo
2Lze+2Lo
2Lze
2F
SSp4
Executed
--- 10 ---
2Lz
2Ab1
SSp3
ChSt1
2A<<+REP
2Lz+2Lo
2F
CCoSp4
Executed
--- 11 ---
FSSp4
2Ab1<+2Lo
ChSt1
2A<<
FCCoSp3
2F+2Lo<+1Lo<<
2Lz
2F
Executed
--- 12 ---
2A<<+1Lo+2Lo<
2Lze
SSp3
ChSt1
2A<<
2F
2F+2Lo<
CCoSp3
'''
