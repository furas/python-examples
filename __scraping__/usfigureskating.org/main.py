#!/usr/bin/env python3

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
