#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48035123/1832058
# 

import scrapy
from scrapy.commands.view import open_in_browser

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['https://www.snapdeal.com/']

    def parse(self, response):
        print('url:', response.url)

        #open_in_browser(response)
        
        for item in response.xpath('//*[@class="catText"]/text()').extract():
            print(item)
    
# --- it runs without project ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(MySpider)
c.start()
