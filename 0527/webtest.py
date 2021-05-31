from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

ledPin = 21
Melody = [400, 400, 500, 500, 400, 400, 300, 400, 300, 300, 250, 400 , 400]
triggerPin = 4
echoPin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/data', methods = ['Post'])
def data():
	data = request.form['led']
	if data == 'on':
		GPIO.output(ledPin, True)
		return home()
	elif data == 'off':
		GPIO.output(ledPin, False)
		return home()
	elif data == 'clean':
		GPIO.output(ledPin, False)
		GPIO.cleanup()
		return home()
	elif data == 'restart':
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(ledPin, GPIO.OUT)
		return home()
	elif data == 'start1':
		p = GPIO.PWM(ledPin, 255)
		p.start(0)
		while True:
			for i in range(10):
				p.ChangeDutyCycle(i)
				time.sleep(0.1)
			for i in reversed(range(10)):
				p.ChangeDutyCycle(i)
				time.sleep(0.1)
		return home()
	elif data == 'clean1':
		GPIO.cleanup()
		return home()
	elif data == 'restart1':
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(ledPin, GPIO.OUT)
		return home()
	elif data == 'start2':
		Buzz = GPIO.PWM(ledPin, 440)
		while True:
			Buzz.start(50)
			for i in range(0, len(Melody)):
				Buzz.ChangeFrequency(Melody[i])
				time.sleep(0.5)
			Buzz.stop()
			time.sleep(1)
	elif data == 'clean2':
		GPIO.cleanup()
		return home()
	elif data == 'restart2':
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(lenPin, GPIO.OUT)
		return home()
	elif data == 'start3':
		Buz = GPIO.PWM(ledPin, 440)
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
					Buz.start(50)
					Buz.ChangeFrequency(200)
					time.sleep(0.1)
					Buz.stop()
					time.sleep(0.03)
				time.sleep(0.02)
			elif distance > 5 and distance < 10:
				for i in range(3):
					Buz.start(50)
					Buz.ChangeFrequency(200)
					time.sleep(0.2)
					Buz.stop()
					time.sleep(0.03)
				time.sleep(0.035)
			elif distance > 10 and distance < 20:
				for i in range(2):
					Buz.start(50)
					Buz.ChangeFrequency(200)
					time.sleep(0.25)
					Buz.stop()
					time.sleep(0.03)
				time.sleep(0.1)
			elif distance > 20 and distance < 30:
				Buz.start(50)
				Buz.ChangeFrequency(200)
				time.sleep(0.3)
				Buz.stop()
				time.sleep(0.5)
			else:
				time.sleep(0.5)
	elif data == 'clean3':
		GPIO.cleanup()
		return home()

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8080")
