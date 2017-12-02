#!/usr/bin/env python

from scrapy.exporters import CsvItemExporter

'''
You have to set this exporter in settings.py

    FEED_EXPORTERS = {
        'csv': 'your_project_name.exporters.HeaderslessCsvItemExporter',
    }

And now scrapy should write all csv files without headers.

    scrapy crawl <project> -o <filename.csv>

Or you can set

    FEED_EXPORTERS = {
        'headerless': 'your_project_name.exporters.HeaderslessCsvItemExporter',
    }

and get csv without headers only when you use -t headerless

    scrapy crawl <project> -o <filename.csv> -t headerless
'''

class HeaderslessCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['include_headers_line'] = False
        super(HeaderslessCsvItemExporter, self).__init__(*args, **kwargs)

