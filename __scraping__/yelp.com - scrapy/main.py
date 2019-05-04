#!/usr/bin/env python3

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'

    def start_requests(self):
        urls = ['https://www.yelp.com/biz_photos/ess-a-bagel-new-york']

        for url in urls:
            url = url + '?category=food'
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # small versions
        images = response.xpath('//div[@class="media-landing_gallery photos"]//img[@class="photo-box-img"]/@src ').extract()
        #yield {'image_urls': images}

        # big versions
        images = [url.replace('258s.jpg', 'o.jpg') for url in images]
        yield {'image_urls': images}

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    #'USER_AGENT': 'Mozilla/5.0',
    'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    'IMAGES_STORE': '.',
})

c.crawl(MySpider)
c.start()
