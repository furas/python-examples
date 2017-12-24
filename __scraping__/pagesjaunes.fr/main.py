#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47774713/1832058
#

import scrapy

class MySpider(scrapy.Spider):
    
    name="myspider"
    
    allowed_domains = ["www.pagesjaunes.fr", "www.pagesjaunes.com"]
    
    start_urls = []

    def start_requests(self):
        
        url = 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui={}&ou={}&page={}'

        for page in range(5):
            yield scrapy.Request(url.format('macon', 'bordeaux', page)) #, callback=self.parse)
        
        
    def parse(self, response):

        self.logger.info("%s page visited", response.url)
        
        print('parse url >>>', response.url)
        
        for item in response.css('article'):
            title = item.css('.denomination-links ::text').extract_first().strip()
            tel = item.css('.bi-contact-tel strong ::text').extract_first().strip()
        
            email = item.css('.hidden-phone.SEL-email a ::attr(data-pjlb)').extract_first()
            if email:
                email = email[8:-17]
                email = base64.b64decode(email)
                url = response.joinurl(email)
                yield scrapy.Response(url, callback=parse_email, meta={'title': title, 'tel': tel})
                
            print('title', title, ', tel', tel, 'email:', email)
            
            yield {'title': title, 'tel': tel, 'email:': email}

    def parse_email(self, response):

        print('parse_email url  >>>', response.url)
        print('parse_email meta >>>', response.meta)
        
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'output.csv',
})
c.crawl(MySpider)
c.start()
