#!/usr/bin/env python3

import scrapy
#from scrapy.commands.view import open_in_browser
import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = []
    
    #start_urls = ['https://www.chumbak.com/women-apparel/GY1/c/']
    
    #start_urls = [
    #    'https://api-cdn.chumbak.com/v1/category/474/products/?count_per_page=24&page=1',
    #    'https://api-cdn.chumbak.com/v1/category/474/products/?count_per_page=24&page=2',
    #    'https://api-cdn.chumbak.com/v1/category/474/products/?count_per_page=24&page=3',
    #]
    
    def start_requests(self):
        pages = 10
        url_template = 'https://api-cdn.chumbak.com/v1/category/474/products/?count_per_page=24&page={}'
        
        for page in range(pages):
            url = url_template.format(page)
            yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)

        #open_in_browser(response)
        
        # get page number
        page_number = response.url.strip('=')[-1]
        
        # save JSON in separated file
        filename = 'page-{}.json'.format(page_number)
        with open(filename, 'wb') as f:
           f.write(response.body)
        
        # convert JSON into Python's dictionary
        data = json.loads(response.text)
        
        # get urls for images
        for product in data['products']:
            #print('title:', product['title'])
            #print('url:', product['url'])
            #print('image_url:', product['image_url'])
            
            # create full url to image
            image_url = 'https://media.chumbak.com/media/catalog/product/small_image/260x455' + product['image_url']
            # send it to scrapy and it will download it
            yield {'image_urls': [image_url]}
            
                   
        # download files
        #for href in response.css('img::attr(href)').extract():
        #   url = response.urljoin(src)
        #   yield {'file_urls': [url]}

        # download images and convert to JPG
        #for src in response.css('img::attr(src)').extract():
        #   url = response.urljoin(src)
        #   yield {'image_urls': [url]}

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in CSV or JSON
    'FEED_FORMAT': 'json',     # 'cvs', 'json', 'xml'
    'FEED_URI': 'output.json', # 'output.cvs', 'output.json', 'output.xml'

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    #'FILES_STORE': '/path/to/valid/dir',

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    #'IMAGES_STORE': '/path/to/valid/dir',
    'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    'IMAGES_STORE': '.',
})
c.crawl(MySpider)
c.start()
