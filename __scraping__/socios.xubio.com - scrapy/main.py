import scrapy


class XubioContadoresSpider(scrapy.Spider):

    name = "XubioContadores"
    
    start_urls = [
        f'https://socios.xubio.com/ar/contadores/?pag={i}' for i in range(1, 10)
    ]

    def parse(self, response):
        print('url:', response.url)
        
        for box in response.xpath('//div[@class="w-100 padding-15 "]'):

            name = box.xpath('.//div[@class="col-11"]//p//text()').extract_first()
            phone = box.xpath('.//div[@class="col-md-2 col-12 h-60"]//p//text()').extract_first()
            address = box.xpath('.//div[@class="col-md-4 col-12 h-60"]//p//text()').extract_first()
            email = box.xpath('.//div[@class="col-md-3 col-12 h-60"]//p//text()').extract_first()

            item = dict()
            
            item['name'] = name
            item['phone'] = phone
            item['address'] = address
            item['email'] = email

            yield item
            
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(XubioContadoresSpider)
c.start()             
