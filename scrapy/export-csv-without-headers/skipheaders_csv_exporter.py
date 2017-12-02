
#!/usr/bin/env python

from scrapy.exporters import CsvItemExporter

'''
You have to set this exporter in settings.py

    FEED_EXPORTERS = {
        'csv': 'your_project_name.exporters.SkipHeadersCsvItemExporter',
    }

And now scrapy should write all csv files without headers.

    scrapy crawl <project> -o <filename.csv>

Or you can set

    FEED_EXPORTERS = {
        'skipheaders': 'your_project_name.exporters.SkipHeadersCsvItemExporter',
    }

and get csv without headers only when you use -t skipheaders

    scrapy crawl <project> -o <filename.csv> -t skipheaders
'''

class SkipHeadersCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):

        # args[0] is file handler to opened file.
        # If file is not empty then skip headers.
        if args[0].tell() > 0:
            kwargs['include_headers_line'] = False

        super(HeadlessCsvItemExporter, self).__init__(*args, **kwargs)

