import RPi.GPIO as GPIO
import sys
import time


pin = 18        # 라인 근접 센서
mpin1 = 20      # 앞 왼 바퀴1
mpin2 = 21      # 앞 왼 바퀴2
mpin3 = 6       # 앞 오 바퀴1
mpin4 = 12      # 앞 오 바퀴2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
GPIO.setup(mpin1, GPIO.OUT)
GPIO.setup(mpin2, GPIO.OUT)
GPIO.setup(mpin3, GPIO.OUT)
GPIO.setup(mpin4, GPIO.OUT)

m1 = GPIO.PWM(mpin1, 100)
m2 = GPIO.PWM(mpin2, 100)
m3 = GPIO.PWM(mpin3, 100)
m4 = GPIO.PWM(mpin4, 100)

GPIO.output(mpin1, False)
GPIO.output(mpin2, False)
GPIO.output(mpin3, False)
GPIO.output(mpin4, False)

def setSpeed(speed, p1, p2):
    p1.ChangeDutyCycle(speed*10)
    p2.ChangeDutyCycle(speed*10)

try:
    m1.start(0) # start the PWM on 0% duty cycle
    m2.start(0) # start the PWM on 0% duty cycle
    m3.start(0) # start the PWM on 0% duty cycle
    m4.start(0) # start the PWM on 0% duty cycle
    
    while True:
        if GPIO.input(pin) == False:
            print("Black")
            
            for i in range(10):
                GPIO.output(mpin1, True)
                GPIO.output(mpin2, False)
                GPIO.output(mpin3, False)
                GPIO.output(mpin4, True)
                setSpeed(i, m1, m4)
                time.sleep(1)
        elif GPIO.input(pin) == True:
            print("White")
            GPIO.output(mpin1, False)
            GPIO.output(mpin2, False)
            GPIO.output(mpin3, False)
            GPIO.output(mpin4, False)
            time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()