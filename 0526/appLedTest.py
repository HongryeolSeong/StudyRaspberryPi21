from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def flask():
	return "Hello Flask"

@app.route('/led/on')
def ledOn():
	GPIO.output(ledPin, True)
	return "<h1> Led On </h1>"

@app.route('/led/off')
def ledOff():
	GPIO.output(ledPin, False)
	return "<h1> Led Off </h1>"

@app.route('/led/clean')
def clean():
	GPIO.cleanup()	#GPIO 라이브러리/모듈이 점유한 리소스를 해제하는 기능
	return "<h1> GPIO Clean </h1>"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8080")
