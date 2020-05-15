#!/usr/bin/env python3

# date: 2020.04.28
# https://stackoverflow.com/questions/61481586/how-to-scrap-the-non-loaded-content-of-the-page/

import requests
from bs4 import BeautifulSoup

def get_page(session):
    url = "https://www.gpw.pl/spolki"
    
    response = session.get(url)
    soup = BeautifulSoup(response.content)
    
    all_links = soup.find_all("a")
    
    data = []

    for link in all_links:
        href = link.get("href")
        if "spolka?isin=" in href:
            data.append(href)
    
    print('\n'.join(data))


def get_ajax_data(session, offset, limit=10):
    url = 'https://www.gpw.pl/ajaxindex.php'

    data = {
        "offset": str(offset),
        "limit": str(limit),
        "format": "html",

        "action": "GPWCompanySearch",
        "start": "ajaxSearch",
        "page": "spolki",
        "lang": "PL",
        "letter": "",
        "order": "",
        "order_type": "",
        "searchText": "",
        "index[empty]": "on",
        "index[WIG20]":"on",
        "index[mWIG40]":"on",
        "index[sWIG80]":"on",
        "index[WIG30]":"on",
        "index[WIG]":"on",
        "index[WIGdiv]":"on",
        "index[WIG-CEE]":"on",
        "index[WIG-Poland]":"on",
        "index[InvestorMS]":"on",
        "index[TBSP.Index]":"on",
        "index[CEEplus]":"on",
        "index[mWIG40TR]":"on",
        "index[NCIndex]":"on",
        "index[sWIG80TR]":"on",
        "index[WIG-banki]":"on",
        "index[WIG-budownictwo]":"on",
        "index[WIG-chemia]":"on",
        "index[WIG-energia]":"on",
        "index[WIG-ESG]":"on",
        "index[WIG-górnictwo]":"on",
        "index[WIG-informatyka]":"on",
        "index[WIG-leki]":"on",
        "index[WIG-media]":"on",
        "index[WIG-motoryzacja]":"on",
        "index[WIG-nieruchomości]":"on",
        "index[WIG-odzież]":"on",
        "index[WIG-paliwa]":"on",
        "index[WIG-spożywczy]":"on",
        "index[WIG-telekomunikacja]":"on",
        "index[WIG-Ukraine]":"on",
        "index[WIG.GAMES]":"on",
        "index[WIG.MS-BAS]":"on",
        "index[WIG.MS-FIN]":"on",
        "index[WIG.MS-PET]":"on",
        "index[WIG20TR]":"on",
        "index[WIG30TR]":"on",
        "index[WIGtech]":"on",
        "sector[510]":"510","sector[110]":"110","sector[750]":"750","sector[410]":"410","sector[310]":"310","sector[360]":"360","sector[740]":"740","sector[180]":"180","sector[220]":"220","sector[650]":"650","sector[350]":"350","sector[320]":"320","sector[610]":"610","sector[690]":"690","sector[660]":"660","sector[330]":"330","sector[820]":"820","sector[399]":"399","sector[150]":"150","sector[640]":"640","sector[540]":"540","sector[140]":"140","sector[830]":"830","sector[520]":"520","sector[210]":"210","sector[170]":"170","sector[730]":"730","sector[420]":"420","sector[185]":"185","sector[370]":"370","sector[630]":"630","sector[130]":"130","sector[620]":"620","sector[720]":"720","sector[710]":"710","sector[810]":"810","sector[430]":"430","sector[120]":"120","sector[450]":"450","sector[160]":"160","sector[530]":"530","sector[440]":"440",
        "country[POLSKA]":"on","country[AUSTRALIA]":"on","country[AUSTRIA]":"on","country[Belgia]":"on","country[BUŁGARIA]":"on","country[CYPR]":"on","country[CZECHY]":"on","country[DANIA]":"on","country[ESTONIA]":"on","country[FRANCJA]":"on","country[GLOBAL]":"on","country[GUERNSEY]":"on","country[HISZPANIA]":"on","country[HOLANDIA]":"on","country[INNY]":"on","country[IRLANDIA]":"on","country[KANADA]":"on","country[LITWA]":"on","country[LUKSEMBURG]":"on","country[NIEMCY]":"on","country[Norwegia]":"on","country[REPUBLIKA+CZESKA]":"on","country[SŁOWACJA]":"on","country[Słowenia]":"on","country[STANY+ZJEDNOCZONE]":"on","country[SZWAJCARIA]":"on","country[SZWECJA]":"on","country[UKRAINA]":"on","country[WĘGRY]":"on","country[WIELKA+BRYTANIA]":"on","country[WŁOCHY]":"on","country[JERSEY]":"on",
        "voivodship[11]":"on","voivodship[16]":"on","voivodship[5]":"on","voivodship[13]":"on","voivodship[17]":"on","voivodship[7]":"on","voivodship[2]":"on","voivodship[10]":"on","voivodship[8]":"on","voivodship[4]":"on","voivodship[15]":"on","voivodship[9]":"on","voivodship[6]":"on","voivodship[3]":"on","voivodship[12]":"on","voivodship[14]":"on"
    }    

    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.content)
    
    all_links = soup.find_all("a")
    
    data = []

    for link in all_links:
        href = link.get("href")
        if "spolka?isin=" in href:
            data.append("https://www.gpw.pl/spolki/" + href)
    
    return data
    
# --- main ---

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.163 Chrome/80.0.3987.163 Safari/537.36'})
                  
#data = get_page(s)
#print('\n'.join(data))

limit = 10
for offset in range(0, 10*limit, limit):
    print('---', offset, '---')
    data = get_ajax_data(s, offset, limit)
    print('\n'.join(data))




