#!/usr/bin/env python3 

# date: 2019.11.30

import paho.mqtt.client as mqtt

def on_subscribe(client, userdata, mid, granted_qos):
    print("on_subscribe:", client, userdata, mid, granted_qos)

def on_message(client, userdata, message):
    #print('on_message:', client, userdata, message)
    #print(dir(message))
    print('on_message:', message.payload.decode())
   
host = "mqtt.eclipse.org"

client = mqtt.Client()
client.connect(host, port=1883, keepalive=60, bind_address="")

client.on_subscribe = on_subscribe
client.on_message = on_message

client.subscribe('temp', 1)

client.loop_forever()
