#-*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switchi = 5
switcho = 6
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchi, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(switcho, GPIO.OUT)

def swBlink(channel):
	global flag
	if flag == False:
		print("interrupt_LED_ON")
		GPIO.output(switcho, True)
		flag = True
	else:
		print("interrupt_LED_OFF")
		GPIO.output(switcho, False)
		flag = False

GPIO.add_event_detect(switchi, GPIO.RISING, callback=swBlink)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
