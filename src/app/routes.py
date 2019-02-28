from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/search', method=['GET'])
# def city_search_form():
#     return render_template('/search.html')

# @app.route('/search', method=['POST'])
# def city_search_results():
#     render_template()   
    