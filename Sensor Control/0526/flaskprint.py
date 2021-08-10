from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
	return "Hello Flask"

@app.route('/name')
def name():
	return "<h1> My name is Hong </h1>"

@app.route('/age')
def age():
	return "<h1> I'm 27 years old </h1>"

@app.route('/job')
def job():
	return "<h1> My job is student </h1>"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8080")
