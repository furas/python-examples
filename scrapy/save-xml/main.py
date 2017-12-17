#!/usr/bin/env python3

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('url:', response.url)

        # finc tags on 
        for quote in response.css('.tag-item a'):
            
            # create tag
            tag = 'Tag ' + quote.css('::text').extract_first()
            
            # find url to subpage
            url = quote.css('::attr(href)').extract_first()
            url = response.urljoin(url)
            
            print('tag/url:', tag, url)
            
            # create request with tag as meta
            yield scrapy.Request(url, meta={'tag': tag}, callback=self.parse_tags)
            
    def parse_tags(self, response):
        print('url:', response.url)
            
        # get tag from previous request
        tag = response.meta['tag']
        
        # find quotes
        all_quotes = response.css('.quote .text ::text').extract()
            
        # display
        for quote in all_quotes:
            print('--- quote ---')
            print(quote)

        # crop quotes only to make smaller example output
        all_quotes = [quote[:10] + ' ...' for quote in all_quotes]
        all_quotes = all_quotes[:3]
        
        # send all quotes for one tag as single item
        yield {tag: all_quotes}

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in XML, CSV or JSON
    'FEED_FORMAT': 'xml',     # 'json, csv
    'FEED_URI': 'output.xml', # 'output.json, output.csv
})
c.crawl(MySpider)
c.start()
