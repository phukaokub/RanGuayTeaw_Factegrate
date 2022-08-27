import json
from time import sleep
import urllib3

'''
ตัวอย่างการควบคุมกระบอกลม (Actuator) ตัวหมายเลข 0 ที่ติดตั้งอยู่ใน TeleSorting System หมายเลข 0
'''

http    = urllib3.PoolManager()

for t in range(3):

    # Activate
    data_json   = {"action" : 1}
    data_encode = json.dumps(data_json).encode("utf-8")
    
    res = http.request("POST",
                        "http://localhost/tss/0/actuator/0",
                        body=data_encode,
                        headers={"Content-Type" : "application/json"})
    
    text    = res.data.decode("utf-8")
    print(text)

    sleep(1)

    # Deactivate
    data_json   = {"action" : 0}
    data_encode = json.dumps(data_json).encode("utf-8")
    
    res = http.request("POST",
                        "http://localhost/tss/0/actuator/0",
                        body=data_encode,
                        headers={"Content-Type" : "application/json"})
    
    text    = res.data.decode("utf-8")
    print(text)

    sleep(1)

'''
ตัวอย่างการอ่านข้อมูลจาก Sensor ตัวหมายเลข 0 ที่ติดตั้งอยู่ใน TeleSorting System หมายเลข 0
'''

http    = urllib3.PoolManager()

for t in range(100):

    res = http.request( "GET",
                        "http://localhost/tss/0/sensor/0"
                        )
    text    = res.data.decode("utf-8")
    print(text)

    sleep(0.1)