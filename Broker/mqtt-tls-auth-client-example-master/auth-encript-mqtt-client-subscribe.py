import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("/PCB/CELL-01/UR3E-01/REGOUT")

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

#---------------------------------------------------------------------------------------------------------------------------------------

keyPaths = "/home/raspberry/Workspace/mqtt-tls-auth-client-example-master/"

client = mqtt.Client(client_id="python-test-subscriber", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username="user01", password="user01")
client.tls_set(ca_certs=keyPaths+"ca.crt", certfile=keyPaths+"client01.crt",
                    keyfile=keyPaths+"client01.key", cert_reqs=ssl.CERT_NONE,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(True)
print("Connecting...")
client.connect("10.40.30.89", 31285, 30)

client.loop_forever()




