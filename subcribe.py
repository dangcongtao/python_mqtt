import random
from paho.mqtt import client as mqtt_client


# just example value
broker = 'mqtt.taodc.company.com.vn' 
port = 20
topic = "python/mqtt"


client_id = f'taodctest-{random.randint(0, 1000)}' # just example value

# username & pass reqire to connect mqtt server, just example value
username = 'usr_name'
password = 'passwd123'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username=username, password=password)
    
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subcribe(client):
    def on_message(client, userdata, msg):
        print(msg.payload.decode('utf-8'))


    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subcribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
