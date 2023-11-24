import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub") # puclisher 이름
mqttc.connect("0.0.0.0", 1883)
mqttc.publish("/hello", payload = "off", qos=0, retain=False) # topic, message


