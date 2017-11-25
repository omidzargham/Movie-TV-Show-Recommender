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

base_url= "https://api.themoviedb.org/3/discover/movie?api_key=" + os.environ['API_KEY'] + "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"

entertainment_type = "" # save this in local storage on browser

@app.route("/")
def home_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route("/movie")
def movie():
    entertainment_type = "movie"
    return render_template("movie.html")

@app.route("/tv")
def tv():
    entertainment_type = "tv"
    return render_template("tv.html")

@app.route("/list", methods=['POST'])
def generate_list():
    genre = "action"
    discover_url = base_url + "&with_genre=" + genre
    r = requests.get(discover_url)
    print(r.json())
    return render_template("movie.html") #should be list.html

	

if __name__ == "__main__":
	app.run()
