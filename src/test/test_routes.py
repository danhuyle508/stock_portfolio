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
        assert rv.status_code == 200   

    def test_preview_route_get(self, session):
        rv = app.test_client().post('/preview_page', data={'symbol' : 'goog'})
        assert rv.status_code == 405

    def test_register_get(self, session):
        rv = app.test_client().get('/register')
        assert b'<h2>Register:</h2>' in rv.data

    def test_login_get(self, session):
        rv = app.test_client().get('/login')
        assert b'<h2>Login</h2>' in rv.data

    def test_register_post(self, session):
        rv = app.test_client().post('/register', data={'email': 'dog@gmail.com', 'password': '123'})
        assert rv.status_code == 405
    def test_lgoin_post(self, session):
        rv = app.test_client().post('/login', data={'email': 'dog@gmail.com', 'password': '123'})
        assert rv.status_code == 405    