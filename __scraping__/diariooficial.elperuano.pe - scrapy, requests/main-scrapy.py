# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.09
# [javascript - Web Scraping Journal "El Peruano" - Python/Scrapy - Stack Overflow](https://stackoverflow.com/questions/71402424/web-scraping-journal-el-peruano-python-scrapy/71403407#71403407)

import scrapy

class SpiderPeruano(scrapy.Spider):
    name = "peruano"
    
    start_urls = [
        "https://diariooficial.elperuano.pe/Normas"
    ]

    custom_settings= {
        "FEED_URI": "peruano.json",
        "FEED_FORMAT": "json",
        "FEED_EXPORT_ENCODING": "utf-8"
    }

    def parse(self, response):
        print('[parse] url:', response.url)

        yield scrapy.FormRequest.from_response(
                    response,                    
                    formxpath= "//form[@id='space_PortalNormasLegalesN']",
                    formdata={"cddesde": "03/01/2022", "cdhasta": "03/03/2022", "btnBuscar":""},
                    dont_click=True,
                    dont_filter=True,
                    #headers={'Referer':"https://diariooficial.elperuano.pe/Normas", 'X-Requested-With': 'XMLHttpRequest'},
                    callback=self.parse_result
               )

    def parse_result(self, response):
        print('[parse_result] url:', response.url)
    
        links = response.xpath("//div[@class='ediciones_texto']/h5/a/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_link)


    def parse_link(self, response):
        print('[parse_link] url:', response.url)
        
        title = response.xpath("//div[@class='story']/h1[@class='sumilla']/text()").get()
        num = response.xpath("//div[@class='story']/h2[@class='resoluci-n']/text()").getall()
        body = response.xpath("//div[@class='story']/p/text()").getall()

        yield {
            "title": title,
            "num": num,
            "body": body
        }

# --- run without project ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
    # save in file CSV, JSON or XML
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(SpiderPeruano)
c.start() 

