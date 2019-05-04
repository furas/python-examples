#!/usr/bin/env python3

import scrapy
from scrapy.http import FormRequest

class MySpider(scrapy.Spider):

    name = 'myspider'

    def start_requests(self):
        urls = [
            #'https://www.zomato.com/new-york-city/waldys-wood-fired-pizza-penne-chelsea-manhattan/photos'
            'https://www.zomato.com/new-york-city/cafeteria-chelsea-manhattan/photos'
        ]

        for url in urls:
            #url = url + '?category=food'
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # small images 200x200
        #urls = response.xpath('//div[@id="thumbsContainer"]//img/@data-original').extract()
        #urls = response.xpath('//img[@class="res-photo-thumbnail thumb-load lazy-photo-inner"]/@data-original').extract()
        #yield {'image_urls': urls}

        # big images 800x600
        #urls = [url.replace('200%3A200', '800%3A600') for url in urls]
        #yield {'image_urls': urls}

        # big images 1900x1200
        #urls = [url.replace('200%3A200', '1900%3A1200') for url in urls]
        #yield {'image_urls': urls}

        data = {
            'res_id': '16761868', #, '16780723', # place ID
            'offset': '30',    # change it
            'category':	'all', # 'food'
            'action': 'fetch_photos',
            'index': '30',
            'limit': '10', # chage it
        }

        url = 'https://www.zomato.com/php/load_more_res_pics.php'
        yield FormRequest(url, callback=self.parse_post, formdata=data)

    def parse_post(self, response):

        urls = response.xpath('//img[@class="res-photo-thumbnail thumb-load lazy-photo-inner"]/@data-original').extract()
        urls = [url.replace('\/', '/') for url in urls]

        yield {'image_urls': urls}

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    'IMAGES_STORE': '.',
})

c.crawl(MySpider)
c.start()



