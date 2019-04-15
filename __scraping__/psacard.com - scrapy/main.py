
# date: 2019.04.08
# https://stackoverflow.com/questions/55576576/scraping-table-with-scrapy

import scrapy


class PsaSpider(scrapy.Spider):
    name = 'psa'
    allowed_domains = ['psacard.com']
    start_urls = ['https://www.psacard.com/pop/t206/']

    def parse(self, response):
        rows = response.css('table.pop-grid tbody tr')
        
        
        for row in rows:
            yield {
            'name':    row.css('td')[0].css('span.t206-pop-title::text').extract_first(default='').strip(),
            'variety': row.css('td')[0].css('span.variety::text').extract_first(default='').strip(),
            'auth' :  [x.strip() for x in row.xpath('td[3]//text()').extract()],
            'psa1':   [x.strip() for x in row.xpath('td[4]//text()').extract()],
            'psa1.5': [x.strip() for x in row.xpath('td[5]//text()').extract()],
            'psa2':   [x.strip() for x in row.xpath('td[6]//text()').extract()],
            'psa3':   [x.strip() for x in row.xpath('td[7]//text()').extract()],
            'psa4':   [x.strip() for x in row.xpath('td[8]//text()').extract()],
            'psa5':   [x.strip() for x in row.xpath('td[9]//text()').extract()],
            'psa6':   [x.strip() for x in row.xpath('td[10]//text()').extract()],
            'psa7':   [x.strip() for x in row.xpath('td[11]//text()').extract()],
            'psa8':   [x.strip() for x in row.xpath('td[12]//text()').extract()],
            'psa9':   [x.strip() for x in row.xpath('td[13]//text()').extract()],
            'psa10':  [x.strip() for x in row.xpath('td[14]//text()').extract()],
            'total':  [x.strip() for x in row.xpath('td[14]//text()').extract()],
            }
