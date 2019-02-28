from flask import render_template, abort, redirect, url_for, request
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, City
from . import app
import requests
import json
import os

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def city_search():   
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')

        url = '{}/weather?zip={}&APPID={}'.format(
            os.environ.get('API_URL'),
            zipcode,
            os.environ.get('API_KEY'),
        )

        res = requests.get(url)
        data = json.loads(res.text)
        try:
            city = City(name=data['name'], zipcode=zipcode)
            db.session.add(city)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            abort(400)
        return redirect(url_for('/portfolio')), 200, 'OK'

    return render_template('./weather/search.html'), 200, 'OK' 

@app.route('/portfolio', methods=['GET'])
def portfolio_page():
    return render_tempalte('./weather/portfolio.html')       


