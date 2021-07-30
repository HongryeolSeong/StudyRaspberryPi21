#-*- coding: utf-8-*- #주석설정
import RPi.GPIO as GPIO #RPi.GPIO 모듈내 함수 사용
import time

switch = 6		#입력핀설정

GPIO.setmode(GPIO.BCM)	#BCM 모드

GPIO.setup(switch, GPIO.IN) #핀모드(입력)

try:
	while True:
		if GPIO.input(switch) == True:
			print("Pushed")
			time.sleep(0.3) #스위치의 미세한 진동에의한 값 무시

except KeyboardInterrupt:
	GPIO.cleanup()
