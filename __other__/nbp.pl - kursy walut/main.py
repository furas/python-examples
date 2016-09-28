#!/usr/bin/env python3

from lxml import etree

def execute(url):

    html = etree.parse(url)
    #print(etree.tounicode(html))

    root = html.getroot()
    #print(root)

    for tag in root:
        #print('tag:', tag.tag)

        #for subtag in tag:
        #    print('subtag:', subtag.tag, '=', subtag.text)

        if tag.tag == 'pozycja':
            print( [subtag.text for subtag in tag if tag.tag == 'pozycja'] )

        #print('-----')

urls = [
    'http://nbp.pl/kursy/xml/LastA.xml',
    'http://nbp.pl/kursy/xml/LastB.xml',
]

for url in urls:
    execute(url)
