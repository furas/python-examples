#!/usr/bin/env python3

#  ./main.py > open-fm.xspf

#   config: http://open.fm/api/jelonek/configs?version=1.98.0003&platform=web&platformType=web
# stations: http://open.fm/api/static/stations/stations.json
# channels: http://open.fm/api/api-ext/v2/channels/medium.json
#   stream: http://stream.open.fm/%id
#  dawniej: http://gr-relay-16.gaduradio.pl/%id
import requests

import requests

r = requests.get('http://open.fm/api/static/stations/stations.json')

data = [(channel['id'], channel['name']) for channel in r.json()['channels']]

data = sorted(data, key=lambda x:x[1])

print('''<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
  <title>open.fm</title>
  <trackList>
''')
    
for id_, name in data:
    #print('http://gr-relay-16.gaduradio.pl/%-3s --- %s' % (id_, name))
    print('''    <track>
      <album>%s</album>
      <location>http://stream.open.fm/%s</location>
    </track>'''  % (name, id_))

print('''  </trackList>
</playlist>''')

"""
http://open.fm/cover/100x100/e19f7f000001000000000000000056fa5130080a98880000

{"result": {
    "configs": [
        {
            "streams": {
                "relay": "http://stream.open.fm"
            },
            "gemius_stream": {
                "tree": "1",
                "id": "nLFFZoBhPdl7FuSzo2qH15dQPzgsAvu5HaNPr91UpPv.o7",
                "hit_collector": "http://ggspl.hit.gemius.pl",
                "additional": {
                    "GA": "1.1"
                }
            },
            "votes": {
                "vote_for": "http://open.fm/api/api-ext/vote_for_song",
                "vote_against": "http://open.fm/api/api-ext/vote_against_song"
            },
            "ads": {
                    "goldbach": {
                        "prerolls_template": "http://go.goldbachpoland.bbelements.com/please/showit/7105/%(id)/1/43/?typkodu=js&_xml=1"
                    }
                },
            "channels": {
                "list": "http://open.fm/api/static/stations/stations.json",
                "logos": {
                    "square_black": "http://open.fm/logo/%(width)x%(height)/%(id)",
                    "square_white": "http://open.fm/logo/%(width)x%(height)/%(id)"
                },
                "current_stream": "http://open.fm/api/currenttrack/%(id)",
                "playlists": {
                    "album_cover": "http://open.fm/cover/%(width)x%(height)/%(id)",
                    "single_channel": {
                        "short": "http://open.fm/api/api-ext/v2/channels/%(id)/short.json",
                        "long": "http://open.fm/api/api-ext/v2/channels/%(id)/long.json",
                        "medium": "http://open.fm/api/api-ext/v2/channels/%(id)/medium.json"
                    },
                    "all_channels": {
                        "short": "http://open.fm/api/api-ext/v2/channels/short.json",
                        "medium": "http://open.fm/api/api-ext/v2/channels/medium.json",
                        "long": "http://open.fm/api/api-ext/v2/channels/long.json"
                    }
                }
            }
        }
    ],
    "type": "static",
    "revision": "133",
    "argsHash": "",
    "status": 0
}}
"""
