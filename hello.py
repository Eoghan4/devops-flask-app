from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
	return "<p>Welcome, Flask!</p><a href='/about'>About</a><a href='/contact'>Contact</a>"

@app. route("/about")
def say_about():
	return "<p>About!</p> <a href='/'>Home</a>"

@app. route("/contact")
def say_contact():
        return "<p>Contact! C23362336@mytudublin.ie</p> <a href='/'>Home</a>"
