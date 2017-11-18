# -*- coding: utf-8 -*-
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['blog.furas.pl']
    start_urls = ['http://blog.furas.pl/category/python.html','http://blog.furas.pl/category/html.html','http://blog.furas.pl/category/linux.html']

    def parse(self, response):
        
        # get category from url
        category = response.url.split('/')[-1][:-5]

        urls = response.css('article a::attr(href)').extract() # links to den subpages
        
        for url in urls:
            # skip some urls
            if ('/tag/' not in url) and ('/category/' not in url):
                url = response.urljoin(url)
                # add category (as meta) to send it to callback function
                yield scrapy.Request(url=url, callback=self.parse_details, meta={'category': category})

    def parse_details(self, response):

        # get category
        category = response.meta['category']

        # get only first title (or empty string '') and strip it
        title = response.css('h1.entry-title a::text').extract_first('')
        title = title.strip()
        
        # get only first date (or empty string '') and strip it
        date = response.css('.published::text').extract_first('')
        date = date.strip()
        
        yield {
            'Title': title,
            'Date': date,
            'Category': category,
        }
