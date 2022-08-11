import paho.mqtt.client as mqtt
import ssl
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("/PCB/CELL-01/UR3E-01/REGOUT")

def on_message(client, userdata, msg):
    print("Recibi: ",msg.topic, msg.payload)

#---------------------------------------------------------------------------------------------------------------------------------------
keyPaths = "/home/antonio/LANITED/mqtt-tls-auth-client-example-master/"

client = mqtt.Client(client_id="Upython-test-subscriber-pubisher", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username="user01", password="user01")
client.tls_set(ca_certs=keyPaths+"ca.crt", certfile=keyPaths+"client01.crt",
                    keyfile=keyPaths+"client01.key", cert_reqs=ssl.CERT_NONE,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(True)
print("Connecting...")
client.connect("10.40.30.50", 31285, 30)

client.loop_start()

#--------------------------------------------------------------------------------
index = 0
while(True):
    print("\n")
    print("Envio -> /PCB/CELL-01/UR3E-01/REGOUT: " + str(index) + "|"+str(0)+"|"+str(0)+"|"+str(0))
    client.publish("/PCB/CELL-01/UR3E-01/REGOUT", str(index))
    index+=1
    time.sleep(1)


