I use [http://quotes.toscrape.com](http://quotes.toscrape.com) to get some data.

I get tags in `parse` and send every tag to second request (using `meta=`) 
And then in `parse_quote` I create one element with one tag and many quotes.
Finally I yield this as one item.

It gives

    <?xml version="1.0" encoding="utf-8"?>
    <items>
        <item>
            <Tag books>
                <value>“The perso ...</value>
                <value>“Good frie ...</value>
                <value>“I have al ...</value>
            </Tag books>
        </item>
        <item>
            <Tag humor>
                <value>“The perso ...</value>
                <value>“A day wit ...</value>
                <value>“Anyone wh ...</value>
            </Tag humor>
        </item>
        <item>
            <Tag life>
                <value>“There are ...</value>
                <value>“It is bet ...</value>
                <value>“This life ...</value>
            </Tag life>
        </item>
    </items>

Maybe with own exporter I could change `<value>` into `<quote>` and remove `<item>` 

(example: [Formatting Scrapy's output to XML](https://stackoverflow.com/questions/13962881/formatting-scrapys-output-to-xml)

