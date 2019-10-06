from ruuvitag_sensor.ruuvi import RuuviTagSensor as ruuvi
import json
import os
import paho.mqtt.client as mqtt

MQTT_CLIENT = os.getenv("CLIENT", "pi")
MQTT_SERVER = os.getenv("SERVER")
INTERVAL = int(os.getenv("SCAN_INTERVAL", 30))

def get_topic(mac):
    return "/ruuvi/{}".format(mac.replace(':', '').lower())

if __name__ == "__main__":
    if MQTT_SERVER is None:
        exit('ERROR: Please configure mandatory environment variable SERVER')

    client = mqtt.Client(MQTT_CLIENT)
    client.connect(MQTT_SERVER)

    while True:
        datas = ruuvi.get_data_for_sensors([], INTERVAL)
        for key, value in datas.items():
            print(get_topic(key) + ": " + json.dumps(value))
            client.publish(get_topic(key), json.dumps(value))