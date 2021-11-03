import requests

#import os
#api_key = os.getenv("API_KEY")

api_key = "ef....."

#city_name = input("Enter city name : ")
city_name = 'Warsaw'

url = "https://api.weatherbit.io/v2.0/current" # url without `?`

payload = {
    'key': api_key,
    'city': city_name,
    #'lang': 'pl'
}   

response = requests.get(url, params=payload)

data = response.json()

if 'error' in data:
    print('Error:', data['error'])
else:
    #print(data)
    
    data = data['data'][0]
    
    temperature = data["temp"]
    pressure    = data["pres"]
    humidity    = data["rh"]
    description = data["weather"]["description"]
    
    print(f"Temperature (in kelvin unit) = {temperature}")
    print(f"atmospheric pressure (in hPa unit) = {pressure}")
    print(f"humidity (in percentage) = {humidity}")
    print(f"description = {description}")

