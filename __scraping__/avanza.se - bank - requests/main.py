import requests
from bs4 import BeautifulSoup

def display(content, filename='output.html'):
    with open(filename, 'w') as f:
        f.write(content)
    webbrowser.open(filename)

session = requests.Session()
session.headers.update({'USER-AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})

# main page
url = 'https://www.avanza.se/index/om-indexet.html/19002/omx-stockholm-30'
response = session.get(url)

# XHR

# curl 'https://www.avanza.se/ab/component/highstockchart/getchart/orderbook'
# -H 'Host: www.avanza.se'
# -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
# -H 'Accept: */*'
# -H 'Accept-Language: pl,en-US;q=0.7,en;q=0.3' --compressed
# -H 'Referer: https://www.avanza.se/index/om-indexet.html/19002/omx-stockholm-30'
# -H 'Content-Type: application/json'
# -H 'Cache-Control: no-cache'
# -H 'X-Requested-With: XMLHttpRequest'
# -H 'Cookie: AZACOOKIEMESSAGE=1; AZAABSESSION=e1sz4ei1jog1cyhmrwpbarcs'
# -H 'DNT: 1'
# -H 'Connection: keep-alive' 
# --data '{"orderbookId":19002,"chartType":"AREA","widthOfPlotContainer":640,"chartResolution":"MINUTE","navigator":true,"percentage":false,"volume":false,"owners":false,"timePeriod":"today","ta":[]}'

params = {
    'orderbookId': 19002,
    'chartType': 'AREA',
    'widthOfPlotContainer': 640,
    'chartResolution': 'MINUTE',
    'navigator': True,
    'percentage': False,
    'volume': False,
    'owners': False,
    'timePeriod': 'week',
    'ta': [],
}

headers = {
    ##'Host': 'www.avanza.se',
    #'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    #'Accept': '*/*',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
    #'Referer': 'https://www.avanza.se/index/om-indexet.html/19002/omx-stockholm-30',
    #'Content-Type': 'application/json',
    #'Cache-Control': 'no-cache',
    #'X-Requested-With': 'XMLHttpRequest',
    ##'Content-Length': '189',
    ##'Cookie': 'AZACOOKIEMESSAGE=1; AZAABSESSION=e1sz4ei1jog1cyhmrwpbarcs',
    #'DNT': '1',
    #'Connection': 'keep-alive',
}
        
url = 'https://www.avanza.se/ab/component/highstockchart/getchart/orderbook'        
response = session.post(url, json=params, headers=headers)

print(response.text)
print(response.request.headers)
print(response.request.body)
#print(response.cookies)

#print(response.json())
data = response.json()
print('keys:', data.keys())

#~ soup = BeautifulSoup(html)
#~ divs = soup.find_all('div', {'class': 'xxx'}) 

#~ for div in divs:
   #~ print(div.text)
