import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import sys
import threading
import signal
import os
import time

# event_stop = threading.Event()
# event_pause = threading.Event()
# event_stop.clear()
# event_pause.clear()

pin = 18        # 라인 근접 센서
mpin1 = 20      # 앞 왼 바퀴1
mpin2 = 21      # 앞 왼 바퀴2
mpin3 = 6       # 앞 오 바퀴1
mpin4 = 12      # 앞 오 바퀴2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
GPIO.setup(mpin1, GPIO.OUT)
GPIO.setup(mpin2, GPIO.OUT)
GPIO.setup(mpin3, GPIO.OUT)
GPIO.setup(mpin4, GPIO.OUT)

m1 = GPIO.PWM(mpin1, 100)
m2 = GPIO.PWM(mpin2, 100)
m3 = GPIO.PWM(mpin3, 100)
m4 = GPIO.PWM(mpin4, 100)

GPIO.output(mpin1, False)
GPIO.output(mpin2, False)
GPIO.output(mpin3, False)
GPIO.output(mpin4, False)

def set_left():
    GPIO.output(mpin1, False)
    GPIO.output(mpin2, True)
    GPIO.output(mpin3, False)
    GPIO.output(mpin4, True)

def set_right():
    GPIO.output(mpin1, True)
    GPIO.output(mpin2, False)
    GPIO.output(mpin3, True)
    GPIO.output(mpin4, False)

def set_start():
    GPIO.output(mpin1, True)
    GPIO.output(mpin2, False)
    GPIO.output(mpin3, False)
    GPIO.output(mpin4, True)

def stop():
    GPIO.output(mpin1, False)
    GPIO.output(mpin2, False)
    GPIO.output(mpin3, False)
    GPIO.output(mpin4, False)

# def setSpeed(speed, p1, p2):
#     p1.ChangeDutyCycle(speed*10)
#     p2.ChangeDutyCycle(speed*10)

def on_message(client, userdata, message):
    topic=str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic+message)

    if message == 's':
        set_start()
    elif message == 't':
        stop()
    elif message == 'l':
        set_left()
    elif message == 'r':
        set_right()
    else: pass

broker_address='210.119.12.93'
pub_topic = 'MOTOR/TEST/'
print("creating new instance")
client=mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.subscribe(pub_topic)

# client.on_connect = on_connect
# client.on_disconnect = on_disconnect
client.on_message = on_message

try:
    while True:
        client.loop_forever()

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()