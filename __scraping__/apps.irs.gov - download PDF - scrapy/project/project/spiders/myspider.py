import scrapy


class MySpider(scrapy.Spider):

    name = 'myspider'

    def __init__(self, start=2020, end=2020, *args, **kwargs):  # <--- receive parameters
        """Get parameters `start` and `end`."""

        super().__init__(*args, **kwargs)
        self.start = int(start)  # <--- receive parameter
        self.end   = int(end)    # <--- receive parameter

    def start_requests(self):
        """Generate start requests using parameters `start` and `end`."""
        
        url_pattern = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?criteria=currentYearRevDateString&submitSearch=Find&value={}'

        for year in range(self.start, self.end+1):
            # generate `url` with `year`
            url = url_pattern.format(year)
            # send `year` to `parse` as parameter
            yield scrapy.Request(url, meta={'year': year})
            
    def parse(self, response):
        print('[parse] url:', response.url)
        
        # get `year`
        year = response.meta['year']
        print('[parse] year:', year)
        
        # find links to all PDF in table
        for link in response.xpath('//table[@class="picklist-dataTable"]//td/a'):
            url  = link.xpath('@href').get().strip()
            name = link.xpath('text()').get()
            #print('PDF url :', url)
            #print('PDF name:', name)
            
            # create `path` for downloaded file
            path = 'pdf/{name}/{name} - {year}.pdf'.format(name=name, year=year)

            yield {'file_urls': [url], 'path': path}

        # find link with text `Next`
        next_page = response.xpath('//div[@class="paginationBottom"]/a[contains(text(), "Next")]/@href').get()
        #print('next_page:', next_page)

        if next_page:
            next_page = response.urljoin(next_page)
            #print('next_page:', next_page)
            # send `year` to `parse`
            yield scrapy.Request(next_page, meta={'year': year})

