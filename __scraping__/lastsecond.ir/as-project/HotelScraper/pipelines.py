# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

class HotelscraperPipeline(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        print('init pipeline args:', args)
        print('init pipeline kwargs:', kwargs)

    #~ @classmethod
    #~ def from_crawler(cls, crawler):
        #~ # Here, you get whatever value was passed through the "table" parameter
        #~ hello = crawler.spider.hello
        #~ print('open_spide: crawler.spider.hello:', crawler.spider.hello)
        
        #~ return cls(hello)
            
    def open_spider(self, spider):
        print('open_spide: spider.hello:', spider.hello)
        self.hello = spider.hello
        
    def process_item(self, item, spider):
        print('process_item: spider.hello:', spider.hello)
        print('process_item: self.hello:', self.hello)
        return item

class DynamicSQLlitePipeline(object):

    def open_spider(self, spider):
        
        print('open_spider:', spider.table)

        try:
            db_path = "sqlite:///"+settings.SETTINGS_PATH+"\\data.db"
            db = dataset.connect(db_path)
            table_name = table[0:3]  # FIRST 3 LETTERS
            self.my_table = db[table_name]
        except Exception as ex:
            print('Error:', ex)
