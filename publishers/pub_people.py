# pub_people.py
import time
import json
import random
from paho.mqtt import client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/sensor/people"
STUDENT_ID = "11926379"

client = mqtt.Client("pub_people")
client.connect(BROKER, PORT)

try:
    for i in range(10):
        payload = {
            "student_id": STUDENT_ID,
            "sensor": "people_counter",
            "value": random.randint(0, 5),
            "seq": i+1,
            "timestamp": time.time()
        }
        msg = json.dumps(payload)
        client.publish(TOPIC, msg)
        print("Published to", TOPIC, msg)
        time.sleep(2)
finally:
    client.disconnect()
