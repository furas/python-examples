#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47888293/1832058
# 

import scrapy

data = '''https://www.ceneo.pl/48523541, 1362
https://www.ceneo.pl/46374217, 2457'''


class MySpider(scrapy.Spider):
    
    name = 'myspider'

    start_urls = ['https://www.ceneo.pl/33022301']

    def start_requests(self):
        # get data from file 
        #f = open('urls.csv', 'r')
        
        # simulate file with string
        f = data.split('\n')
        
        for row in f:
            url, id_ = row.split(',')
            url = url.strip()
            id_ = id_.strip()
            
            print(url, id_)
            
            # send `ID` to request
            yield scrapy.Request(url=url, meta={'id': id_})

    def parse(self, response):
        print('url:', response.url)

        # get ID
        id_ = response.meta['id']
        
        all_prices = response.xpath('(//td[@class="cell-price"] /a/span/span/span[@class="value"]/text())[position() <= 10]').extract()
        all_sellers = response.xpath('(//tr/td/div/ul/li/a[@class="js_product-offer-link"]/text())[position()<=10]').extract()
        
        all_sellers = [item.replace('Opinie o ', '') for item in all_sellers]

        for price, seller in zip(all_prices, all_sellers):
            # put ID in item
            yield {'urlid': id_, 'price': price.strip(), 'seller': seller.strip()}

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(MySpider)
c.start()
