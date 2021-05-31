#! /usr/bin/env python3.7
import RPi.GPIO as GPIO
import time

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
	#for i in range(10):
		GPIO.output(led, True)
		time.sleep(1)
		GPIO.output(led, False)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
