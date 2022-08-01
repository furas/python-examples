# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.30
# [python - Unshapable list error when scraping information - Stack Overflow](https://stackoverflow.com/questions/72810484/unshapable-list-error-when-scraping-information/)

import scrapy
from scrapy.crawler import CrawlerProcess

class TestSpider(scrapy.Spider):

    name = 'test'

    start_urls = [
        #'https://rejestradwokatow.pl/adwokat/list/strona/1/sta/2,3,9',
        'https://rejestradwokatow.pl/adwokat/abaewicz-agnieszka-51004',
        'https://rejestradwokatow.pl/adwokat/adach-micha-55082',
    ]

    custom_settings = {
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOAD_DELAY': 1,
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    def parse(self, response):
        wev = {
            'Status:': '',
            'Data wpisu w aktualnej izbie na listę adwokatów:': '',
            'Stary nr wpisu:': '',
            'Adres do korespondencji:': '',
            'Fax:': '',
            'Email:': '',
        }

        tic = response.xpath("//div[@class='line_list_K']//div//span//text()").getall()
        det = response.xpath("//div[@class='line_list_K']//div//div//text()").getall()

        #print(tic)
        #print(det)
        #print('---')

        all_rows = response.xpath("//div[@class='line_list_K']/div")

        for row in all_rows:
            name  = row.xpath(".//span/text()").get()
            value = row.xpath(".//div/text()").get()
            if name and value:
                wev[name.strip()] = value.strip()
            elif name and name.strip() == 'Email:':
                # <div class="address_e" data-ea="adwokat.adach" data-eb="gmail.com"></div>
                div = row.xpath('./div')
                email_a = div.attrib['data-ea']
                email_b = div.attrib['data-eb']
                wev[name.strip()] = f'{email_a}@{email_b}'

        print(wev)

        yield wev

# --- run without creating project and save results in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    #'USER_AGENT': 'Mozilla/5.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(TestSpider)
c.start()

