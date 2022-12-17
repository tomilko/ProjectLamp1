import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
		result = "<a href='/1'>ON</a><br></br>"
		result += "<a href='/2'>OFF</a>"
		return result

@app.route("/1")
def on():
		os.system("echo 1 > /sys/class/gpio/gpio199/value")
		return "Lamp is ON<br></br><a href='/'>Back to main page</a>"
		
@app.route("/2")
def off():
		os.system("echo 0 > /sys/class/gpio/gpio199/value")
		return "Lamp is OFF<br></br><a href='/'>Back to main page</a>"
