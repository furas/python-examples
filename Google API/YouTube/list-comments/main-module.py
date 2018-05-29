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

import googleapiclient.discovery

API_KEY = '<YOUR-API-KEY>'

service = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

data = {
    'part': 'snippet',
    'videoId': 'oVp1vrfL_w4',
    #'order': 'time',
}

request = service.commentThreads().list(**data)
#request = service.commentThreads().list(part='snippet', videoId='oVp1vrfL_w4')

result = request.execute()

for item in result['items']:
    print(item['snippet']['topLevelComment']['snippet']['authorDisplayName'])
    print('---')
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    #print(item['snippet']['topLevelComment']['snippet']['textOriginal'])
    print('====================')
