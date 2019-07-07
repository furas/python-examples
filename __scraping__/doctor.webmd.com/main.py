#!/usr/bin/env python3

import scrapy

class MySpider(scrapy.Spider):
    
    name = 'myspider'

    #allowed_domains = [''link'']
    start_urls = ['https://doctor.webmd.com/find-a-doctor/specialty/psychiatry/arizona/phoenix?pagenumber=1']

    def parse(self, response):

        doctors_urls =  (response.xpath('//*[@class="doctorName"]//@href').extract())

        for doctor in doctors_urls:
            doctor = response.urljoin(doctor)
            print (doctor) 
            yield scrapy.Request(url=doctor,callback=self.parse_doctor)

        next_page  = response.xpath('//*[@id="next-onRight"]//@href').extract_first() 

        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)

    def parse_doctor(self,response):

        yield {"Name": response.xpath('//*[@class="header"]//*[@itemprop="name"]//text()').extract_first(),
         "Speciality":response.xpath('//*[@itemprop="medicalSpecialty"]//*[@itemprop="name"]//text()').extract_first(),
         "Years of experience":response.xpath('//*[@class="profile-content"]//*[@class="subheader content-body years"]//text()').extract_first(),
         "Employer": response.xpath('//*[@class="address"]//*[@class="practice"]//text()').extract_first(),
         "Address": response.xpath('//*[@itemprop="address"]//*[@itemprop="streetaddress"]//text()').extract(),
         "City": response.xpath('//*[@itemprop="address"]//*[@itemprop="addressLocality"]//text()').extract(),
         "Url": response.url}   
        
# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'output.csv', # 
})
c.crawl(MySpider)
c.start()
