
Template for standalone scrapy with

- run as standalone script using `scrapy.crawler.CrawlerProcess()`
- generate urls at start `start_requests()`
- save data in CSV or JSON `'FEED_FORMAT', 'FEED_URI'`
- download files  `'ITEM_PIPELINES', 'FILES_STORE', yield {'file_urls': [url]}`
- download images `'ITEM_PIPELINES', 'IMAGES_STORE', yield {'image_urls': [url]}`
- send `meta` data to next parser
- open html in web browser
- convert `response.body` to `json`
- save every response.boy in separated file

