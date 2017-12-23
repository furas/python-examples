#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47848134/1832058
#

import scrapy
import json

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    allowed_domains = ['www.myntra.com']

    start_urls = ['https://www.myntra.com/web/v2/search/data/duke']
    
    #def start_requests(self):
    #    for tag in self.tags:
    #        for page in range(self.pages):
    #            url = self.url_template.format(tag, page)
    #            yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)

        #print(response.body)
        
        data = json.loads(response.body)
        
        print('data.keys():', data.keys())
        
        print('meta:', data['meta'])
        
        print("data['data']:", data['data'].keys())
        
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
    #'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',

    # save in CSV or JSON
    'FEED_FORMAT': 'csv',     # 'json
    'FEED_URI': 'output.csv', # 'output.json

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    #'FILES_STORE': '/path/to/valid/dir',

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.files.ImagesPipeline': 1},
    #'IMAGES_STORE': '/path/to/valid/dir',
    
    #'HTTPCACHE_ENABLED': False,
    #'dont_redirect': True,
    #'handle_httpstatus_list' : [302,307],
    #'CRAWLERA_ENABLED': False,
})
c.crawl(MySpider)
c.start()
