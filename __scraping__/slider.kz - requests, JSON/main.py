# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.18

import requests

# --- list of files to download ----

#
# often server has problem to send data - maybe too many users use it
#

response = requests.get('http://slider.kz/vk_auth.php?q=unravel')

print('text:', response.text[:100])

data = response.json()

for item in data['audios']:
    print(item)

# --- similar artists ---

response = requests.get('https://slider.kz/similar/artist/unravel')

print('text:', response.text[:1000])

data = response.json()

print('key1:', data.keys())
print('key2:', data['similarartists'].keys())
print('key2:', data['similarartists']['artist'][0].keys())

for item in data['similarartists']['artist']:
    print('name:', item['name'])
    print('url:', item['url']) 
    print('image:', item['image'][0]['#text']) 
    print('---')
