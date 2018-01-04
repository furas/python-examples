
#
# https://stackoverflow.com/a/48078358/1832058
# 

import requests
from lxml import html

s = requests.session()

result = s.get("http://forum.toribash.com/tori_spy.php")
tree = html.fromstring(result.content)

for script in tree.xpath("//script"):
    if script.text and 'highestid' in script.text:
        highestid = script.text.split('\n')[3]
        highestid = highestid[13:-1]
        print('highestid:', highestid)

        result = s.get('http://forum.toribash.com/vaispy.php?do=xml&last='+highestid, headers=dict(referer=url))
        #print(result.text)
        data = html.fromstring(result.content)

        for item in data.xpath('.//event'):
            print('--- event ---')
            print('id:', item.xpath('.//id')[0].text)
            print('postid:', item.xpath('.//postid')[0].text)
            print(item.xpath('.//preview')[0].text)
