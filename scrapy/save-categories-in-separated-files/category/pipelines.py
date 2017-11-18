# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class CategoryPipeline(object):
    
    def process_item(self, item, spider):
        
        # get category and use it as filename
        filename = item['Category'] + '.csv'
        
        # open file for appending
        with open(filename, 'a') as f:
            writer = csv.writer(f)

            # write only selected elements 
            row = [item['Title'], item['Date']]
            writer.writerow(row)

            #write all data in row
            #warning: item is dictionary so item.values() don't have to return always values in the same order
            #writer.writerow(item.values())
            
        return item
