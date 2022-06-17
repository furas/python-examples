# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.09
# [python - Why won't my regular expressions match the following string? - Stack Overflow](https://stackoverflow.com/questions/72560211/why-wont-my-regular-expressions-match-the-following-string/72562216#72562216)

import scrapy
import re

econ_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://pisa.ucsc.edu',
    'Accept-Language': 'en-us',
    'Host': 'pisa.ucsc.edu',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Referer': 'https://pisa.usc.edu/class_search/',
    'Accept-Encoding': ['gzip', 'deflate', 'br'],
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
}


data = {
    'action': 'results',
    'binds[:term]': '2228',
    'binds[:reg_status]': 'all',
    'binds[:subject]': 'ECON',
    'binds[:catalog_nbr_op]': '=',
    'binds[:catalog_nbr]': '',
    'binds[:title]': '',
    'binds[:instr_name_op]': '=',
    'binds[:instructor]': '',
    'binds[:ge]': '',
    'binds[:crse_units_op]': '=',
    'binds[:crse_units_from]': '',
    'binds[:crse_units_to]': '',
    'binds[:crse_units_exact]': '',
    'binds[:days]': '',
    'binds[:times]': '',
    'binds[:acad_career]': '',
    'binds[:asynch]': 'A',
    'binds[:hybrid]': 'H',
    'binds[:synch]': 'S',
    'binds[:person]': 'P',
}

def professor_filter(item):
    return (re.search(r'\w\.', item) or "Staff" in item)

class ClassesSpider(scrapy.Spider):

    name = "classes"

    def start_requests(self):
        urls = ['https://pisa.ucsc.edu/class_search/index.php']
        for url in urls:
            #yield scrapy.Request(url,
            #                     headers=econ_headers,
            #                     body='action=results&binds%5B%3Aterm%5D=2228&binds%5B%3Areg_status%5D=all&binds%5B%3Asubject%5D=ECON&binds%5B%3Acatalog_nbr_op%5D=%3D&binds%5B%3Acatalog_nbr%5D=&binds%5B%3Atitle%5D=&binds%5B%3Ainstr_name_op%5D=%3D&binds%5B%3Ainstructor%5D=&binds%5B%3Age%5D=&binds%5B%3Acrse_units_op%5D=%3D&binds%5B%3Acrse_units_from%5D=&binds%5B%3Acrse_units_to%5D=&binds%5B%3Acrse_units_exact%5D=&binds%5B%3Adays%5D=&binds%5B%3Atimes%5D=&binds%5B%3Aacad_career%5D=&binds%5B%3Aasynch%5D=A&binds%5B%3Ahybrid%5D=H&binds%5B%3Asynch%5D=S&binds%5B%3Aperson%5D=P',
            #                     callback=self.parse)

            yield scrapy.FormRequest(url,
                                 headers=econ_headers,
                                 formdata=data,
                                 callback=self.parse)



    def parse(self, response):

        page = response.url.split("/")[-2]

        all_rows = response.xpath('//div[contains(@id, "rowpanel_")]')

        classDict = {}

        for row in all_rows:
            classname = row.xpath('.//h2//a/text()').re(r'(?i)(\w+\s\w+)+\s-\s\w+\xa0+([\w\s]+\b)')
            professor = row.xpath('(.//div[@class="panel-body"]//div)[3]/text()').get().strip()
            print(classname, professor)
            if professor and professor_filter(professor):
                classDict[tuple(classname)] = [professor]
                yield {'class': tuple(classname), 'professor': professor}  # it will write to file csv

            else:
                print('skip:', professor)

        print(classDict)

        #filename = f'class-{page}.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log(f'Saved file {filename}')


# --- run without project and save in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEEDS': {'output.csv': {'format': 'csv'}},  # new in 2.1
})
c.crawl(ClassesSpider)
c.start()
