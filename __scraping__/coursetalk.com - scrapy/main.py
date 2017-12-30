#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48017689/1832058
#

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['https://www.coursetalk.com/subjects/data-science/courses']

    def parse(self, response):
        print('url:', response.url)

        for item in response.xpath('.//*[@class="as-table-cell"]/a/@href').extract():
            if item.startswith('/provider'):
                print(item)
            
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(MySpider)
c.start()
