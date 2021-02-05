# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter

from scrapy.pipelines.files import FilesPipeline


class RenameFilesPipeline(FilesPipeline):

    # `item` needs `Scrapy 2.4+`
    def file_path(self, request, response=None, info=None, *, item=None):
        """Use `path` from `item` (created in `parse`) to rename downloaded file."""
        
        return item['path']
