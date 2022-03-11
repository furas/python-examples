# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.10
# ?

import scrapy
from scrapy.crawler import CrawlerProcess

class dgtest2(scrapy.Spider):
    name = 'dgtest2'
    start_urls = ['https://careers.infinity.aero/Careers.aspx']

    custom_settings = {
        'FEEDS': {
            'output.csv': {
                'format': 'csv',
                'item_export_kwargs': {
                   'include_headers_line': False,
                }
            }
        },  # new in 2.1
    }

    def parse(self, response):
        for url in response.xpath('//a/@href').getall():
            yield {
               'url': response.urljoin(url),
            }
    
process = CrawlerProcess()
process.crawl(dgtest2)
process.start()

