# sub_people.py
from paho.mqtt import client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/sensor/people"

def on_connect(client, userdata, flags, rc):
    print("Connected (people subscriber) code:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("People Counter Received:", data)

client = mqtt.Client("sub_people")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT)
client.loop_forever()
