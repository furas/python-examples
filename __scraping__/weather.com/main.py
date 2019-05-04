
# date: 2019.04.22
# https://stackoverflow.com/questions/55790002/attempting-to-grab-certain-elements/55790313#55790313

import requests
import lxml.html

html = requests.get("https://weather.com/weather/tenday/l/USCA1037:1:US")

element_object = lxml.html.fromstring(html.content)
table = element_object.xpath('//div[@class="twc-table-scroller"]')[0]

td = table.xpath('.//tr/td[@class="twc-sticky-col"]/@title')
print(td)
