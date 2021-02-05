# project/settings.py

```
ITEM_PIPELINES = {
    'project.pipelines.RenameFilesPipeline': 300,
}
FILES_STORE = '.'
```

# project/pipelines.py

```
from scrapy.pipelines.files import FilesPipeline


class RenameFilesPipeline(FilesPipeline):

    # `item` needs `Scrapy 2.4+`
    def file_path(self, request, response=None, info=None, *, item=None):
        """Use `path` from `item` (created in `parse`) to rename downloaded file."""

        return item['path']
```

# project/spiders/myspider.py

```
import scrapy


class MySpider(scrapy.Spider):

    name = 'myspider'

    # ... code ...
```
