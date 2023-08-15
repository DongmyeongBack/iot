import paho.mqtt.client as mqtt
from flask import Flask, request 
from flask_restx import Resource, Api

print("script start")

app = Flask(__name__)
api = Api(app)


# subscriber callback
def on_messages(client, userdata, message):
        global topicGlobal
        topicGlobal = message.topic
        recv_message = str(message.payload.decode("utf-8"))
        print("message received ", str(message.payload.decode("utf-8")))
        print("message topic= ", message.topic)
        print("message qos=", message.qos)
        print("message retain flag= ", message.retain)
        client.disconnect()
        print("disconnect")

broker_address = "0.0.0.0"
client1 = mqtt.Client("device_flask")
client1.connect(broker_address)
print("Connected")
client1.subscribe("/registration/#") # 중간은 +, 마지막은 #
print("Subscribe")
topicGlobal = ''
client1.on_message = on_messages
client1.loop_forever()

print("step2")


@api.route(topicGlobal)
class Action(Resource):
    def get(self):
        data = request.json.get('data')
        print("topic = ", topicGlobal, '\n', "data = ", data)
        # publish하기
        mqttc = mqtt.Client("python_pub")
        mqttc.connect("127.0.0.1", 1883)
        mqttc.publish(topicGlobal, payload = data, qos=0, retain=False)
        return {
            'data': data
            }

if __name__ == '__main__':
    print("Server start")
    app.run(debug=True, host='0.0.0.0', port=80, use_reloader=False)

