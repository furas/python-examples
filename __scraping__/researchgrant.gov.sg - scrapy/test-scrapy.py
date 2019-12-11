#!/usr/bin/env python3

# date: 2019.12.07
# https://stackoverflow.com/questions/59259699/scrapy-formrequest-parameter-not-working-but-showing-all-result-instead/
# page: https://researchgrant.gov.sg/eservices/advanced-search/

import scrapy
import urllib.parse

class MySpider(scrapy.Spider):

    name = 'myspider'
    #allowed_domains = []

    params = {
        'name': 'advancesearchawardedprojectsp'
    }

    args = {
        'keyword': '',
        'source': 'sharepoint',
        'type': 'project',
        'status': 'open',
        'page': 1,
        '_pp_projectstatus': '',

        #'_pp_hiname': 'tan',
        #'_pp_piname': '',
        '_pp_hiname': 'ab',
        '_pp_piname': '', #'pua',

        '_pp_source': '',
        '_pp_details': '',
    }

    def start_requests(self):
        
        # create request for first page
        args = urllib.parse.urlencode(self.args)

        url = 'https://researchgrant.gov.sg/eservices/mvcgrid?' + args

        yield scrapy.FormRequest(url, callback=self.parse_item, method='POST', formdata=self.params, headers={'X-Requested-With': 'XMLHttpRequest'})
        

    def parse_item(self,response):
        #print('parse_item] url:', response.url)
        #print('parse_item] text:', response.text)

        #for quote in response.xpath('//div[contains(@style,"overflow-x:auto")]'):
        #    for row in quote.xpath('./table[contains(@class,"table-striped")]/tbody/tr'):
        #        link = row.xpath('td[1]/a/@href').extract_first()
        #        yield scrapy.Request(link, callback=self.parse_product)

        for row in response.xpath('//table[@name="MVCGridTable_advancesearchawardedprojectsp"]/tbody/tr'):
            link = row.xpath('.//a/@href').get()
            #title = row.xpath('.//a/text()').get()
            yield scrapy.Request(link, callback=self.parse_product)

        # create request for next page
        onclick = response.xpath('//a[@aria-label="Next page"]/@onclick').get()
        
        if onclick:
            # next page 
            self.args['page'] += 1
            args = urllib.parse.urlencode(self.args)
            url = 'https://researchgrant.gov.sg/eservices/mvcgrid?' + args
            yield scrapy.FormRequest(url, callback=self.parse_item, method='POST', formdata=self.params, headers={'X-Requested-With': 'XMLHttpRequest'})

    def parse_product(self, response):
        #print('parse_product] url:', response.url)

        # .extract_first() or .get() instead of .extract()
        project_id = response.xpath('//span[@id="ctl00_ctl47_g_b43c0a74_fae0_498f_b75e_c103772db011_ctl00_lblProjIdExt"]/text()').get()
        title = response.xpath('//span[@id="ctl00_ctl47_g_b43c0a74_fae0_498f_b75e_c103772db011_ctl00_lblProjectTitle"]/text()').get()
        pi = response.xpath('//span[@id="ctl00_ctl47_g_b43c0a74_fae0_498f_b75e_c103772db011_ctl00_lblLeadPIName"]/text()').get()
        hi = response.xpath('//span[@id="ctl00_ctl47_g_b43c0a74_fae0_498f_b75e_c103772db011_ctl00_lblHostInstName"]/text()').get()
        date = response.xpath('//span[@id="ctl00_ctl47_g_b43c0a74_fae0_498f_b75e_c103772db011_ctl00_dtPickerStartDate"]/text()').get()
        # etc.
                
        item = {
            'id': project_id,
            'title': title,
            'pi': pi,
            'hi': hi,
            'date': date,
        }

        yield item

# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    # save in file CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', #
})
c.crawl(MySpider)
c.start()
