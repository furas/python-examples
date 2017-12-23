#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47910852/1832058
#

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Rule, CrawlSpider
#from scrapy.commands.view import open_in_browser

class MySpider(CrawlSpider):

    name = 'MySpider' 

    handle_httpstatus_list = [404, 301, 302, 303]

    all_responses_log = './responses_all.log'
    ok_responses_log  = './responses_ok.log'
    bad_responses_log = './responses_bad.log'
    redirects_responses_log = './responses_redirect.log'

    start_urls = [
        'http://httpbin.org/status/301',
        'http://httpbin.org/status/302',
        'http://httpbin.org/status/303',

        'http://httpbin.org/status/404',
        'http://httpbin.org/status/200',
    ]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_item"
        )
    ]

    def parse(self, response):
        print('parse url:', response.url)

        self.test_status('parse()', response)

    def parse_item(self, response):
        print('parse item url:', response.url)

        self.test_status('parse_item()', response)

        # The list of items that are found on the particular page
        items = []
        res = Selector(response)
        self.append(self.resp_log_file, str(response))
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)

    def test_status(self, text, response):
        try:
            if response.status == 404:
                log = self.bad_responses_log
            elif response.status == 200:
                log = self.ok_responses_log
            #elif 299 < response.status < 400:
            elif response.status in (301, 302, 303, 307):
                log = self.redirects_responses_log
            else:
                log = self.redirects_responses_log

            message = "{} | {} | {}\n".format(response.status, text, response.url)
            self.append(log, message)
        except Exception as e:
            print('Error:', e)

    def append(self, filename, string):
        print('Writing log:', filename)
        with open(filename, 'a') as f:
            f.write(string)


# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(MySpider)
c.start()
