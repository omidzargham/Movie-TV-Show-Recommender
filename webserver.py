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

api_base_url = "https://api.themoviedb.org/3/"

image_base_url = "https://image.tmdb.org/t/p/w1280" #append "poster_path" attribute to this url to get image for movie/tv show

youtube_url = "https://www.youtube.com/embed/" #append video "key" attribute to this url to get trailer for a particular movie/tv show


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

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/movie")
def movie():
    return render_template("genres.html")

@app.route("/tv")
def tv():
    return render_template("genres.html")

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

    discover_params = "?api_key=" + os.environ['API_KEY'] + "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"    
    discover_url = api_base_url + "discover/" + entertainment_type + discover_params + "&with_genres=" + genre_id
    r = requests.get(discover_url)
    movie_list = r.json()["results"]
    return render_template("list.html", type=entertainment_type, list=movie_list, image_url=image_base_url) # need to properly place in movie data

@app.route("/selection")
def display_selection():
    entertainment_type = request.args.get("entertainment_type")
    ID = request.args.get("id")
    selection_params = "?api_key=" + os.environ['API_KEY'] + "&language=en-US&append_to_response=videos" #Gets movie details and Youtube IDs to get trailer from Youtube
    selection_url = api_base_url + entertainment_type + "/" + str(ID) + selection_params 
    r = requests.get(selection_url)
    return render_template("selection.html", type=entertainment_type, selection=r.json(), image_url=image_base_url, youtube_url=youtube_url)



if __name__ == "__main__":
	app.run()
