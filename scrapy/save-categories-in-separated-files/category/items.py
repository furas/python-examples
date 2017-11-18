# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CategoryItem(scrapy.Item):
    Title = scrapy.Field()
    Date = scrapy.Field()
    # extra field used as filename 
    Category = scrapy.Field()
