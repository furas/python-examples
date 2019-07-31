#!/usr/bin/env python3

# date: 2019.07.29
# https://stackoverflow.com/questions/57245315/using-scrapy-how-to-download-pdf-files-from-some-extracted-links

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = [
          'https://www.alloschool.com/course/alriadhiat-alaol-ibtdaii',
    ]

    def parse(self, response):
        
        for link in response.css('.default .er').xpath('@href').extract():
             url = response.url
             path = response.css('ol.breadcrumb li a::text').extract()
             next_link = response.urljoin(link)
             yield scrapy.Request(next_link, callback=self.parse_det, meta={'url': url, 'path': path})

    def parse_det(self, response):

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'path':response.meta['path'],
            'file_urls': [extract_with_css('a.btn.btn-primary::attr(href)')],
            'url':response.meta['url']
        }

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
})
c.crawl(MySpider)
c.start()
