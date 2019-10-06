from dotenv import load_dotenv
from ruuvitag_sensor.ruuvi import RuuviTagSensor as ruuvi
import json
import os
import paho.mqtt.client as mqtt

# Load config.
load_dotenv("config.env")

MQTT_CLIENT = os.getenv("CLIENT", "pi")
MQTT_SERVER = os.getenv("SERVER")
INTERVAL = os.getenv("SCAN_INTERVAL", 30)

# Format topic.
def get_topic(mac):
    return "/ruuvi/{}".format(mac.replace(':', '').lower())

if __name__ == "__main__":
    if MQTT_SERVER is None:
        exit('ERROR: Please configure mandatory value SERVER in config.env')

    client = mqtt.Client(MQTT_CLIENT)
    client.connect(MQTT_SERVER)

    while True:
        datas = ruuvi.get_data_for_sensors([], INTERVAL)
        for key, value in datas.items():
            print(get_topic(key) + ": " + json.dumps(value))
            client.publish(get_topic(key), json.dumps(value))