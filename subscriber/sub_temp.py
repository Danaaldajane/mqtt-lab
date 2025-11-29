# sub_temp.py
from paho.mqtt import client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/sensor/temperature"

def on_connect(client, userdata, flags, rc):
    print("Connected (temp subscriber) code:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Temperature Received:", data)

client = mqtt.Client("sub_temp")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT)
client.loop_forever()
