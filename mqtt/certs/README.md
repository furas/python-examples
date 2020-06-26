
https://stackoverflow.com/questions/62479786/python-paho-mqtt-can-not-connect-to-mqtts-with-username-and-password/

## Command Line Success

```bash
mosquitto_sub -h learn.evermight.net -p 9101 -t "test" -u "stackoverflow" -P "stackoverflow" --capath /etc/ssl/certs/
```

```bash
mosquitto_pub -h learn.evermight.net -p 9101 -t "test" -u "stackoverflow" -P "stackoverflow" -m "hello world" --capath /etc/ssl/certs/
```

## NodeJS Success

```javascript
const mqtt = require('async-mqtt');

  try{
    const client = await mqtt.connectAsync("mqtts://learn.evermight.net",{
      port:9101,
      host:"mqtts://learn.evermight.net",
      username:"stackoverflow",
      password:"stackoverflow",
      connectTimeout:5000,
      protocolId:"MQIsdp",
      protocolVersion:3,
      encoding:"utf8",
      keepalive: 60
    });
    await client.publish("test","hello world");
    await client.end();
  } catch(e) {
    console.log(e);
  }
```

## Website JavaScript

(note: websockets use port 9102)

```javascript
import Paho from "paho-mqtt";

const client = new Paho.Client("learn.evermight.net",9102,"WebBrowser");
  client.onConnectionLost = response=>console.log("lostMQTTConnection: " +(response.errorCode !== 0 ? response.errorMessage : "Unknown MQTT Error" ));
  client.onMessageArrived = message=>console.log(message.payloadString);
  client.connect({
    onSuccess:_=>client.subscribe("test"),
    useSSL:true,
    userName:"stackoverflow",
    password:"stackoverflow",
  });
```

## Python

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)


client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.tls_set()  # without arguments uses default system settings

client.username_pw_set(username="stackoverflow", password="stackoverflow")
print("Connecting...")
client.connect("learn.evermight.net", 9101, 10)
client.loop_forever()
```

---

I found that I can connect if I add this command without arguments

```
client.tls_set()
```

---

In paho documentation at the end of description for `tls_set()` you can see

```
Must be called before connect*().
```

but it works for me event after client.connect()

---

In the same domentation you can see that without arguments it uses defult system settings

```
By default, on Python 2.7.9+ or 3.4+,
the default certification authority of the system is used. 

On older Python version this parameter is mandatory.
```

---

It is needed only if `mosquitto_sub`/`mosquitto_pub` needs `--capath /etc/ssl/certs/`.
If `mosquitto_sub`/`mosquitto_pub` works without `--capath /etc/ssl/certs/` then don't use it.


