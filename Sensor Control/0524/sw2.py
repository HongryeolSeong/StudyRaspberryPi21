#-*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switchi1 = 6
switchi2 = 13
switcho = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchi1, GPIO.IN)
GPIO.setup(switchi2, GPIO.IN)
GPIO.setup(switcho, GPIO.OUT)

try:
	while True:
		if GPIO.input(switchi1) == True:
			print("On Pushed")
			time.sleep(0.3)
			GPIO.output(switcho,True)
		elif GPIO.input(switchi2) == True:
			print("Off Pushed")
			time.sleep(0.3)
			GPIO.output(switcho,False)

except KeyboardInterrupt:
	GPIO.cleanup()
