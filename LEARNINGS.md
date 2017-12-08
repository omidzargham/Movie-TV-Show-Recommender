# Movie/TV Show Recommendations

By Omid Afshar, Omid Zargham, Divine Velasquez, Camille Harris

### URL

Our application is available at: 

### Overview:

Our web application recommends the most popular movies and TV shows by genre. Upon arriving to our website, a user will be prompted with the choice to search for movies or TV shows. Once the user selects one of these options, they will choose a particular genre that they are interested in viewing from the following choices: Action, Adventure, Animation, Comedy, Drama, Horror, Romance, and Sci-Fi. Based on the entertainment type and genre the user selected (i.e. action movie), our application queries the MovieDB API to obtain a list of results that we then display on our website in order of popularity. The user can then select each result to see various information about it, including the title, release date, rating, overview, and trailer (if there is one available). 


### Technologies Used:

#### HTML

HTML determines the structure of each distinct page of our website.

#### CSS

CSS is used to styles various elements of our website. It is specifically used on top of Bootstrap's styles.

#### Javascript

Javascript is specifically used to store values in the web browser's local storage as well as to append URL parameters upon clicking specific links, such as when selecting a particular genre.

#### jQuery

jQuery is a Javascript library required by Bootstrap and specifically used in our website to add "onclick" methods for the buttons in our application.

#### Bootstrap

Bootstrap is a front-end web framework used throughout our website for styling and layout purposes.

#### Python

Python serves as the back-end programming language for the server. It is the language in which Flask operates.

#### Flask

Flask is a microframework that allows us to control the server's responses to GET and POST requests. We also use the Jinja2 template engine to assist in adding content to our HTML templates.

#### MovieDB API

The MovieDB is an online movie and television database. We utilize its API in our application to get a list of movies or TV shows corresponding to a particular genre, and to get information, images, and trailers for specific movies and TV shows. 

#### JSON

JSON (JavaScript Object Notation) is the format in which the API sends data to the web server.

#### Heroku

Heroku is a Platform as a Service (PaaS) that hosts our web application.