from src import app
import pytest

class TestClass():

    def test_home_route_get_status(self):
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert b'<title>Home</title>' in rv.data

    def test_search_route_get_status(self):
        rv = app.test_client().get('/search')
        assert rv.status_code == 200
        assert b'<h1>search</h1>' in rv.data

    def test_protfolio(session):
        rv = app.test_client().get('/portfolio')
        assert rv.status_code == 200
        assert b'<h1>Coming soon.</h1>' in rv.data
        
    def test_search_route_post():
        res app.test_client().post('/search', data={'symbol': 'goog'})
        asser rv.status_code == 302    
