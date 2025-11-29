# pub_humidity.py
import time
import json
import random
from paho.mqtt import client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/sensor/humidity"
STUDENT_ID = "11926379"

client = mqtt.Client("pub_humidity")
client.connect(BROKER, PORT)

try:
    for i in range(10):
        payload = {
            "student_id": STUDENT_ID,
            "sensor": "humidity",
            "value": random.randint(30, 70),
            "seq": i+1,
            "timestamp": time.time()
        }
        msg = json.dumps(payload)
        client.publish(TOPIC, msg)
        print("Published to", TOPIC, msg)
        time.sleep(1)
finally:
    client.disconnect()
