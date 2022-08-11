from pickle import TRUE
import time
import snap7
import ssl
import paho.mqtt.client as mqtt 
from snap7 import util
from snap7.types import*

data_read= ['0','0',0,0,0,0,0,0,0,0,0,0,0,0,0]

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code", rc)
    for i in range(0,14):
        client.subscribe(topics3[i])
    # client.subscribe(topics3[2])
    # client.subscribe(topics3[4])
    # client.subscribe(topics3[6])
    # client.subscribe(topics3[8])

def on_message(client, userdata, msg):
    try:
        if (msg.topic == topics3[0]):
            data_read[0]=str(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[2]):
            data_read[2]=int(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[4]):
            data_read[4]=int(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[6]):
            data_read[6]=int(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[8]):
            data_read[8]=bool(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[9]):
            data_read[9]=int(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[11]):
            data_read[11]=bool(msg.payload.decode("utf-8"))
        if (msg.topic == topics3[13]):
            data_read[13]=int(msg.payload.decode("utf-8"))
    except:
        pass
    # if (msg.topic == topics18[1]):
    #     data_read[1]=str(msg.payload.decode("utf-8"))
    # if (msg.topic == topics18[2]):
    #     data_read[2]=int(msg.payload.decode("utf-8"))
    # if (msg.topic == topics18[3]):
    #     data_read[3]=str(msg.payload.decode("utf-8"))
    # if (msg.topic == topics_ur[0]):
    #    data_read[4]=int(msg.payload.decode("utf-8"))
    #print("Recibi: ",msg.topic, msg.payload)
    #print(data_read)

IP = '10.40.30.10'
RACK = 0
SLOT = 0

DB_TEST = 2
START_ADDRESST = 276
SIZET = 2

DB_NUM_2 = 2
START_ADDRESS2 = 0
SIZE2 = 286

DB_NUM_3 = 3
START_ADDRESS3 = 0
SIZE3 = 316

DB_NUM_4 = 4
START_ADDRESS4 = 0
SIZE4 = 32

DB_NUM_5 = 5
START_ADDRESS5 = 0
SIZE5 = 306

DB_NUM_6 = 6
START_ADDRESS6 = 0
SIZE6 = 50

DB_NUM_7 = 7
START_ADDRESS7 = 0
SIZE7 = 265

DB_NUM_8 = 8
START_ADDRESS8 = 0
SIZE8 = 304

DB_NUM_9 = 9
START_ADDRESS9 = 0
SIZE9 = 286

DB_NUM_10 = 10
START_ADDRESS10 = 0
SIZE10 = 276

DB_NUM_11 = 11
START_ADDRESS11 = 0
SIZE11 = 30

DB_NUM_12 = 12
START_ADDRESS12 = 0
SIZE12 = 348

DB_NUM_13 = 13
START_ADDRESS13 = 0
SIZE13 = 50

DB_NUM_14 = 14
START_ADDRESS14 = 0
SIZE14 = 286

DB_NUM_15 = 15
START_ADDRESS15 = 0
SIZE15 = 276

DB_NUM_16 = 16
START_ADDRESS16 = 0
SIZE16 = 30

DB_NUM_17 = 17
START_ADDRESS17 = 0
SIZE17 = 10

DB_NUM_18 = 18
START_ADDRESS18 = 0
SIZE18 = 20

DB_NUM_19 = 19
START_ADDRESS19 = 0
SIZE19 = 286

DB_NUM_20 = 20
START_ADDRESS20 = 0
SIZE20 = 266

DB_NUM_21 = 21
START_ADDRESS21 = 0
SIZE21 = 304

DB_NUM_22 = 22
START_ADDRESS22 = 0
SIZE22 = 276

DB_NUM_23 = 23
START_ADDRESS23 = 0
SIZE23 = 286

DB_NUM_30 = 30
START_ADDRESS30 = 0
SIZE30 = 286

topics2   = []
topics3   = []
topics4   = []
topics5   = []
topics6   = []
topics7   = []
topics8   = []
topics9   = []
topics10  = []
topics11  = []
topics12  = []
topics13  = []
topics14  = []
topics15  = []
topics16  = []
topics17  = []
topics18  = []
topics19  = []
topics20  = []
topics21  = []
topics22  = []
topics23  = []
topics24  = []
topics25  = []
topics26  = []
topics27  = []
topics28  = []
topics29  = []
topics30  = []
topics_ur = []

plc_db2   = []
plc_db3   = []
plc_db4   = []
plc_db5   = []
plc_db6   = []
plc_db7   = []
plc_db8   = []
plc_db9   = []
plc_db10  = []
plc_db11  = []
plc_db12  = []
plc_db13  = []
plc_db14  = []
plc_db15  = []
plc_db16  = []
plc_db17  = []
plc_db18  = []
plc_db19  = []
plc_db20  = []
plc_db21  = []
plc_db22  = []
plc_db23  = []
plc_db24  = []
plc_db25  = []
plc_db26  = []
plc_db27  = []
plc_db28  = []
plc_db29  = []
plc_db30  = []

#-GENERANDO ARREGLOS DE TOPICOS
topics_ur.append('/PCB/CELL-A/UR3-A/CONTROLLER/JOBNUMBER/VALUE')

topics2.append('/PCB/CELL-A/RACK-A/MONITORING/STATUS/TYPE')
topics2.append('/PCB/CELL-A/RACK-A/MONITORING/STATUS/TIMESTAMP')
topics2.append('/PCB/CELL-A/RACK-A/MONITORING/STATUS/VALUE')
topics2.append('/PCB/CELL-A/RACK-A/MONITORING/COUNT/VALUE')
topics2.append('/PCB/CELL-A/RACK-A/MONITORING/COUNT/TIMESTAMP')
topics2.append('/PCB/CELL-A/RACK-A/MONITORING/DETECT/VALUE')
topics2.append('/PCB/CELL-A/RACK-A/MONITORING/DETECT/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/TRACKCODE/VALUE')             #0
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/TRACKCODE/TIMESTAMP')         #1
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/COMMAND/VALUE')               #2
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/COMMAND/TIMESTAMP')           #3
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/JOBNUMBER/VALUE')             #4
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/JOBNUMBER/TIMESTAMP')         #5
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/VISOR/VALUE')                 #6 LEER
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/VISOR/TIMESTAMP')             #7
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/PUBLISH/VALUE')               #8
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/TOOL/VALUE')                  #9
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/TOOL/TIMESTAMP')              #10
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/EXECUTE/VALUE')               #11
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/EXECUTE/TIMESTAMP')           #12
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/VISORRESULT/VALUE')           #13
topics3.append('/PCB/CELL-A/UR3-A/CONTROLLER/VISORRESULT/TIMESTAMP')       #14 
#-------------------------------------------------------------------------------------------------------------------------------------
topics4.append('/PCB/CELL-A/LPKF-A/MONITORING/GATE/VALUE')
topics4.append('/PCB/CELL-A/LPKF-A/MONITORING/GATE/TIMESTAMP')
topics4.append('/PCB/CELL-A/LPKF-A/MONITORING/CLAMP/VALUE')
topics4.append('/PCB/CELL-A/LPKF-A/MONITORING/CLAMP/TIMESTAMP')
topics4.append('/PCB/CELL-A/LPKF-A/MONITORING/CYCLETIME/VALUE')
topics4.append('/PCB/CELL-A/LPKF-A/MONITORING/CYCLETIME/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/STATUS/TYPE')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/STATUS/TIMESTAMP')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/STATUS/VALUE')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/DETECT/VALUE')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/DETECT/TIMESTAMP')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/GRIPPER/VALUE')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/GRIPPER/TIMESTAMP')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/POSITION/VALUE')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/POSITION/TIMESTAMP')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/CLEANER/VALUE')
topics5.append('/PCB/CELL-A/CLEAN-A/MONITORING/CLEANER/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/COMMAND/VALUE')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/COMMAND/TIMESTAMP')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/EXECUTE/VALUE')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/EXECUTE/TIMESTAMP')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/STATUS/VALUE')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/STATUS/TIMESTAMP')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/RESULTWORK/VALUE')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/RESULTWORK/TIMESTAMP')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/EMERGENCYSTOP/VALUE')
topics6.append('/PCB/CELL-A/CLEAN-A/CONTROLLER/EMERGENCYSTOP/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics7.append('/PCB/CELL-A/INSPECTION-A/MONITORING/STATUS/TYPE')
topics7.append('/PCB/CELL-A/INSPECTION-A/MONITORING/STATUS/TIMESTAMP')
topics7.append('/PCB/CELL-A/INSPECTION-A/MONITORING/STATUS/VALUE')
#-------------------------------------------------------------------------------------------------------------------------------------
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/COMMAND/VALUE')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/COMMAND/TIMESTAMP')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/EXECUTE/VALUE')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/EXECUTE/TIMESTAMP')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/STATUS/VALUE')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/STATUS/TIMESTAMP')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/RESULTWORK/VALUE')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/RESULTWORK/TIMESTAMP')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/TRACKCODE/VALUE')
topics8.append('/PCB/CELL-A/INSPECTION-A/CONTROLLER/TRACKCODE/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/STATUS/TYPE')
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/STATUS/TIMESTAMP')
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/STATUS/VALUE')
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/COUNT/VALUE')
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/COUNT/TIMESTAMP')
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/SLOTCOUNTER/VALUE')
topics9.append('/PCB/CELL-A/NOOK-A/MONITORING/SLOTCOUNTER/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics10.append('/PCB/CELL-A/RACK-B/MONITORING/STATUS/TYPE')
topics10.append('/PCB/CELL-A/RACK-B/MONITORING/STATUS/TIMESTAMP')
topics10.append('/PCB/CELL-A/RACK-B/MONITORING/STATUS/VALUE')
topics10.append('/PCB/CELL-A/RACK-B/MONITORING/DETECT/VALUE')
topics10.append('/PCB/CELL-A/RACK-B/MONITORING/DETECT/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics11.append('/PCB/CELL-A/UR5-B/MONITORING/HOMEACT/VALUE')
topics11.append('/PCB/CELL-A/UR5-B/MONITORING/HOMEACT/TIMESTAMP')
topics11.append('/PCB/CELL-A/UR5-B/MONITORING/OVERRUNINIT/VALUE')
topics11.append('/PCB/CELL-A/UR5-B/MONITORING/OVERRUNINIT/TIMESTAMP')
topics11.append('/PCB/CELL-A/UR5-B/MONITORING/OVERRUNEND/VALUE')
topics11.append('/PCB/CELL-A/UR5-B/MONITORING/OVERRUNEND/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/STATUS/TYPE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/STATUS/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/STATUS/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/DETECTSIDE1/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/DETECTSIDE1/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/DETECTSIDE2/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/DETECTSIDE2/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/TRANSFER/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/TRANSFER/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/APPROACH/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/APPROACH/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/RIGHTAPPLICATOR/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/RIGHTAPPLICATOR/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/LEFTAPPLICATOR/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/LEFTAPPLICATOR/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/COUNTER/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/COUNTER/TIMESTAMP')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/CYCLETIME/VALUE')
topics12.append('/PCB/CELL-A/STENCIL-B/MONITORING/CYCLETIME/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/COMMAND/VALUE')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/COMMAND/TIMESTAMP')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/EXECUTE/VALUE')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/EXECUTE/TIMESTAMP')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/STATUS/VALUE')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/STATUS/TIMESTAMP')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/RESULTWORK/VALUE')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/RESULTWORK/TIMESTAMP')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/EMERGENCYSTOP/VALUE')
topics13.append('/PCB/CELL-A/STENCIL-B/CONTROLLER/EMERGENCYSTOP/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/STATUS/TYPE')
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/STATUS/TIMESTAMP')
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/STATUS/VALUE')
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/COUNT/VALUE')
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/COUNT/TIMESTAMP')
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/SLOTCOUNTER/VALUE')
topics14.append('/PCB/CELL-A/NOOK-B/MONITORING/SLOTCOUNTER/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics15.append('/PCB/CELL-A/BREAKRACK-B/MONITORING/STATUS/TYPE')
topics15.append('/PCB/CELL-A/BREAKRACK-B/MONITORING/STATUS/TIMESTAMP')
topics15.append('/PCB/CELL-A/BREAKRACK-B/MONITORING/STATUS/VALUE')
topics15.append('/PCB/CELL-A/BREAKRACK-B/MONITORING/DETECT/VALUE')
topics15.append('/PCB/CELL-A/BREAKRACK-B/MONITORING/DETECT/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics16.append('/PCB/CELL-A/PICKANDPLACE-B/MONITORING/DETECT1/VALUE')
topics16.append('/PCB/CELL-A/PICKANDPLACE-B/MONITORING/DETECT1/TIMESTAMP')
topics16.append('/PCB/CELL-A/PICKANDPLACE-B/MONITORING/DETECT2/VALUE')
topics16.append('/PCB/CELL-A/PICKANDPLACE-B/MONITORING/DETECT2/TIMESTAMP')
topics16.append('/PCB/CELL-A/PICKANDPLACE-B/MONITORING/CLAMP/VALUE')
topics16.append('/PCB/CELL-A/PICKANDPLACE-B/MONITORING/CLAMP/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics17.append('/PCB/CELL-A/OVEN-C/MONITORING/GATE/VALUE')
topics17.append('/PCB/CELL-A/OVEN-C/MONITORING/GATE/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics18.append('/PCB/CELL-A/OVEN-C/CONTROLLER/COMMAND/VALUE')
topics18.append('/PCB/CELL-A/OVEN-C/CONTROLLER/COMMAND/TIMESTAMP')
topics18.append('/PCB/CELL-A/OVEN-C/CONTROLLER/EXECUTE/VALUE')
topics18.append('/PCB/CELL-A/OVEN-C/CONTROLLER/EXECUTE/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/STATUS/TYPE')
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/STATUS/TIMESTAMP')
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/STATUS/VALUE')
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/COUNT/VALUE')
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/COUNT/TIMESTAMP')
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/SLOTCOUNTER/VALUE')
topics19.append('/PCB/CELL-A/NOOK-C/MONITORING/SLOTCOUNTER/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics20.append('/PCB/CELL-A/INSPECTION-C/MONITORING/STATUS/TYPE')
topics20.append('/PCB/CELL-A/INSPECTION-C/MONITORING/STATUS/TIMESTAMP')
topics20.append('/PCB/CELL-A/INSPECTION-C/MONITORING/STATUS/VALUE')
#-------------------------------------------------------------------------------------------------------------------------------------
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/COMMAND/VALUE')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/COMMAND/TIMESTAMP')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/EXECUTE/VALUE')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/EXECUTE/TIMESTAMP')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/STATUS/VALUE')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/STATUS/TIMESTAMP')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/RESULTWORK/VALUE')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/RESULTWORK/TIMESTAMP')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/TRACKCODE/VALUE')
topics21.append('/PCB/CELL-A/INSPECTION-C/CONTROLLER/TRACKCODE/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics22.append('/PCB/CELL-A/ROTATIONRACK-C/MONITORING/STATUS/TYPE')
topics22.append('/PCB/CELL-A/ROTATIONRACK-C/MONITORING/STATUS/TIMESTAMP')
topics22.append('/PCB/CELL-A/ROTATIONRACK-C/MONITORING/STATUS/VALUE')
topics22.append('/PCB/CELL-A/ROTATIONRACK-C/MONITORING/DETECT/VALUE')
topics22.append('/PCB/CELL-A/ROTATIONRACK-C/MONITORING/DETECT/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/STATUS/TYPE')
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/STATUS/TIMESTAMP')
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/STATUS/VALUE')
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/COUNT/VALUE')
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/COUNT/TIMESTAMP')
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/SLOTCOUNTER/VALUE')
topics23.append('/PCB/CELL-A/FINISHEDRACK-C/MONITORING/SLOTCOUNTER/TIMESTAMP')
#-------------------------------------------------------------------------------------------------------------------------------------
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/TOOL/VALUE')
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/TOOL/TIMESTAMP')
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/VISOR/VALUE')
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/VISOR/TIMESTAMP')
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/STATUS/TYPE')
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/STATUS/TIMESTAMP')
topics30.append('/PCB/CELL-A/UR3-A/MONITORING/STATUS/VALUE')

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
keyPaths = "/home/antonio/LANITED/Broker/mqtt-tls-auth-client-example-master/"
client = mqtt.Client(client_id="Upython-test-subscriber-pubisher", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username="user01", password="user01")
client.tls_set(ca_certs=keyPaths+"ca.crt", certfile=keyPaths+"client01.crt",
                    keyfile=keyPaths+"client01.key", cert_reqs=ssl.CERT_NONE,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(True)

try:
    client.connect("10.40.30.50", 31285, 30)
    print("Broker Connected")
    client.loop_start()
except:
    print("Broker Failed")
    


# #---------------------------------------------------------------------------------------------------------------------------------------
# PLC CONNECTION
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)
c=plc.get_connected()
print(c)
state = plc.get_cpu_state()
print(f'State:{state}')


#print(dbrt)

j=0
while True:
    start  = time.time()    
    dbr2    = plc.db_read(DB_NUM_2,   START_ADDRESS2,   SIZE2)
    dbr3    = plc.db_read(DB_NUM_3,   START_ADDRESS3,   SIZE3)
    dbr4    = plc.db_read(DB_NUM_4,   START_ADDRESS4,   SIZE4)
    dbr5    = plc.db_read(DB_NUM_5,   START_ADDRESS5,   SIZE5)
    dbr6    = plc.db_read(DB_NUM_6,   START_ADDRESS6,   SIZE6)
    dbr7    = plc.db_read(DB_NUM_7,   START_ADDRESS7,   SIZE7)
    dbr8    = plc.db_read(DB_NUM_8,   START_ADDRESS8,   SIZE8)
    dbr9    = plc.db_read(DB_NUM_9,   START_ADDRESS9,   SIZE9)
    dbr10   = plc.db_read(DB_NUM_10,  START_ADDRESS10,  SIZE10)
    dbr11   = plc.db_read(DB_NUM_11,  START_ADDRESS11,  SIZE11)
    dbr12   = plc.db_read(DB_NUM_12,  START_ADDRESS12,  SIZE12)
    dbr13   = plc.db_read(DB_NUM_13,  START_ADDRESS13,  SIZE13)
    dbr14   = plc.db_read(DB_NUM_14,  START_ADDRESS14,  SIZE14)
    dbr15   = plc.db_read(DB_NUM_15,  START_ADDRESS15,  SIZE15)
    dbr16   = plc.db_read(DB_NUM_16,  START_ADDRESS16,  SIZE16)
    dbr17   = plc.db_read(DB_NUM_17,  START_ADDRESS17,  SIZE17)
    dbr18   = plc.db_read(DB_NUM_18,  START_ADDRESS18,  SIZE18)
    dbr19   = plc.db_read(DB_NUM_19,  START_ADDRESS19,  SIZE19)
    dbr20   = plc.db_read(DB_NUM_20,  START_ADDRESS20,  SIZE20)
    dbr21   = plc.db_read(DB_NUM_21,  START_ADDRESS21,  SIZE21)
    dbr22   = plc.db_read(DB_NUM_22,  START_ADDRESS22,  SIZE22)
    dbr23   = plc.db_read(DB_NUM_23,  START_ADDRESS23,  SIZE23)
    # dbr24   = plc.db_read(DB_NUM_24,  START_ADDRESS24,  SIZE24)
    # dbr25   = plc.db_read(DB_NUM_25,  START_ADDRESS25,  SIZE25)
    # dbr26   = plc.db_read(DB_NUM_26,  START_ADDRESS26,  SIZE26)
    # dbr27   = plc.db_read(DB_NUM_27,  START_ADDRESS27,  SIZE27)
    # dbr28   = plc.db_read(DB_NUM_28,  START_ADDRESS28,  SIZE28)
    # dbr29   = plc.db_read(DB_NUM_29,  START_ADDRESS29,  SIZE29)
    dbr30   = plc.db_read(DB_NUM_30,  START_ADDRESS30,  SIZE30)
    #dbrt = plc.db_read(DB_TEST,  START_ADDRESST,  SIZET)

    #RACK-A.MONITORING DB2-------------------------------------------------------------------------------------------------------------------------
    plc_db2.append(util.get_int(dbr2,0))                     #INT           0  -- Status.Type
    plc_db2_dt1=str(util.get_date_time_object(dbr2,2))                   
    plc_db2.append(plc_db2_dt1)                              #DATE&TIME     1  -- Status.Timestamp
    plc_db2.append(util.get_string(dbr2, 10))                #STRING        2  -- Status.Value
    plc_db2.append(util.get_int(dbr2,266))                   #INT           3  -- Count.Value
    plc_db2_dt2=str(util.get_date_time_object(dbr2,268))
    plc_db2.append(plc_db2_dt2)                              #DATE&TIME     4  -- Count.Timestamp
    plc_db2.append(util.get_int(dbr2,276))                   #INT           5  -- Detect.Value
    plc_db2_dt3=str(util.get_date_time_object(dbr2,278))
    plc_db2.append(plc_db2_dt3)                              #DATE&TIME     6  -- Detect.Timestamp

    #LPKF-A.MONITORING DB4-------------------------------------------------------------------------------------------------------------------------
    plc_db4.append(util.get_int(dbr4,0))                     #INT           0  -- Gate.Value
    plc_db4_dt1=str(util.get_date_time_object(dbr4,2))                   
    plc_db4.append(plc_db4_dt1)                              #DATE&TIME     1  -- Gate.Timestamp
    plc_db4.append(util.get_int(dbr4,10))                    #INT           2  -- Clamp.Type
    plc_db4_dt2=str(util.get_date_time_object(dbr4,12))                   
    plc_db4.append(plc_db4_dt2)                              #DATE&TIME     3  -- Clamp.Timestamp
    plc_db4.append(util.get_dint(dbr4,20))                   #DINT          4  -- Cycletime.Type
    plc_db4_dt3=str(util.get_date_time_object(dbr4,24))                   
    plc_db4.append(plc_db4_dt3)                              #DATE&TIME     5  -- Cycletime.Timestamp
    
    #CLEAN-A.MONITORING DB5-------------------------------------------------------------------------------------------------------------------------
    plc_db5.append(util.get_int(dbr5,0))                     #INT           0  -- Status.Type
    plc_db5_dt1=str(util.get_date_time_object(dbr5,2))                   
    plc_db5.append(plc_db5_dt1)                              #DATE&TIME     1  -- Status.Timestamp
    plc_db5.append(util.get_string(dbr5, 10))                #STRING        2  -- Status.Value
    plc_db5.append(util.get_int(dbr5,266))                   #INT           3  -- Detect.Value
    plc_db5_dt2=str(util.get_date_time_object(dbr5,268))
    plc_db5.append(plc_db5_dt2)                              #DATE&TIME     4  -- Detect.Timestamp
    plc_db5.append(util.get_int(dbr5,276))                   #INT           5  -- Gripper.Value
    plc_db5_dt3=str(util.get_date_time_object(dbr5,278))
    plc_db5.append(plc_db5_dt3)                              #DATE&TIME     6  -- Gripper.Timestamp
    plc_db5.append(util.get_int(dbr5,286))                   #INT           5  -- Position.Value
    plc_db5_dt4=str(util.get_date_time_object(dbr5,288))
    plc_db5.append(plc_db5_dt4)                              #DATE&TIME     6  -- Position.Timestamp
    plc_db5.append(util.get_int(dbr5,296))                   #INT           5  -- Cleaner.Value
    plc_db5_dt5=str(util.get_date_time_object(dbr5,298))
    plc_db5.append(plc_db5_dt5)                              #DATE&TIME     6  -- Cleaner.Timestamp

    #INSPECTION-A.MONITORING DB7-------------------------------------------------------------------------------------------------------------------------
    plc_db7.append(util.get_int(dbr7,0))                     #INT           0  -- Status.Type
    plc_db7_dt1=str(util.get_date_time_object(dbr7,2))                   
    plc_db7.append(plc_db7_dt1)                              #DATE&TIME     1  -- Status.Timestamp
    plc_db7.append(util.get_string(dbr7, 10))                #STRING        2  -- Status.Value

    #NOOK-A.MONITORING DB9-------------------------------------------------------------------------------------------------------------------------
    plc_db9.append(util.get_int(dbr9,0))                     #INT           0  -- Status.Type
    plc_db9_dt1=str(util.get_date_time_object(dbr9,2))                   
    plc_db9.append(plc_db9_dt1)                              #DATE&TIME     1  -- Status.Timestamp
    plc_db9.append(util.get_string(dbr9, 10))                #STRING        2  -- Status.Value
    plc_db9.append(util.get_int(dbr9,266))                   #INT           3  -- Count.Value
    plc_db9_dt2=str(util.get_date_time_object(dbr9,268))
    plc_db9.append(plc_db9_dt2)                              #DATE&TIME     4  -- Count.Timestamp
    plc_db9.append(util.get_int(dbr9,276))                   #INT           5  -- Slotcounter.Value
    plc_db9_dt3=str(util.get_date_time_object(dbr9,278))
    plc_db9.append(plc_db9_dt3)                              #DATE&TIME     6  -- Slotcounter.Timestamp

    #RACK-B.MONITORING DB10-------------------------------------------------------------------------------------------------------------------------
    plc_db10.append(util.get_int(dbr10,0))                   #INT           0  -- Status.Type
    plc_db10_dt1=str(util.get_date_time_object(dbr10,2))                 
    plc_db10.append(plc_db10_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db10.append(util.get_string(dbr10, 10))              #STRING        2  -- Status.Value
    plc_db10.append(util.get_int(dbr10,266))                 #INT           3  -- Detect.Value
    plc_db10_dt2=str(util.get_date_time_object(dbr10,268))
    plc_db10.append(plc_db10_dt2)                            #DATE&TIME     4  -- Detect.Timestamp
    
    #UR5-B.MONITORING DB11-------------------------------------------------------------------------------------------------------------------------
    plc_db11.append(util.get_int(dbr11,0))                   #INT           0  -- HomeAct.Value
    plc_db11_dt1=str(util.get_date_time_object(dbr11,2))                   
    plc_db11.append(plc_db11_dt1)                            #DATE&TIME     1  -- HomeAct.Timestamp
    plc_db11.append(util.get_int(dbr11,10))                  #INT           2  -- Overruninit.Type
    plc_db11_dt2=str(util.get_date_time_object(dbr11,12))                   
    plc_db11.append(plc_db11_dt2)                            #DATE&TIME     3  -- Overruninit.Timestamp
    plc_db11.append(util.get_dint(dbr11,20))                 #DINT          4  -- Overrunend.Type
    plc_db11_dt3=str(util.get_date_time_object(dbr11,22))                   
    plc_db11.append(plc_db11_dt3)                            #DATE&TIME     5  -- Overrunend.Timestamp
    
    #STENCIL-B.MONITORING DB12----------------------------------------------------------------------------------------------------------------------
    plc_db12.append(util.get_int(dbr12,0))                   #INT           0  -- Status.Type
    plc_db12_dt1=str(util.get_date_time_object(dbr12,2))                 
    plc_db12.append(plc_db12_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db12.append(util.get_string(dbr12, 10))              #STRING        2  -- Status.Value
    plc_db12.append(util.get_int(dbr12,266))                 #INT           3  -- Detectside1.Value
    plc_db12_dt2=str(util.get_date_time_object(dbr12,268))
    plc_db12.append(plc_db12_dt2)                            #DATE&TIME     4  -- Detectside1.Timestamp
    plc_db12.append(util.get_int(dbr12,276))                 #INT           5  -- Detectside2.Value
    plc_db12_dt3=str(util.get_date_time_object(dbr12,278))
    plc_db12.append(plc_db12_dt3)                            #DATE&TIME     6  -- Detectside2.Timestamp
    plc_db12.append(util.get_int(dbr12,286))                 #INT           7  -- Transfer.Value
    plc_db12_dt4=str(util.get_date_time_object(dbr12,288))
    plc_db12.append(plc_db12_dt4)                            #DATE&TIME     8  -- Transfer.Timestamp
    plc_db12.append(util.get_int(dbr12,296))                 #INT           9  -- Approach.Value
    plc_db12_dt5=str(util.get_date_time_object(dbr12,298))
    plc_db12.append(plc_db12_dt5)                            #DATE&TIME     10  -- Approach.Timestamp
    plc_db12.append(util.get_int(dbr12,306))                 #INT           11  -- Rightapplicator.Value
    plc_db12_dt6=str(util.get_date_time_object(dbr12,308))
    plc_db12.append(plc_db12_dt6)                            #DATE&TIME     12  -- Rightapplicator.Timestamp
    plc_db12.append(util.get_int(dbr12,316))                 #INT           13  -- Leftapplicator.Value
    plc_db12_dt7=str(util.get_date_time_object(dbr12,318))
    plc_db12.append(plc_db12_dt7)                            #DATE&TIME     14  -- Leftapplicator.Timestamp
    plc_db12.append(util.get_int(dbr12,326))                 #INT           15  -- Counter.Value
    plc_db12_dt8=str(util.get_date_time_object(dbr12,328))
    plc_db12.append(plc_db12_dt8)                            #DATE&TIME     16  -- Counter.Timestamp
    plc_db12.append(util.get_int(dbr12,336))                 #INT           17  -- Cycletime.Value
    plc_db12_dt9=str(util.get_date_time_object(dbr12,340))
    plc_db12.append(plc_db12_dt9)                            #DATE&TIME     18  -- Cycletime.Timestamp

    #NOOK-B.MONITORING DB14-------------------------------------------------------------------------------------------------------------------------
    plc_db14.append(util.get_int(dbr14,0))                   #INT           0  -- Status.Type
    plc_db14_dt1=str(util.get_date_time_object(dbr14,2))                   
    plc_db14.append(plc_db14_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db14.append(util.get_string(dbr14, 10))              #STRING        2  -- Status.Value
    plc_db14.append(util.get_int(dbr14,266))                 #INT           3  -- Count.Value
    plc_db14_dt2=str(util.get_date_time_object(dbr14,268))
    plc_db14.append(plc_db14_dt2)                            #DATE&TIME     4  -- Count.Timestamp
    plc_db14.append(util.get_int(dbr14,276))                 #INT           5  -- Slotcounter.Value
    plc_db14_dt3=str(util.get_date_time_object(dbr14,278))
    plc_db14.append(plc_db14_dt3)                            #DATE&TIME     6  -- Slotcounter.Timestamp

    #BREAKRACK-B.MONITORING DB15--------------------------------------------------------------------------------------------------------------------
    plc_db15.append(util.get_int(dbr15,0))                   #INT           0  -- Status.Type
    plc_db15_dt1=str(util.get_date_time_object(dbr15,2))                 
    plc_db15.append(plc_db15_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db15.append(util.get_string(dbr15, 10))              #STRING        2  -- Status.Value
    plc_db15.append(util.get_int(dbr15,266))                 #INT           3  -- Detect.Value
    plc_db15_dt2=str(util.get_date_time_object(dbr15,268))
    plc_db15.append(plc_db15_dt2)                            #DATE&TIME     4  -- Detect.Timestamp

    #PICKANDPLACEB.MONITORING DB16------------------------------------------------------------------------------------------------------------------
    plc_db16.append(util.get_int(dbr16,0))                   #INT           0  -- Detect1.Value
    plc_db16_dt1=str(util.get_date_time_object(dbr16,2))
    plc_db16.append(plc_db16_dt1)                            #DATE&TIME     1  -- Detect1.Timestamp
    plc_db16.append(util.get_int(dbr16,10))                  #INT           2  -- Detect2.Value
    plc_db16_dt2=str(util.get_date_time_object(dbr16,12))
    plc_db16.append(plc_db16_dt2)                            #DATE&TIME     3  -- Detect2.Timestamp
    plc_db16.append(util.get_int(dbr16,20))                  #INT           4  -- Clamp.Value
    plc_db16_dt3=str(util.get_date_time_object(dbr16,22))
    plc_db16.append(plc_db16_dt3)                            #DATE&TIME     5  -- Clamp.Timestamp

    #OVEN-C.MONITORING DB17-------------------------------------------------------------------------------------------------------------------------
    plc_db17.append(util.get_int(dbr17,0))                   #INT           0  -- Gate.Value
    plc_db17_dt1=str(util.get_date_time_object(dbr17,2))                   
    plc_db17.append(plc_db17_dt1)                            #DATE&TIME     1  -- Gate.Timestamp

    #NOOK-C.MONITORING DB19-------------------------------------------------------------------------------------------------------------------------
    plc_db19.append(util.get_int(dbr19,0))                   #INT           0  -- Status.Type
    plc_db19_dt1=str(util.get_date_time_object(dbr19,2))                   
    plc_db19.append(plc_db19_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db19.append(util.get_string(dbr19, 10))              #STRING        2  -- Status.Value
    plc_db19.append(util.get_int(dbr19,266))                 #INT           3  -- Count.Value
    plc_db19_dt2=str(util.get_date_time_object(dbr19,268))
    plc_db19.append(plc_db19_dt2)                            #DATE&TIME     4  -- Count.Timestamp
    plc_db19.append(util.get_int(dbr19,276))                 #INT           5  -- Slotcounter.Value
    plc_db19_dt3=str(util.get_date_time_object(dbr19,278))
    plc_db19.append(plc_db19_dt3)                            #DATE&TIME     6  -- Slotcounter.Timestamp

    #INSPECTION-C.MONITORING DB20-------------------------------------------------------------------------------------------------------------------
    plc_db20.append(util.get_int(dbr20,0))                   #INT           0  -- Status.Type
    plc_db20_dt1=str(util.get_date_time_object(dbr20,2))                   
    plc_db20.append(plc_db20_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db20.append(util.get_string(dbr20, 10))              #STRING        2  -- Status.Value

    #ROTATIONRACK-C.MONITORING DB22-----------------------------------------------------------------------------------------------------------------
    plc_db22.append(util.get_int(dbr22,0))                   #INT           0  -- Status.Type
    plc_db22_dt1=str(util.get_date_time_object(dbr22,2))                 
    plc_db22.append(plc_db22_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db22.append(util.get_string(dbr22, 10))              #STRING        2  -- Status.Value
    plc_db22.append(util.get_int(dbr22,266))                 #INT           3  -- Detect.Value
    plc_db22_dt2=str(util.get_date_time_object(dbr22,268))
    plc_db22.append(plc_db22_dt2)                            #DATE&TIME     4  -- Detect.Timestamp

    #FINISHEDRACK-C.MONITORING DB23-----------------------------------------------------------------------------------------------------------------
    plc_db23.append(util.get_int(dbr23,0))                   #INT           0  -- Status.Type
    plc_db23_dt1=str(util.get_date_time_object(dbr23,2))                   
    plc_db23.append(plc_db23_dt1)                            #DATE&TIME     1  -- Status.Timestamp
    plc_db23.append(util.get_string(dbr23, 10))              #STRING        2  -- Status.Value
    plc_db23.append(util.get_int(dbr23,266))                 #INT           3  -- Count.Value
    plc_db23_dt2=str(util.get_date_time_object(dbr23,268))
    plc_db23.append(plc_db23_dt2)                            #DATE&TIME     4  -- Count.Timestamp
    plc_db23.append(util.get_int(dbr23,276))                 #INT           5  -- Slotcounter.Value
    plc_db23_dt3=str(util.get_date_time_object(dbr23,278))
    plc_db23.append(plc_db23_dt3)                            #DATE&TIME     6  -- Slotcounter.Timestamp

    #UR3-A.MONITORING DB30-----------------------------------------------------------------------------------------------------------------
    plc_db30.append(util.get_int(dbr30,0))                   #INT           0  -- Tool.value
    plc_db30_dt1=str(util.get_date_time_object(dbr30,2))                  
    plc_db30.append(plc_db30_dt1)                            #DATE&TIME     1  -- Tool.Timestamp
    plc_db30.append(util.get_int(dbr30,10))                  #INT           2  -- Visor.Value              
    plc_db30_dt2=str(util.get_date_time_object(dbr30,12))
    plc_db30.append(plc_db30_dt2)                            #DATE&TIME     3  -- Visor.Timestamp
    plc_db30.append(util.get_string(dbr30, 20))              #STRING        4  -- Status.Type
    plc_db30_dt3=str(util.get_date_time_object(dbr30,276))
    plc_db30.append(plc_db30_dt3)                            #DATE&TIME     5  -- Status.Timestamp
    plc_db30.append(util.get_int(dbr30,284))                 #INT           6  -- Status.Value
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #print(plc_db2)
    plc_db3.append(util.get_string(dbr3, 0))
    client.publish(topics3[0], plc_db3[0],1,True) 

    for i in range(0,1):
        client.publish(topics17[i], plc_db17[i],1,True)

    for i in range(0,2):
        client.publish(topics7[i], plc_db7[i],1,True)
        client.publish(topics20[i], plc_db20[i],1,True)

    for i in range(0,4):
        client.publish(topics10[i], plc_db10[i],1,True)
        client.publish(topics15[i], plc_db15[i],1,True)
        client.publish(topics22[i], plc_db22[i],1,True)

    for i in range(0,5):
        client.publish(topics4[i], plc_db4[i],1,True)
        client.publish(topics11[i], plc_db11[i],1,True)
        client.publish(topics16[i], plc_db16[i],1,True)

    for i in range(0,6):
        client.publish(topics2[i], plc_db2[i],1,True)
        client.publish(topics9[i], plc_db9[i],1,True)
        client.publish(topics14[i], plc_db14[i],1,True)
        client.publish(topics19[i], plc_db19[i],1,True)
        client.publish(topics23[i], plc_db23[i],1,True)
        client.publish(topics30[i], plc_db30[i],1,True)
    
    for i in range(0,10):
        client.publish(topics5[i], plc_db5[i],1,True)
    
    for i in range(0,18):
        client.publish(topics12[i], plc_db12[i],1,True)

    # plc_db3.append(util.get_int(dbr3,274))                   #INT           0  -- Status.Type
    # client.publish(topics3[4], plc_db3[0])

    # #WRITE TAGS TO PLC---------------------------------------------------------------------------------------------------------------------------------------
    #UR3-A.CONTROLLER -- DB3
    #print(data_read)
                   #STRING        2  -- Status.Value
    #util.set_string(dbr3,0,data_read[0])
    util.set_int(dbr3,264,data_read[2])  
    util.set_int(dbr3,274,data_read[4])  
    util.set_int(dbr3,284,data_read[6])  
    util.set_bool(dbr3,294,0,data_read[8])  
    util.set_int(dbr3,296,data_read[9])  
    #util.set_bool(dbr3,306,0,data_read[11])  
    #util.set_int(dbr3,316,data_read[13]) 
    plc.db_write(DB_NUM_3, START_ADDRESS3, dbr3)
    

    # util.set_int(dbr18,0,data_read[0])                  # (bytearray, byte_index:int,bool_index:int,value: bool)
    # util.set_bool(dbr18,10,0,data_read[2])              # (bytearray, byte_index:int,value_real:real)
    # plc.db_write(DB_NUM_18, START_ADDRESS18, dbr18)     #as_db_write(db_number: int, start: int, size: int, data)
    #time.sleep(1)
    end = time.time()
    tiempo = round(end - start,2)
    print('Publicando '+ str(j) +' --  '+ str(tiempo))
    j = j+1
    plc_db2   = []
    plc_db3   = []
    plc_db4   = []
    plc_db5   = []
    plc_db6   = []
    plc_db7   = []
    plc_db8   = []
    plc_db9   = []
    plc_db10  = []
    plc_db11  = []
    plc_db12  = []
    plc_db13  = []
    plc_db14  = []
    plc_db15  = []
    plc_db16  = []
    plc_db17  = []
    plc_db18  = []
    plc_db19  = []
    plc_db20  = []
    plc_db21  = []
    plc_db22  = []
    plc_db23  = []
    plc_db24  = []
    plc_db25  = []
    plc_db26  = []
    plc_db27  = []
    plc_db28  = []
    plc_db29  = []
    plc_db30  = []
    
