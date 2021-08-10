#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

ledPin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 255)

p.start(0)

try:
	while True:
		for i in range(100):
			p.ChangeDutyCycle(i)
			time.sleep(0.1)
		for i in reversed(range(100)):
			p.ChangeDutyCycle(i)
			time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
