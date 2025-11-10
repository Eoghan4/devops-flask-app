from flask import Flask
import os # Import os module to handle environment variables

# Assuming Redis integration (even if commented out for now)
# To avoid crashes related to missing Redis connection:
# REDIS_HOST = os.environ.get('REDIS_HOST', 'the-redis-server')
# cache = redis.Redis(host=REDIS_HOST, port=6379) 

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "<p>Welcome, Flask!</p><a href='/about'>About</a><a href='/contact'>Contact</a>"

@app.route("/about")
def say_about():
    return "<p>About!</p> <a href='/'>Home</a>"

@app.route("/contact")
def say_contact():
    return "<p>Contact! C23362336@mytudublin.ie</p> <a href='/'>Home</a>"

# --- THE CRITICAL FIX ---
# This block tells the Python script to run the web server and keep it alive,
# binding it to 0.0.0.0 so it's accessible inside the container.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
# --- END CRITICAL FIX ---