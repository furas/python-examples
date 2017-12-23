#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47761077/1832058
#

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    allowed_domains = ['www.lequipe.fr']

    start_urls = ['http://www.lequipe.fr/Basket/RES_NBA.html']

    def parse(self, response):
        print('url:', response.url)

        for item in response.xpath('//*[@class="filtrecalendrier"]/option/@value'): 

            url = response.urljoin(item.extract())
            #print(url)

            yield scrapy.Request(url, callback=self.parse_items)
            
    def parse_items(self, response):
        rows = response.css('.ligne')
        
        for row in rows:
            
            item = {
                'equipe_dom': row.css('.equipeDom a::text').extract_first(),
                'score_dom':  row.css('div.score span.score--chiffre::text').extract_first(),
                'score_ext':  row.css('div.score span.score--chiffre.gange::text').extract_first(),
                'equipe_ext': row.css('.equipeExt a::text').extract_first(),
                'classement_dom': row.css('.equipeDom a span::text').extract_first(),
                'classement_ext': row.css('.equipeExt a span::text').extract_first(),
            }

            #print(item)
            
            yield item
    
# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(MySpider)
c.start()

'''
Result

/Basket/BasketResultat22420.html
/Basket/BasketResultat22421.html
/Basket/BasketResultat22422.html
...
'''

