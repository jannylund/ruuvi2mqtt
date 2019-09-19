from ruuvitag_sensor.ruuvi import RuuviTagSensor as ruuvi
import paho.mqtt.client as mqtt
import json

def get_topic(mac):
    return "/ruuvi/{}".format(mac.replace(':', '').lower())

if __name__ == "__main__":
    client = mqtt.Client("pi")
    client.connect("10.0.1.141")

    while True:
        datas = ruuvi.get_data_for_sensors([], 30) # second param is interval to wait in seconds.
        for key, value in datas.items():
            print(get_topic(key) + ": " + json.dumps(value))
            client.publish(get_topic(key), json.dumps(value))