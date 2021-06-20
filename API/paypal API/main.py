
# https://developer.paypal.com/docs/platforms/get-started/
# https://developer.paypal.com/docs/integration/direct/transaction-search/

import requests

# --- constants ---

#CLIENT_ID = "ARg..."  # 80 chars
#SECRET    = "EAl..."  # 80 chars

#ENDPOINT = "https://api-m.sandbox.paypal.com"  # Sandbox - doesn't have access to transactions
ENDPOINT = "https://api-m.paypal.com"          # Live
    
DEBUG = True

# --- functions ---

def display_response(response):
    print('response:', response)
    print('url:', response.url)
    print('text:', response.text)    

def display_data(data):
    for key, value in data.items():
        if key == 'scope':
            for item in value.split(' '):
                print(key, '=', item)
        else:
            print(key, '=', value)
    
def get_token():
    if DEBUG:
        print('--- get token ---')
    
    url = ENDPOINT + '/v1/oauth2/token'
    
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US",
    }
        
    payload = {
        "grant_type": "client_credentials"
    }
        
    response = requests.post(url, auth=(CLIENT_ID, SECRET), data=payload)

    if DEBUG:
        display_response(response)    
    
    data = response.json()
    
    if DEBUG:
        display_data(data)
    
    return data['access_token']

def get_transactions():
    if DEBUG:
        print('--- transaction ---')
    
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": "en_US",
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    
    url = ENDPOINT + "/v1/reporting/transactions"
    
    payload = {
        'start_date': '2021-01-01T00:00:00-0700',
        'end_date':   '2021-02-01T00:00:00-0700',
    }    
    
    response = requests.get(url, headers=headers, params=payload)

    if DEBUG:
        display_response(response)    
    
    data = response.json()

    if DEBUG:
        display_data(data)
        
# --- main ---

TOKEN = get_token()

print('--- token ---')
print('TOKEN:', TOKEN)

get_transactions()

