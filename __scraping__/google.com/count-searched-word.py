#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48048171/1832058
# 

import scrapy
import re

class MySpider(scrapy.Spider):
    
    name = 'myspider'
    
    allowed_domains = ['www.google.com']

    def __init__(self, word=None):
        super().__init__()
        self.word = word
        self.start_urls = ['https://www.google.com/search?q='+self.word]

    def parse(self, response):
        print('url:', response.url)
        
        # all text on page
        #text = response.xpath('//text()').extract() 
        
        # text only in search results
        text = response.xpath('//*[@class="g"]//text()').extract() 
        
        text = ''.join(text).lower()
        count = len(re.findall(self.word, text))
        
        print('count:', count)
    
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess
import sys

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
#c.crawl(MySpider, word='scraping')
c.crawl(MySpider, word=sys.argv[1])
c.start()
