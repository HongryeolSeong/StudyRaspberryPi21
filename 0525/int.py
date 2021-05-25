#-*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch = 5
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)	#내부풀다운 사용

def swBlink(channel):	# callback 함수
	global flag
	if flag == False:
		print("interrupt")
		flag = True
	else:
		flag = False
#인터럽터핀에 라이징신호가 인가되면 콜백함수로 리턴되어 실행된다.
GPIO.add_event_detect(switch, GPIO.RISING, callback=swBlink)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
