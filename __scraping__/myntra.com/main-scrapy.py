#!/usr/bin/env python3

# date: 2020.05.26
# https://stackoverflow.com/questions/60547578/extract-data-from-script-tag/

import scrapy
import json

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = ['https://www.myntra.com/men-footwear']

    def parse(self, response):
        print('url:', response.url)

        scripts = response.xpath('//script/text()')[9].get()

        # remove window.__myx = 
        script = scripts.split('=', 1)[1]
        
        # convert to dictionary
        data = json.loads(script)
        
        for item in data['searchData']['results']['products']:
            
            info = {
                'product': item['product'],
                'productId': item['productId'],
                'brand': item['brand'],
                'url': 'https://www.myntra.com/' + item['landingPageUrl'],
            }
            
            #yield info

            yield response.follow(item['landingPageUrl'], callback=self.parse_item, meta={'item': info})
            
    def parse_item(self, response):
        print('url:', response.url)

        info = response.meta['item']
        
        # TODO: parse product page with more information
        
        yield info
        
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(MySpider)
c.start() 
