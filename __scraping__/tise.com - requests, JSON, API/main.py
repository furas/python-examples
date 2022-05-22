# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.16

import requests

headers = {
    'authority': 'tise.com',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9,no;q=0.8,en;q=0.7',
    'referer': 'https://tise.com/elisdak/following',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tise-app-platform': 'web',
    'tise-app-version': '0.0.16',
    'tise-system-os': 'web',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}

params = {
    'beforeTimestamp': '1652651040854',
}

response = requests.get('https://tise.com/api/user/5e9125bdfd11b10031be2b76/following', params=params, headers=headers)

data = response.json()

data['next']
