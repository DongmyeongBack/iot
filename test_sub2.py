import paho.mqtt.client as mqtt

# subscriber callback
def on_message(client, userdata, message):
        print("message received ", str(message.payload.decode("utf-8")))
        print("message topic= ", message.topic)
        print("message qos=", message.qos)
        print("message retain flag= ", message.retain)

broker_address = "0.0.0.0"
client1 = mqtt.Client("client2")
client1.connect(broker_address)
client1.subscribe("동명/개인정보")
client1.on_message = on_message
client1.loop_forever()
