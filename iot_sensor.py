import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub") # puclisher 이름
mqttc.connect("127.0.0.1", 1883)
mqttc.publish("/registration/bulbs/bulb1", payload = "on", qos=0, retain=False) 

def on_message(client, userdata, message):
        print("message received ", str(message.payload.decode("utf-8")))
        print("message topic= ", message.topic)
        print("message qos=", message.qos)
        print("message retain flag= ", message.retain)

borker_address = "0.0.0.0"
client1 = mqtt.Client("client1")
client1.connect(borker_address)
client1.subscribe("/registration/bulbs/blub1")
client1.on_message = on_message
client1.loop_forever()
