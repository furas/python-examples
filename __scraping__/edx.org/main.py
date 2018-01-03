#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48067671/1832058
# 

from scrapy.http import Request
from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.loader import ItemLoader
import json

class Course_spider(CrawlSpider):
    
    name = 'CourseSpider'
    allowed_domains = ['www.edx.org']
    start_urls = ['https://www.edx.org/course/?language=Spanish']

    rules = (Rule(LinkExtractor(allow=r'/course'), callback='parse_item', follow='True'),)

    def parse_item(self, response):
        print('parse_item url:', response.url)

        course_id = response.xpath('//*[@id="course-info-page"]/@data-course-id').extract_first()
        if course_id:
            url = 'https://www.edx.org/api/catalog/v2/courses/' + course_id
            yield Request(url, callback=self.parse_json)
            
    def parse_json(self, response):
        print('parse_json url:', response.url)
        
        item = json.loads(response.body)
        
        return item

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #     
})
c.crawl(Course_spider)
c.start()
