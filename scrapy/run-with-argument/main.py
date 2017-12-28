#!/usr/bin/env python3

#
# $ scrapy crawl myspider -a word="abba"
#

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['http://quotes.toscrape.com']

    def __init__(self, word=None, *args, **kwargs):  # <--- receive parameter
        super().__init__(*args, **kwargs)
        self.word = word  # <--- receive parameter

    def parse(self, response):
        print('url:', response.url)
        print('word:', self.word)  # <--- use parameter
        
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(MySpider, word='tags') # <--- send parameter
c.start()
