#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

triggerPin = 4
echoPin = 14
speaker = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(speaker, GPIO.OUT)

Buzz = GPIO.PWM(speaker, 440)

try:
	while True:
		GPIO.output(triggerPin, GPIO.LOW)
		time.sleep(0.00001)
		GPIO.output(triggerPin, GPIO.HIGH)

		while GPIO.input(echoPin) == 0:
			start = time.time()
		while GPIO.input(echoPin) == 1:
			stop = time.time()

		rtTotime = stop - start
		distance = rtTotime * 34000 / 2
		print("distance : %.2fcm" % distance)

		if distance < 5:
			for i in range(5):
				Buzz.start(50)
				Buzz.ChangeFrequency(200)
				time.sleep(0.1)
				Buzz.stop()
				time.sleep(0.03)
			time.sleep(0.02)
		elif distance > 5 and distance < 10:
			for i in range(3):
				Buzz.start(50)
				Buzz.ChangeFrequency(200)
				time.sleep(0.2)
				Buzz.stop()
				time.sleep(0.03)
			time.sleep(0.035)
		elif distance > 10 and distance < 20:
			for i in range(2):
				Buzz.start(50)
				Buzz.ChangeFrequency(200)
				time.sleep(0.25)
				Buzz.stop()
				time.sleep(0.03)
			time.sleep(0.1)
		elif distance > 20 and distance < 30:
			Buzz.start(50)
			Buzz.ChangeFrequency(200)
			time.sleep(0.3)
			Buzz.stop()
			time.sleep(0.5)
		else:
			time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
