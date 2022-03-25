# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.13
# [python - How to make allowed domain dynamic using Scrapy? - Stack Overflow](https://stackoverflow.com/questions/71446581/how-to-make-allowed-domain-dynamic-using-scrapy/71453753#71453753)

import scrapy
import urllib.parse

class SeleniumSpider(scrapy.Spider):
    name = 'test_selenium'

    #allowed_domains=['quotes.toscrape.com']

    start_urls = ['https://quotes.toscrape.com/page/1/']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        allowed = set()  # `set()` to keep every domain only once

        for url in self.start_urls:
            parts = urllib.parse.urlparse(url)
            #print(parts)
            allowed.add( parts.netloc )

        self.allowed_domains = list(allowed)

        for domain in self.allowed_domains:
            print("allowed:", domain)
    def parse(self, response):
        print('parse url:', response.url)

        for a in response.xpath('//a/@href'):
            yield response.follow(a)
        
# --- run without project ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess()
c.crawl(SeleniumSpider)
c.start()

