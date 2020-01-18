#!/usr/bin/env python3

# date: 2020.01.17
# https://stackoverflow.com/questions/59789768/init-missing-1-required-positional-argument-when-added-stats/

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = ['http://books.toscrape.com/'] #'http://quotes.toscrape.com']

    def parse(self, response):
        print('url:', response.url)
        

class MyPipeline(object):

    def __init__(self, stats):
        print('__init__ stats:', stats)
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        print('from_crawler stats:', crawler.stats)
        return cls(crawler.stats)

    
from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'ITEM_PIPELINES': {'__main__.MyPipeline': 1}, # used Pipeline created in current file (needs __main___)
})
c.crawl(MySpider)
c.start()
