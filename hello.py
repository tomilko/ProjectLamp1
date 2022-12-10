import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
		return "<a href='/1'>ON</a><a href='/2'>OFF</a>"

@app.route("/1")
def on():
		os.system("echo 1 > /sys/class/gpio/gpio199/value")
		return "ON"
		
@app.route("/2")
def off():
		os.system("echo 0 > /sys/class/gpio/gpio199/value")
		return "OFF"
