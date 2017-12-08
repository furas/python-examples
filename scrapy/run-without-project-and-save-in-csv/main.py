#!/usr/bin/env python3

import scrapy
 
class MySpider(scrapy.Spider):

    name = 'myspider'
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
 
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
 
# --- run it without project ---

import scrapy.crawler

c = scrapy.crawler.CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'data.csv'
})
c.crawl(MySpider)
c.start()
