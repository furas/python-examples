#!/usr/bin/env python3

import scrapy
#from scrapy.commands.view import open_in_browser
#import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = []
    
    start_urls = ['https://www.ceneo.pl/33022301']

    #def start_requests(self):
    #    self.url_template = http://quotes.toscrape.com/tag/{}/page/{}/
    #    self.tags = ['love', 'inspirational', 'life', 'humor', 'books']
    #    self.pages = 10
    # 
    #    for tag in self.tags:
    #        for page in range(self.pages):
    #            url = self.url_template.format(tag, page)
    #            yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)

        all_prices = response.xpath('(//td[@class="cell-price"] /a/span/span/span[@class="value"]/text())[position() <= 10]').extract()
        all_sellers = response.xpath('(//tr/td/div/ul/li/a[@class="js_product-offer-link"]/text())[position()<=10]').extract()
        
        pairs = [{'price': price.strip(), 'seller': seller.strip()} for price, seller in zip(all_prices, all_sellers)]
        yield pairs
        
        #for price, seller in zip(all_prices, all_sellers):
        #    yield {'price': price.strip(), 'seller': seller.strip()}
        
        #open_in_browser(response)
        
        # save JSON in separated file
        #number = response.url.split('/')[-1]
        #filename = 'page-{}.json'.format(number)
        #with open(filename, 'wb') as f:
        #   f.write(response.body)

        # convert JSON into Python's dictionary
        #data = json.loads(response.text)

        # download files
        #for href in response.css('img::attr(href)').extract():
        #   url = response.urljoin(src)
        #   yield {'file_urls': [url]}

        # download images and convert to JPG
        #for src in response.css('img::attr(src)').extract():
        #   url = response.urljoin(src)
        #   yield {'image_urls': [url]}

        #item = {'url': '...', 'title': '...'}
        #yield self.Request(url, meta={'item': item}, callback=self.parse_details)
        
    #def parse_details(self, response):
    #   item = response.meta['item']
    #   item['more'] = 'More and more data'
    #   yield item  
    
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    #'FILES_STORE': '/path/to/valid/dir',

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    #'IMAGES_STORE': '/path/to/valid/dir',
})
c.crawl(MySpider)
c.start()
