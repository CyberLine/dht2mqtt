# DHT 2 MQTT

```
git clone https://github.com/CyberLine/dht2mqtt.git
cd dht2mqtt
pip3 install -r requirements.txt
chmod +x *.py
# check the config block in the python file, then:
./dht_gpio.py
# or
./dht_serial.py
```

Use in cron and report values every minute:
`* * * * * /home/pi/dht_gpio.py 2>&1 >/dev/null`