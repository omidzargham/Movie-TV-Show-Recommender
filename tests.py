from webserver import getGenres

def test_genres():
    assert getGenres.status_code == 200
