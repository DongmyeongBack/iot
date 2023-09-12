# iot

1. mosquitto 실행
  <pre><code>
    mosquitto
  </code>
  </pre>
안되면(포트가 사용중이라면) 어떤 프로세스가 사용중인지 확인하기
  <pre><code>
  sudo netstat -anlp | grep:1883
  pkill mosquitto
  </code>
  </pre

3. device 실행
flask 사용 등 과정에서 sudo 권환이 필요
sudo python3 iot_device.py
<pre><code>
    sudo python3 iot_device.py
  </code>
  </pre>

3. sensor 실행
개발했다면 실행 X
python3 iot_sensor.py
<pre><code>
python3 iot_sensor.py
  </code>
  </pre>


5. curl을 통해 GET 요청 보내기
<pre><code>
curl -X GET -H "Content-Type: application/json" -d '{"data": "on"}' "127.0.0.1:80/registration/bulbs/bulb1"
  </code>
  </pre>
