from flask import render_template, abort, redirect, url_for, request, session, flash
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, Company
from .forms import CompanyForm, CompanyAddForm
from . import app
import requests
import json
import os

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/search', methods=['GET', 'POST'])
def company_search():   

    form = CompanyForm()

    if form.validate_on_submit():

        symbol = form.data['symbol']

        url = f'https://api.iextrading.com/1.0/stock/{symbol}/company'

        res = requests.get(url)
        data = json.loads(res.text)

        session['context'] = data
        session['symbol'] = symbol

        return redirect(url_for('.preview_page'), code=302)

    return render_template('weather/search.html', form = form), 200

@app.route('/portfolio', methods=['GET'])
def portfolio_page():
    companies = Company.query.all()
    return render_template('portfolio.html', companies=companies), 200       

@app.route('/preview', methods=['GET', 'POST'])
def preview_page():

    form_context = {
        'name': session['context']['companyName'],
        'symbol': session['symbol']
    }

    form = CompanyAddForm(**form_context)
    if form.validate_on_submit():
        try:
            new_company = Company(name=form.data['name'], symbol=form.data['symbol'])
            print(new_company)
            db.session.add(new_company)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Something went wrong with your search.')
            return redirect(url_for('.company_search'))

        return redirect(url_for('.portfolio_page'))

    return render_template(
        'preview.html',
        form=form,
        symbol=form_context['symbol'],
        symbol_data=session['context'],
    )        