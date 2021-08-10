#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time
import keyboard

pinPiezo = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)

try:
	while True:
		a = int(input())
		Buzz.start(50)

		if a == 1:
			Buzz.ChangeFrequency(100)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 2:
			Buzz.ChangeFrequency(200)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 3:
			Buzz.ChangeFrequency(300)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 4:
			Buzz.ChangeFrequency(400)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 5:
			Buzz.ChangeFrequency(500)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 6:
			Buzz.ChangeFrequency(600)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 7:
			Buzz.ChangeFrequency(700)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 8:
			Buzz.ChangeFrequency(800)
			time.sleep(0.4)
			Buzz.stop()
		elif a == 9:
			Buzz.ChangeFrequency(900)
			time.sleep(0.4)
			Buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()