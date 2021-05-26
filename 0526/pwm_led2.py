#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

ledPin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 25)

p.start(0)

while True:
	d = input("Enter Brightness(0 to 100) : ")
	duty = int(d)

	if(duty == 100):
		p.stop()
		GPIO.cleanup()
		break
	else:
		p.ChangeDutyCycle(duty)
		time.sleep(0.4)
