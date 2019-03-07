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
        assert b'<h1>Search for a company</h1>' in rv.data

    def test_protfolio(self, session):
        rv = app.test_client().get('/portfolio')
        assert rv.status_code == 200
        assert b'<h2>Welcome to the portfolio</h2>' in rv.data
        
    def test_search_route_post(self, session):
        rv = app.test_client().post('/search', data={'symbol': 'goog'})
        assert rv.status_code == 302    

    def test_preview_route_ get(self, session):
        rv = app.test_client().post('/preview_page', data={'symbol' : 'goog'})
        assert rv.status_code == 302
