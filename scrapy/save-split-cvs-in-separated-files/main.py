#!/usr/bin/env python3

# date: 2020.07.05
# https://stackoverflow.com/questions/62735616/scrapy-custom-pipeline-outputting-files-half-the-size-expected/
# https://stackoverflow.com/questions/21009027/split-scrapys-large-csv-file/

import scrapy
from scrapy.exporters import CsvItemExporter
import datetime


class MySpider(scrapy.Spider):

    name = 'myspider'

    # see page created for scraping: http://toscrape.com/
    start_urls = ['http://books.toscrape.com/'] #'http://quotes.toscrape.com']

    def parse(self, response):
        print('url:', response.url)

        # download images and convert to JPG (even if it is already JPG)
        for url in response.css('img::attr(src)').extract():
            url = response.urljoin(url)
            yield {'image_urls': [url], 'session_path': 'hello_world'}


class PartitionedCsvPipeline(object):

    def __init__(self, stats):
        self.filename = "output_{}.csv"
        self.split_limit = 10
        
        self.count = 0
        self.create_exporter()  

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def create_exporter(self):
        now = datetime.datetime.now()
        datetime_stamp = now.strftime("%Y.%m.%d-%H.%M.%S.%f")  # %f for milliseconds because sometimes it can create next file in very short time
        
        self.file = open(self.filename.format(datetime_stamp), 'w+b')
        
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()       

    def finish_exporter(self):
        self.exporter.finish_exporting()
        self.file.close()
    
    def process_item(self, item, spider):

        if self.count >= self.split_limit:
            self.finish_exporter()
            self.count = 0
            self.create_exporter()

        self.exporter.export_item(item)
        self.count += 1
        print('self.count:', self.count)

        return item
        
    def close_spider(self, spider):
        """it is needed to close last file and save data in this file"""
        self.finish_exporter()
        
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    'ITEM_PIPELINES': {'__main__.PartitionedCsvPipeline': 1},   # used Pipeline create in current file (needs __main___)
})

c.crawl(MySpider)
c.start() 
