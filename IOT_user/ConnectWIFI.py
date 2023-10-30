import ezwifi
import time

w = ezwifi.Wifi()

def detect(ssid, password):
    w.scan()
    wifiList = w.get_list()
    print("wifi scan succes")
    print(wifiList)
    for wifi in wifiList:
        if(wifi['ssid'] == ssid):
            w.connect(ssid, password)
            return
        else:
            print("detected wifi")
            print(wifi)


ssid = 'KENTECH_RC'
password = 'kentech123456!'
while True:
    detect(ssid, password)
    time.sleep(5)
    print("scan again")