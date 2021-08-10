#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

triggerPin = 16
echoPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)


try:
	while True:
		GPIO.output(triggerPin, GPIO.LOW)
		time.sleep(0.00001)
		GPIO.output(triggerPin, GPIO.HIGH)

		while GPIO.input(echoPin) == 0: #초음파 전송이 끝나는 전송시간
			start = time.time()         #을 저장
		while GPIO.input(echoPin) == 1: #초음파 수신이 완료된 때 시간
			stop = time.time()          #을 저장

		rtTotime = stop - start
		distance = rtTotime * 34000 / 2
		print("distance : %.2fcm" % distance)

		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
