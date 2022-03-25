#!/usr/bin/env python3

# 
# https://stackoverflow.com/a/48031565/1832058
# 

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['https://www.indeed.cl/trabajo?q=Data%20scientist&l=']

    def parse(self, response):
        print('url:', response.url)

        results = response.xpath('//h2[@class="jobtitle"]/a')
        print('number:', len(results))
        for item in results:
            title = ''.join(item.xpath('.//text()').extract())
            print('title:', title)

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(MySpider)
c.start()
