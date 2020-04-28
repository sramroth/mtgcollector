from flask import render_template, url_for
from mtgcollector import app
from mtgcollector.models import Card, Collection


dummy_collection = [
        {
        'name': 'Stone Giant',
        'set': 'Duel Decks: Venser vs. Koth',
        'foil': False,
        'price': 3.48,
        },
        {
        'name': 'Flooded Grove',
        'set': 'Zendikar Expeditions',
        'foil': True,
        'price': 150.00,
        }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/collections')
def collections():
    return render_template('collections.html', collection=dummy_collection)

@app.route('/about')
def about():
    return render_template('about.html')