#!/usr/bin/env python3

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get list or use empty list 
        # (as default it would return `None` but `start_urls` has to be list)
        self.start_urls = kwargs.get('urls', [])

    def parse(self, response):
        print('url:', response.url)
   
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(MySpider, urls=['http://quotes.toscrape.com'])
c.start()
