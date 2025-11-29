# Lab: Mosquitto + Paho

**Student ID:** 11926379

---

## 1. Installation

### Install Mosquitto Server
1. Download and install Mosquitto from [https://mosquitto.org/download/](https://mosquitto.org/download/).
2. Start the Mosquitto broker on your machine:
```bash
mosquitto
```

### Install Paho MQTT Client
1. Make sure Python is installed.
2. Install Paho MQTT library:
```bash
pip install paho-mqtt
```

---

## 2. Project Overview
This lab demonstrates using Mosquitto MQTT Server with multiple **publishers** (Temperature, Humidity, People Counter) and **subscribers** reading messages from specific topics.

---

## 3. Project Structure
```
mqtt-lab/
├─ publishers/
│  ├─ pub_temp.py
│  ├─ pub_humidity.py
│  └─ pub_people.py
├─ subscribers/
│  ├─ sub_temp.py
│  ├─ sub_humidity.py
│  └─ sub_people.py
├─ run_all.sh
└─ README.md

```

---

## 4. How to Run

### 1. Start Mosquitto Server
```bash
mosquitto
```

### 2. Run Publishers
```bash
python pub_temp.py
 python pub_humidity.py
 python pub_people.py
```

### 3. Run Subscribers
```bash
python sub_temp.py
python sub_humidity.py
python sub_people.py
```

---


## Conclusion
This lab successfully demonstrates the use of **Mosquitto MQTT Server** with multiple **publishers** and **subscribers** using the **Paho library** in Python.  
All publishers (Temperature, Humidity, People Counter) are sending data correctly, and subscribers are receiving messages as expected.  








