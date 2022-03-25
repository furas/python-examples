# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.15
# [python - Scrapy doesn't print anything - Stack Overflow](https://stackoverflow.com/questions/71476860/scrapy-doesnt-print-anything/71478208#71478208)

from scrapy import Spider
from scrapy.http import FormRequest

class ProvinciaSpider(Spider):
    name = 'provincia'
    allowed_domains = ['aduanet.gob.pe']
    start_urls = ['http://www.aduanet.gob.pe/cl-ad-itconsmanifiesto/manifiestoITS01Alias?accion=cargaConsultaManifiesto&tipoConsulta=salidaProvincia']

    def parse(self, response):
        data ={ 'accion': 'consultaManifExpProvincia',
        'salidaPro': 'YES',
        'strMenu': '-',
        'strEmpTransTerrestre': '-',
        'CMc1_Anno': '2022',
        'CMc1_Numero': '96',
        'CG_cadu': '046',
        'viat': '1'}

        yield FormRequest('http://www.aduanet.gob.pe/cl-ad-itconsmanifiesto/manifiestoITS01Alias', formdata=data, callback=self.parse_form_page)
    
    def parse_form_page(self, response):
        table = response.xpath('/html/body/form[1]//td[@class="beta"]/table')
        print('table:', len(table))
        trs = table.xpath('.//tr')[1:]
        print('trs:', len(trs))
        for tr in trs:
            tds = tr.xpath('.//td')
            print('tds:', len(tds))
            if not tds:
                print('empty row')
            else:
                puerto_llegada= tr.xpath('.//td[1]/text()').extract_first().strip()
                pais= tr.xpath('.//td[1]/text()').extract_first().strip()
                bl= tr.xpath('.//td[3]/text()').extract_first().strip()
                peso= tr.xpath('.//td[8]/text()').extract_first().strip()
                bultos= tr.xpath('.//td[9]/text()').extract_first().strip()
                consignatario= tr.xpath('.//td[12]/text()').extract_first().strip()
                embarcador= tr.xpath('.//td[13]/text()').extract_first().strip()
    
                yield {'puerto_llegada': puerto_llegada,
                       'pais': pais,
                       'bl': bl,
                       'peso': peso,
                       'bultos': bultos,
                       'consignatario': consignatario,
                       'embarcador': embarcador}

# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(ProvinciaSpider)
c.start()

