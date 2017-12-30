#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48017424/1832058
# 

from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

class FilmsLocarnoSpiderSpider(Spider):

    name = 'films_locarno_spider'

    allowed_domains = ['https://pardo.ch/']

    start_urls = []

    count = 0 # to display number of pages

    def start_requests(self):
        url = 'https://pardo.ch/pardo/program/archive/2017/catalog-films.html'
        
        self.driver = webdriver.Firefox()

        self.driver.get(url)
        self.logger.info('Sleeping for 1 second')
        time.sleep(1)
        sel = Selector(text=self.driver.page_source)

        #grab list of start pages for all 4/5 editions of festival available
        #list of film page urls on start page (letter A)
        film_page_urls = sel.xpath('//article/a/@href').extract()
        
        print('urls:', film_page_urls)
        print('urls number:', len(film_page_urls))

        for item in sel.xpath('//article/@class').extract():
            print('class:', item)

        for url in film_page_urls:
            url = 'https://pardo.ch' + url
            yield Request(url, callback=self.parse_filmpage)
    
    def parse_filmpage(self, response):
        self.count += 1
        print('url:', self.count, response.url)

        self.driver.get(response.url)
        self.logger.info('Sleeping for 1 second')
        time.sleep(1)
        sel = Selector(text=self.driver.page_source)
        
        title = sel.xpath('.//h1[@class="article__title"]/text()').extract_first().strip()
        description = sel.xpath('.//div[@itemprop="description"]/p/text()').extract_first().strip()
        director = sel.xpath('.//dd[@class="col-1-offset data-director"]/a/text()').extract_first().strip()
        yield {
            'url': response.url, 
            'title': title,
            'director': director,
            'description': description,
        }        
    
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
c.crawl(FilmsLocarnoSpiderSpider)
c.start()

