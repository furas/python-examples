#!/usr/bin/env python3

# using regex "a|b" to find tags

html = '''<foo>
    <a>Hello</a>
    <b>World</b>
    <c>Python</c>
</foo>'''

import lxml.html

data = lxml.html.fromstring(html)

result = data.xpath('./*[re:match(local-name(), "a|b")]',
                    namespaces={'re':"http://exslt.org/regular-expressions"})

print(result)

print(list(x.tag for x in result))

print(list(x.text for x in result))
