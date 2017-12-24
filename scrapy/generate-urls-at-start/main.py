#!/usr/bin/env python3

# 
# https://stackoverflow.com/a/47722953/1832058
# 

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    allowed_domains = ['http://quotes.toqoute.com']
    
    #start_urls = []

    tags = ['love', 'inspirational', 'life', 'humor', 'books', 'reading']
    pages = 3
    url_template = 'http://quotes.toscrape.com/tag/{}/page/{}'
    
    def start_requests(self):
        
        for tag in self.tags:
            for page in range(self.pages):
                url = self.url_template.format(tag, page)
                yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)
                                 
# --- run it without project ---

from scrapy.crawler import CrawlerProcess

#c = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
#    'FEED_FORMAT': 'csv',
#    'FEED_URI': 'data.json',
#}
                   
c = CrawlerProcess()
c.crawl(MySpider)
c.start()
