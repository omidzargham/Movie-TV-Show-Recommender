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

discover_base_url= "https://api.themoviedb.org/3/discover/" # + "movie" or "tv"

discover_params = "?api_key=" + os.environ['API_KEY'] + "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"

def getGenres():
    genres = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=" + os.environ['API_KEY'] + "&language=en-US")
    return genres

genre_list = getGenres().json()["genres"]

@app.route("/")
def home_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route("/movie")
def movie():
    return render_template("movie.html")

@app.route("/tv")
def tv():
    return render_template("tv.html")

@app.route("/list")
def generate_list():
    entertainment_type = request.args.get("entertainment_type")
    genre_name = request.args.get("genre")
    with_genre_id = ""
    without_genre_ids = ""

    for genre in genre_list:
        if (genre["name"] == genre_name):
            genre_id = str(genre["id"])
            break
           
    discover_url = discover_base_url + entertainment_type + discover_params + "&with_genres=" + genre_id
    r = requests.get(discover_url)
    print(r.json())
    return render_template("list.html") #should be list.html



if __name__ == "__main__":
	app.run()
