#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47751535/1832058
#

import scrapy

class QuotesSpider(scrapy.Spider):
    
    name = 'quotes'
    
    allowed_domains = ['www.onthemarket.com']
    
    start_urls = ['https://www.onthemarket.com/for-sale/property/london/']
    
    def parse(self, response):
        url = response.url
        
        print('>>>', url)
        yield {'link': url} # it will save `page=0` too
        
        next_page_url = response.css("li > a.arrow::attr(href)").extract()[-1]
        next_page_url = response.css("li > a.arrow:last-child::attr(href)").extract_first()
        next_page_url = response.xpath('(//li/a[@class="arrow"]/@href)[last()]').extract_first()
        
        print('last:', next_page_url)
    
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url))

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'output.csv',
})
c.crawl(QuotesSpider)
c.start()

