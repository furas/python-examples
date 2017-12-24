
#
# https://stackoverflow.com/a/47744135/1832058
# 

import scrapy

#from allegro.items import AllegroItem

#class AllegroItem(scrapy.Item):
#    product_name = scrapy.Field()
#    product_sale_price = scrapy.Field()
#    product_seller = scrapy.Field()
  
class AllegroPrices(scrapy.Spider):
    
    name = "AllegroPrices"
    allowed_domains = ["allegro.pl"]

    start_urls = [
        "http://allegro.pl/diablo-ii-lord-of-destruction-2-pc-big-box-eng-i6896736152.html",
        "http://allegro.pl/diablo-ii-2-pc-dvd-box-eng-i6961686788.html",
        "http://allegro.pl/star-wars-empire-at-war-2006-dvd-box-i6995651106.html",
        "http://allegro.pl/heavy-gear-ii-2-pc-eng-cdkingpl-i7059163114.html"
    ]
    
    def parse(self, response):
        title = response.xpath('//h1[@class="title"]//text()').extract()
        sale_price = response.xpath('//div[@class="price"]//text()').extract()
        seller = response.xpath('//div[@class="btn btn-default btn-user"]/a/span/text()').extract()
    
        title = title[0].strip()
    
        print(title, sale_price, seller)
        
        yield {'title': title, 'price': sale_price, 'seller': seller}
        
        #items = AllegroItem()
        #items['product_name'] = ''.join(title).strip()
        #items['product_sale_price'] = ''.join(sale_price).strip()
        #items['product_seller'] = ''.join(seller).strip()
        #yield items
    
# --- run it as standalone script without project and save in CSV ---

from scrapy.crawler import CrawlerProcess

#c = CrawlerProcess()

c = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'output.csv'
})

c.crawl(AllegroPrices)
c.start()
