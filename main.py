# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'

import paho.mqtt.client as mqtt
import time
import config

mqtt_url = "mqtt.url.pl"
mqtt_port = 15998
mqtt_keepalive = 10
mqtt_client_name = 'client_0_' + config.cpuid + '_' + str(time.time_ns())
print(mqtt_url, mqtt_port, mqtt_keepalive, mqtt_client_name)
is_connected = False



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global is_connected
    is_connected = True
    # If connection is successful do the rest code
    if rc == 0:
        print("Connected with result code " + str(rc), userdata, flags)
        # Subscribing in on_connect() - if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("Client-0")
        client.publish('Client-0', 'Test message')
    else:
        print('fail')

    # client.subscribe("CoreElectronics/topic")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(client, userdata, msg.topic + " " + str(msg.payload))
    if msg.payload == "Hello":
        print("Received message #1")
        # Do something
    if msg.payload == "World!":
        print("Received message #2")
        # Do something else


def initialize_mqtt_connection():
    print('initializing connection')
    client = mqtt.Client(mqtt_client_name)
    client.on_connect = on_connect
    client.on_message = on_message
    print('starting connection')
    # Connecting
    while True:
        try:
            client.connect(mqtt_url, mqtt_port, mqtt_keepalive)
        # Catching errors
        except:
            print('connecting failed, reconnecting')
        else:
            break
    # Reconnecting part
    client.loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)
    print(client)


# Initialize and start connection
initialize_mqtt_connection()
