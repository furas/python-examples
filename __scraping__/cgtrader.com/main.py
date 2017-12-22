#!/usr/bin/env python3

import scrapy
#from scrapy.commands.view import open_in_browser
#import json

class FileDownloaderItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    full_urls = scrapy.Field()
    
class MySpider(scrapy.Spider):
    
    name = 'myspider'

    allowed_domains = ['www.cgtrader.com']
    start_urls = ['https://www.cgtrader.com/free-3d-print-models?keywords=mobile']

    def parse(self, response):
        print('url:', response.url)

    def parse(self, response):
        for book in response.css('div.grid__col '):
            href = book.css('div.content-box__content > a::attr(href)').extract_first()
            full_url = response.urljoin(href)
            yield scrapy.Request(full_url, callback=self.pas)

    def pas(self,response):
        src = response.css('div.download_free > a::attr(href)').extract_first()
        cover = response.urljoin(src)
        #print('free models link',cover)
        yield scrapy.Request(cover,callback=self.dwn)

    def dwn(self,response):
        mdls = response.css("li > span > a::attr(href)").extract_first()
        cvr = response.urljoin(mdls)
        print('cvrs data',cvr)
        yield FileDownloaderItem(full_urls = [cvr])
        
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    'FILES_STORE': '.',

    # download images and convert to JPG
    # it needs `yield {'image_urls': [url]}` in `parse()`
    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    #'IMAGES_STORE': '/path/to/valid/dir',
})
c.crawl(MySpider)
c.start()
