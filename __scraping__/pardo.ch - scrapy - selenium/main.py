#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48017424/1832058
# 

import scrapy


class MySpider(scrapy.Spider):

    name = 'myspider'

    allowed_domains = ['https://pardo.ch']
    start_urls = ['https://pardo.ch/pardo/program/archive/2017/catalog-films.html']

    count = 0 # to display number of pages

    def parse(self, response):
        all_urls = response.xpath('//article/a/@href').extract()
        
        print('urls number:', len(all_urls))

        for url in all_urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_filmpage, dont_filter=True)
    
    def parse_filmpage(self, response):
        self.count += 1
        print('url:', self.count, response.url)

        title = response.xpath('.//h1[@class="article__title"]/text()').extract_first().strip()
        description = response.xpath('.//div[@itemprop="description"]/p/text()').extract_first().strip()
        director = response.xpath('.//dd[@class="col-1-offset data-director"]/a/text()').extract_first().strip()
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
c.crawl(MySpider)
c.start()

