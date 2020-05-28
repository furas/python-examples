#!/usr/bin/env python3

# date: 2020.05.21
# https://stackoverflow.com/questions/61935547/saving-output-the-to-json-format/

import scrapy
from webpreview import OpenGraph

class News18SSpider(scrapy.Spider):

    name = 'news18_story'
    page_number = 1
    start_urls = ['https://www.news18.com/movies/page-{}/'.format(number) for number in range(1, 21)]

    def parse(self, response):
        all_hrefs = response.xpath('//div[@class="blog-list-blog"]/p/a/@href').getall()

        for href in all_hrefs:
            og = OpenGraph(href, ["og:title", "og:description", "og:image", "og:url"])

            yield {
                "page_title": og.title,
                "description": og.description,
                "image_url": og.image,
                "post_url": og.url
            } 


# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'json',     # csv, json, xml
    'FEED_URI': 'output.json', #
})
c.crawl(News18SSpider)
c.start() 
