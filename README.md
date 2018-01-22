[![Build Status](https://travis-ci.org/omidzargham/entertainment-recommender.svg?branch=master)](https://travis-ci.org/omidzargham/entertainment-recommender)
# Movie/TV Show Recommendations

### URL

available at: http://entertainmentrecommender.herokuapp.com/

### Overview:

A web application that recommends the most popular movies and TV shows by genre. Supports common genres such as action, adventure, animation, comedy, drama, horror, romance, and sci-fi. The application queries the MovieDB API to obtain a list of results and displays information such as the release date, rating, overview, and trailer.

To run locally, you will need MovieDB API key. Once you obtain one, clone this repo, cd into the directory you just made, and type this into your terminal:

```
pip install -r requirements.txt
export API_KEY={your api key}
export FLASK_APP=webserver.py
flask run
```

By Omid Zargham, Omid Afshar, Divine Velasquez, Camille Harris
