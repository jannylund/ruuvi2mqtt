import asyncio
import json
import os
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

import paho.mqtt.client as mqtt
from ruuvitag_sensor.ruuvi import RuuviTagSensor

MQTT_CLIENT = os.getenv("CLIENT", "pi")
MQTT_SERVER = os.getenv("SERVER")
INTERVAL = int(os.getenv("SCAN_INTERVAL", 30))


def get_topic(mac):
    return "/ruuvi/{}".format(mac.replace(':', '').lower())


async def handle_queue(queue):
    client = mqtt.Client(MQTT_CLIENT)
    client.connect(MQTT_SERVER)

    while True:
        if not queue.empty():
            # We only care for the last data for each sensor.
            data = {}
            while not queue.empty():
                (mac, value) = queue.get()
                data[mac] = value

            for key, value in data.items():
                print(key + ":" + json.dumps(value))
                client.publish(key, json.dumps(value))

        time.sleep(INTERVAL)


def run_get_datas_background(queue):
    def handle_data(data):
        mac = get_topic(data[0])
        value = data[1]
        queue.put((mac, value))

    RuuviTagSensor.get_datas(handle_data)



if __name__ == "__main__":
    if MQTT_SERVER is None:
        exit('ERROR: Please configure mandatory environment variable SERVER')

    m = Manager()
    q = m.Queue()

    executor = ProcessPoolExecutor()
    executor.submit(run_get_datas_background, q)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(handle_queue(q))
