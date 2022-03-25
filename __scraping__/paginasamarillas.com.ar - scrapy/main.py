# date: 2022.03.17
# 

from folium import Link
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

class Articulo(Item):
    nombre = Field()
    direccion = Field()
    telefono = Field()
    comunaregion = Field()


class SeccionAmarillaCrawler(CrawlSpider):
    name = 'scraperfunerarias'

    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
    
    allowed_domains = ['paginasamarillas.com.ar']
    start_urls = ["https://www.paginasamarillas.com.ar/buscar/q/funerarias/"]
       
    download_delay = 3 
    
    rules = (
        Rule(
            LinkExtractor(
                #allow=r'https://www.paginasamarillas.com.ar/buscar/q/funerarias/p-\d+/\?tieneCobertura=true'
                allow=r'funerarias/p-\d+
            ), follow=True, callback= "parseador" 
        ),
    )
    
    def parseador(self, response):
        print('url:', response.url)
        sel = Selector(response)
        funerarias = sel.xpath('//div[contains(@class, "figBox")]')
    
        for funeraria in funerarias:
            item = ItemLoader(Articulo(), funeraria)
            item.add_xpath('nombre', './/span[@class="semibold"]/text()', MapCompose(lambda i: i.replace('\n','').replace('\r','').replace('\t','').strip()))
            item.add_xpath('direccion', './/span[@class="directionFig"]/text()', MapCompose(lambda i: i.replace('\n','').replace('\r','').replace('\t','').strip()))
            item.add_xpath('telefono', './/span[@itemprop="telephone"]/text()', MapCompose(lambda i: i.replace('\n','').replace('\r','').replace('\t','').strip()))
            item.add_xpath('comunaregion', './/span[@class="city"]/text()', MapCompose(lambda i: i.replace('\n','').replace('\r','').replace('\t','').strip()))
    
            yield item.load_item()
    
#---------------------------------------------------------------------------

process = CrawlerProcess({
     'FEED_FORMAT': 'csv',
     'FEED_URI': 'output.csv'
})
process.crawl(SeccionAmarillaCrawler)
process.start()
