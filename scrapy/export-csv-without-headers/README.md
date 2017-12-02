

There is `include_headers_line=True` in `CsvItemExporter` but I don't know how to use it directly. 

http://doc.scrapy.org/en/latest/topics/exporters.html#csvitemexporter


But you can create own exporter with `include_headers_line=False` in file `exporters.py` (in the same folder as `settings.py` and `items.py`)

```python
from scrapy.exporters import CsvItemExporter


class HeaderlessCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['include_headers_line'] = False
        super(HeaderlessCsvItemExporter, self).__init__(*args, **kwargs)
```

Then you have to set this exporter in `settings.py`

```python
FEED_EXPORTERS = {
    'csv': 'your_project_name.exporters.HeaderlessCsvItemExporter',
}
```

And now scrapy should write all csv files without headers.

```bash
scrapy crawl <project> -o <filename.csv>
```

Or you can set

```python`
FEED_EXPORTERS = {
    'headerless': 'your_project_name.exporters.HeaderlessCsvItemExporter',
}
```

and get csv without headers only when you use `-t headerless`

```bash
scrapy crawl <project> -o <filename.csv> -t headerless
```

> ps. don't forget to use your project name in place of `your_project_name` in `setttings.py`

---

EDIT:

Now exporter skips headers only if file is not empty (if file.tell() > 0)

```python
from scrapy.exporters import CsvItemExporter

class SkipHeadersCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):

        # args[0] is (opened) file handler
        # if file is not empty then skip headers
        if args[0].tell() > 0:
            kwargs['include_headers_line'] = False

        super(SkipHeaders, self).__init__(*args, **kwargs)
```
