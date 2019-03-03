#!/usr/bin/env python3

import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt

# begin config
broker_address: str = '192.168.2.82'
broker_port: int = 1883

sensor_type: str = Adafruit_DHT.DHT22  # Adafruit_DHT.DHT11
gpio_pin: int = 17

label: str = 'flur'
# end config

humidity, temperature = Adafruit_DHT.read_retry(sensor_type, gpio_pin)
base_topic = 'DHT{0}/{1}/'.format(sensor_type, label)


def mqtt_send(temp, humy):
    client = mqtt.Client(label)
    client.connect(broker_address, broker_port)
    client.publish(base_topic + 'temperature', '{0:0.1f}'.format(temp))
    client.publish(base_topic + 'humidity', '{0:0.1f}'.format(humy))
    client.disconnect()


if humidity is not None and temperature is not None:
    mqtt_send(temperature, humidity)
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
