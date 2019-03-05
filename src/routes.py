from flask import render_template, abort, redirect, url_for, request
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, Company
from . import app
import requests
import json
import os

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/search', methods=['GET', 'POST'])
def company_search():   
    if request.method == 'POST':

        symbol = request.form.get('symbol')

        url = f'https://api.iextrading.com/1.0/stock/{symbol}/company'

        res = requests.get(url)
        data = json.loads(res.text)

        company = Company(name=data['companyName'], symbol=data['symbol'])

        # db.session.add(company)
        # db.session.commit()

        return redirect(url_for('.portfolio_page'), code=302)

    return render_template('weather/search.html'), 200

@app.route('/portfolio', methods=['GET'])
def portfolio_page():
    return render_template('./weather/portfolio.html'), 200       


