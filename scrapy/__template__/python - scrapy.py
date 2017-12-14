#!/usr/bin/env python3

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    allowed_domains = ['http://quotes.toqoute.com']
    
    #start_urls = []

    #def start_requests(self):
    #    for tag in self.tags:
    #        for page in range(self.pages):
    #            url = self.url_template.format(tag, page)
    #            yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)

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
})
c.crawl(MySpider)
c.start()
