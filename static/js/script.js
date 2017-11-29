function setMovie() {

    localStorage.setItem('entertainment_type', 'movie');

}



function setTV() {

    localStorage.setItem('entertainment_type', 'tv');

}

function addURLParams(element) {

    $(element).attr('href', function() {

        var entertainment_type = localStorage.getItem('entertainment_type');
        var genre = $(element).attr('id')
        return this.href + "?entertainment_type=" + entertainment_type + "&genre=" + genre;
    });

}

function addMovieID(element) {
    
        $(element).attr('href', function() {
    
            var entertainment_type = localStorage.getItem('entertainment_type');
            var id = $(element).attr('movie-id')
            return this.href + "?entertainment_type=" + entertainment_type + "&id=" + id;
        });
    
    }