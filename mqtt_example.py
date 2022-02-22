rom pydoc import cli
import time
import paho.mqtt.client as paho
from paho import mqtt
from pynput.keyboard import Key, Controller

keyboard = Controller()


def on_connect(client, userdata, flags, rc, properties=None):
    print("Bağlantı: %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("Mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Abone olundu: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("USERNAME", "PASSWORD")
client.connect("SERVER URL", 8883)

client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

client.subscribe("TOPIC", qos=0)

client.publish("TOPIC", payload="hot", qos=1)

client.loop_forever()


keyboard.type('Hello World')


# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
# keyboard.press('a')
# keyboard.release('a')