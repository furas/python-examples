import requests

def get_proxy():
    
    url = 'http://gimmeproxy.com/api/getProxy?protocol=http&anonymityLevel=1'
    
    try:
        response = requests.get(url)
        data = response.json()

        for key, val in data.items():
            print(key, ':', val)

        return data['curl']

    except Exception as ex:
        print(ex)
    

def test_proxy(proxy):

    if not proxy:
        print('proxy:', proxy)
    else:
        try:
            proxies = proxies={'http': proxy}
            #print('proxies:', proxies)
            response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
            print(response.text)
        except Exception as ex:
            print(ex)

url = get_proxy()
#url = 'http://39.134.161.15:8080'
test_proxy(url)
