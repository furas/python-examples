
# https://stackoverflow.com/questions/62479786/python-paho-mqtt-can-not-connect-to-mqtts-with-username-and-password/

# mosquitto_sub -h learn.evermight.net -p 9101 -t "test" -u "stackoverflow" -P "stackoverflow" --capath /etc/ssl/certs/
# mosquitto_pub -h learn.evermight.net -p 9101 -t "test" -u "stackoverflow" -P "stackoverflow" -m "hello world" --capath /etc/ssl/certs/

# if `mosquitto_pub`/`mosquitto_sub` needs `--capath /etc/ssl/certs/
# then code needs `client.tls_set()`

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.tls_set()  # <-- without arguments it uses default system settings

#client.tls_set_context(???)
#client.tls_insecure_set(True)

client.username_pw_set(username="stackoverflow", password="stackoverflow")

print("Connecting...")

client.connect("learn.evermight.net", 9101, 10)

client.loop_forever()
