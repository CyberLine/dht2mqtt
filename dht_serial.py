#!/usr/bin/env python3

import re
import sys
import serial
import paho.mqtt.client as mqtt

# begin config
broker_address = '192.168.2.82'
broker_port = 1883

serial_port = '/dev/ttyUSB0'
sensor_type = 22  # 11,22

label = 'wohnzimmer'
# end config

arduinoData = serial.Serial(serial_port, 9600)
base_topic = 'DHT{0}/{1}/'.format(sensor_type, label)


def mqtt_send():
    client = mqtt.Client(label)
    client.connect(broker_address, broker_port)
    client.publish(base_topic + 'temperature', temperature)
    client.publish(base_topic + 'humidity', humidity)
    client.disconnect()


while True:
    while (arduinoData.inWaiting() == 0):
        pass

    arduinoString = arduinoData.readline()
    humidity, temperature = re.findall(r'\d+\.\d+', arduinoString)

    if humidity is not None and temperature is not None:
        mqtt_send()
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

    sys.exit()
