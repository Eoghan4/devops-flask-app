from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
	return "<p>Hello, Flask!</p><a href='/about'>About</a>"

@app. route( " / about " )
def say_about():
	return "<p>About!</p> <a href='/'>Home</a>"
