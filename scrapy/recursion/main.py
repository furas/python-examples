# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.10
# [python - Scrapy: How to efficiently follow nested links with similar css selectors? - Stack Overflow](https://stackoverflow.com/questions/71407737/scrapy-how-to-efficiently-follow-nested-links-with-similar-css-selectors/)

import scrapy

class SampleSpider(scrapy.Spider):
    name = "sample"
    
    start_urls = ["https://quotes.toscrape.com/"]

    road = [
        'a[class="tag"][href*=inspirational]::attr(href)',
        'a[class="tag"][href*=life]::attr(href)',
        'a[class="tag"][href*=yourself]::attr(href)',
    ]
    
    def start_requests(self):
        """Run starting URL with full road."""
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_recurse, cb_kwargs={"road": self.road})
        
    def parse_recurse(self, response, road):
        """If road is not empty then send to parse_recurse with smaller road.
           If road is empty then send to parse."""

        first = road[0]
        rest  = road[1:]
        
        links = response.css(first).extract()
        
        if rest:
            # repeat recursion
            for link in links:
                yield response.follow(link, callback=self.parse_recurse, cb_kwargs={"road": rest})
        else:
            # exit recursion
            for link in links:
                yield response.follow(link, callback=self.parse)
            
    def parse(self, response):
        for resp in response.css('span[itemprop="text"]::text').extract():
            print(resp)
            
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(SampleSpider)
c.start() 
