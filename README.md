# iot

1. mosquitto 실행
  mosquitto

안되면(포트가 사용중이라면) 어떤 프로세스가 사용중인지 확인하기
'''
sudo netstat -anlp | grep:1883
pkill mosquitto
'''

3. device 실행
flask 사용 등 과정에서 sudo 권환이 필요
'''
sudo python3 iot_device.py

'''

3. sensor 실행
개발했다면 실행 X
'''
python3 iot_sensor.py
'''


5. curl을 통해 GET 요청 보내기
'''
curl -X GET -H "Content-Type: application/json" -d '{"data": "on"}' "127.0.0.1:80/registration/bulbs/bulb1"
'''
