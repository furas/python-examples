#!/usr/bin/env python3

# Google API for "commentThreads": 
#   https://developers.google.com/youtube/v3/docs/commentThreads/list
#
# Example video on YouTube video to get comments: 
#   https://www.youtube.com/watch?v=oVp1vrfL_w4&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M
#
# Python module for Google API (not used in example)
#   https://github.com/google/google-api-python-client
#
# Google Console for Developers (to register application and get API_KEY)
#   https://console.developers.google.com/

import urllib.request
import urllib.parse
import json

API_KEY = '<YOUR-API-KEY>' 

data = {
    'key': API_KEY,
    'part': 'snippet',
    'videoId': 'oVp1vrfL_w4',
    #'order': 'time',
}

url = 'https://www.googleapis.com/youtube/v3/commentThreads'

params = urllib.parse.urlencode(data)

response = urllib.request.urlopen(url + '?' + params)

result = json.loads(response.read())

for item in result['items']:
    print(item['snippet']['topLevelComment']['snippet']['authorDisplayName'])
    print('---')
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    #print(item['snippet']['topLevelComment']['snippet']['textOriginal'])
    print('====================')
