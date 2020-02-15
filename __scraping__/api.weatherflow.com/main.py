#!/usr/bin/env python3

# date: 2020.02.10
# 

import requests

url = 'https://api.weatherflow.com/wxengine/rest/model/getModelDataBySpot?model_id=-1&spot_id=110&units_wind=mph&units_temp=F&format=json&wf_apikey=84e778ae-fe8e-4b8f-8d33-6bc88967a2b1&wf_token=f147702351af100d7c220b633d085318&v=1.1'
r = requests.get(url)
data = r.json()
for row in data['model_data'][:10]:
    print(row['model_time_local'], '|', row['wind_speed'], '|', row['temp'], )


