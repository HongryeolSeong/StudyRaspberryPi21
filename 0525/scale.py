#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

pinPiezo = 6
Melody = [400, 400, 500, 500, 400, 400, 300, 400, 400, 300, 300, 250, 400, 400, 500, 500, 400, 400, 300, 350, 300, 250, 300, 100]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)

try:
	while True:
		Buzz.start(50)
		for i in range(0, len(Melody)):
			Buzz.ChangeFrequency(Melody[i])
			time.sleep(0.5)
		Buzz.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
