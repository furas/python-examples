import requests
import os

#base = 'http://127.0.0.1:5000'
base = 'https://nb9h0e6cs7.execute-api.eu-central-1.amazonaws.com/dev'

def to_file(data):
    url = base + '/file'
    print('  url:', url)

    res = requests.post(url=url, files={'file': ('input.pdf', data)})

    return res

def to_binary(data):
    url = base + '/binary'
    print('  url:', url)

    headers = {'Content-Type': 'application/octet-stream'}
    res = requests.post(url=url, data=data, headers=headers)

    return res

if __name__ == '__main__':
    data = open("input.pdf", "rb").read()

    print('\n--- INPUT ---\n')
    
    print('  len:', len(data))
    print('first:', data[:20])
    
    print('\n--- FILE ---\n')
    
    res = to_file(data)
    output = res.json()
    
    print(' json:', res.json())
    print('  len:', output['len'])
    print('first:', output['first'].encode('raw_unicode_escape'))

    print('\n--- BINARY ---\n')
    
    res = to_binary(data)
    output = res.json()
    
    print(' json:', res.json())
    print('  len:', output['len'])
    print('first:', output['first'].encode('raw_unicode_escape'))


