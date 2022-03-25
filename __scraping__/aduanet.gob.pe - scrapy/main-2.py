# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.15
# [javascript - Links doesn't have url format in order to scrape them scrapy - Stack Overflow](https://stackoverflow.com/questions/71504331/links-doesnt-have-url-format-in-order-to-scrape-them-scrapy/)

import scrapy
from scrapy import Spider
from scrapy.http import FormRequest

class ProvinciaSpider(Spider):
    
    name = 'provincia'
    allowed_domains = ['aduanet.gob.pe']
    start_urls = ['http://www.aduanet.gob.pe/cl-ad-itconsmanifiesto/manifiestoITS01Alias?accion=cargaConsultaManifiesto&tipoConsulta=salidaProvincia']

    def parse(self, response):
        payload = {
            'accion': 'consultaManifExpProvincia',
            'salidaPro': 'YES',
            'strMenu': '-',
            'strEmpTransTerrestre': '-',
            'CMc1_Anno': '2022',
            'CMc1_Numero': '96',
            'CG_cadu': '046',
            'viat': '1'
        }

        yield FormRequest('http://www.aduanet.gob.pe/cl-ad-itconsmanifiesto/manifiestoITS01Alias',
                          formdata=payload,
                          callback=self.parse_form_page)

    def parse_form_page(self, response):
        print('[parse_form_page] url:', response.url)
        
        table = response.xpath('/html/body/form[1]//td[@class="beta"]/table')
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
            item = {
                'puerto_llegada': tr.xpath('.//td[1]/text()').extract_first().strip(),
                'pais': tr.xpath('.//td[1]/text()').extract_first().strip(),
                'bl': tr.xpath('.//td[3]/text()').extract_first().strip(),
                'peso': tr.xpath('.//td[8]/text()').extract_first().strip().replace(',', ''),    # <---
                'bultos': tr.xpath('.//td[9]/text()').extract_first().strip().replace(',', ''),  # <---
                'consignatario': tr.xpath('.//td[12]/text()').extract_first().strip(),
                'embarcador': tr.xpath('.//td[13]/text()').extract_first().strip(),
            }

            number = tr.xpath('.//td[4]/a/text()').get().strip()
            print(number.strip())
            
            payload = {
                'accion': "consultaManifExpProvinciaDetalle",
                'CMc2_Anno': "2022",
                'CMc2_Numero': "96",  # it can be without spaces but it can't have `+` - "+++96"
                'CG_cadu': "046",
                'CMc2_viatra': "1",
                'CMc2_numcon': "",
                'CMc2_NumDet': number,   # <---
                'tipo_archivo': "",
                'reporte': "ExpPro",
                'backPage': "ConsulManifExpPro",
            }

            yield FormRequest('http://www.aduanet.gob.pe/cl-ad-itconsmanifiesto/manifiestoITS01Alias',
                              formdata=payload,
                              callback=self.parse_categories,
                              meta={"item": item})
        
    def parse_categories(self, response):
        print('[parse_form_page] url:', response.url)

        item = response.meta['item']

        table = response.xpath('//table[./tr/th[contains(text(), "Descripcion")]]')
        print('len(table):', len(table))

        trs = table.xpath('.//tr')[1:]
        print('len(trs):', len(trs))
        
        for tr in trs[:1]:
            item['descripcion'] = tr.xpath('.//td[7]/text()').extract_first().strip()
            yield item

# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(ProvinciaSpider)
c.start() 
