# pub_temp.py
import time
import json
import random
from paho.mqtt import client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/sensor/temperature"
STUDENT_ID = "11926379"

client = mqtt.Client("pub_temp")
client.connect(BROKER, PORT)

try:
    for i in range(10):
        payload = {
            "student_id": STUDENT_ID,
            "sensor": "temperature",
            "value": round(20 + random.random()*10, 2),
            "seq": i+1,
            "timestamp": time.time()
        }
        msg = json.dumps(payload)
        client.publish(TOPIC, msg)
        print("Published to", TOPIC, msg)
        time.sleep(1)
finally:
    client.disconnect()
