#!/usr/bin/env python3

import scrapy
import json
import time

start_url = 'https://www.ssense.com/en-us/men/sneakers'

class MySpider(scrapy.Spider):

    name = 'myspider'
    
    start_urls = [start_url]

    # replace '__IMAGE_PARAMS__' with parameters which I found in DevTool
    params = 'b_white,c_lpad,g_center,h_960,w_960/c_scale,h_680/f_auto,dpr_1.0'

    def parse(self, response):
        #print('url:', response.url)
        
        products = response.xpath('//figure[@class="browsing-product-item"]')

        for product in products:
            item = {
                'name': product.xpath('.//a/figcaption/p[2]/text()').extract_first(),
                'link': product.xpath('.//meta[3]/@content').extract_first(),
            }
            
            #url = response.urljoin(item['link'])
            #yield scrapy.Request(url=url, callback=self.parse_product, meta={'item': item})

            yield response.follow(item['link'], callback=self.parse_product, meta={'item': item})

        #time.sleep(1)
        
        # execute with low
        yield scrapy.Request(start_url, dont_filter=True, priority=-1)


    def parse_product(self, response):
        #print('url:', response.url)
        
        item = response.meta['item']

        all_scripts = response.xpath('//script/text()').extract()
        
        for script in all_scripts:
            if 'window.INITIAL_STATE=' in script:
                images = json.loads(script[21:])['products']['current']['images']
           
                images = [url.replace('__IMAGE_PARAMS__', self.params) for url in images]
                
                item['image_urls'] = images

        yield item
            
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    #'LOG_FILE': 'scrapy.log',
    
    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    'IMAGES_STORE': '.',
})
c.crawl(MySpider)
c.start()
