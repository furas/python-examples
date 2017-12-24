

With `.extract_first()` you always get first link in pagination which is link to first or second page.

Using `.extract()[-1]` you get last link in pagination which directs to next page.

    next_page_url = response.css("li > a.arrow::attr(href)").extract()[-1]

or you can use CSS selector `:last-child` (with `.extract_first()`)

    next_page_url = response.css("li > a.arrow:last-child::attr(href)").extract_first()

or using xpath and `[last()]`

    next_page_url = response.xpath('(//li/a[@class="arrow"]/@href)[last()]').extract_first()

or

    next_page_url = response.xpath('(//li/a[@class="arrow"])[last()]/@href').extract_first()


