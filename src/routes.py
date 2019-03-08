from flask import render_template, abort, redirect, url_for, request, session, flash
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, Company, Portfolio
from .forms import CompanyForm, CompanyAddForm, PortfolioCreateForm
from . import app
from .auth import login_required
import requests
import json
import os

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.add_template_global
def get_portfolios():
 
    return Portfolio.query.all()    

@app.route('/search', methods=['GET', 'POST'])
@login_required
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

@app.route('/portfolio', methods=['GET','POST'])
@login_required
def portfolio_page():
    
    form = PortfolioCreateForm()

    if form.validate_on_submit():
        try: 
            portfolio = Portfolio(name=form.data['name'])
            db.session.add(portfolio)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Something went wrong with your Portfolio.')
            print('no bueno')
            return render_template('portfolio.html', form=form)

        return redirect(url_for('.company_search'))

    companies = Company.query.filter_by()
    return render_template('portfolio.html', companies=companies, form=form)            

@app.route('/preview', methods=['GET', 'POST'])
@login_required
def preview_page():

    form_context = {
        'name': session['context']['companyName'],
        'symbol': session['symbol']
    }

    form = CompanyAddForm(**form_context)
    if form.validate_on_submit():
        try:
            
            new_company = Company(name=form.data['name'], symbol=form.data['symbol'], portfolio_id=form.data['portfolios'],)
            db.session.add(new_company)
            db.session.commit()
            print('done')
        except (DBAPIError, IntegrityError):
            flash('Something went wrong with your search.')
            db.session.rollback()
            return redirect(url_for('.company_search'))

        return redirect(url_for('.portfolio_page')), 302

    return render_template(
        'preview.html',
        form=form,
        symbol=form_context['symbol'],
        symbol_data=session['context'],
    )        