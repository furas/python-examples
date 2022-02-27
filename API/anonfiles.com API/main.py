# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.23
# [Uploading to anonfiles API with curl in python - Stack Overflow](https://stackoverflow.com/questions/71243221/uploading-to-anonfiles-api-with-curl-in-python/)


import requests

files = {
    'file': ('file.txt', open('file.txt', 'rb')),
}

url = 'https://api.anonfiles.com/upload'
response = requests.post(url, files=files)

data = response.json()

print(data['data']['file']['url']['short'])

