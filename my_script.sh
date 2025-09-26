#!/bin/bash
# This script automates creation of Flask venv
echo -e "Welcome to the Flask Automation Script!\n"
echo "Author: Eoghan McGough"

echo "Installing Dependencies..."
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y nano vim python-is-python3 python3-venv python3-pip

echo "Setting up Virtual Environment..."
python -m venv .my_venv2
source .my_venv2/bin/activate
pip install flask

echo "Creating Python File..."
cat <<EOF > hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "<p>Hello, Flask!</p><a href='/about'>About</a>"

@app.route("/about")
def say_about():
    return "<p>About!</p><a href='/'>Home</a>"
EOF

echo "Running Flask App..."
flask --app hello run --host=0.0.0.0
