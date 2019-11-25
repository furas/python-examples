#!/usr/bin/env python3

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CutSpider(CrawlSpider):

    name = 'CUT'
    
    allowed_domains = ['blog.furas.pl']
    start_urls = ['https://blog.furas.pl/']

    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        #print(response.url)
        return {'url': response.url}


from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(CutSpider)
c.start()
