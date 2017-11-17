"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request	
import os
import requests

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route("/")
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/movie")
def movie():
	return render_template("movie.html")

@app.route("/tv")
def tv():
	return render_template("tv.html")
	

if __name__ == "__main__":
	app.run()
