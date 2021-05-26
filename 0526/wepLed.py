from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/data', methods = ['POST'])
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

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8080")
