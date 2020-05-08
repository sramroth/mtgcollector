#####################################################################################
# Name: Scott Ramroth
# Class: CS3080 Python Programming
# 
# Description: MTGCollector is a web-based card collection application that utlizes
# open source card pricing data to help collectors keep track of the value of their
# collection. The application is build in Flask and uses SQLAlchemy to manage a
# database.
#####################################################################################

import csv
from flask import render_template, url_for, flash, redirect
from mtgcollector import app, db
from mtgcollector.forms import CardForm
from mtgcollector.models import CollectionCard, Collection

#######################################################
# Helper Functions
#######################################################

# Find the seearched card within the csv files and return it as a CollectionCard object
def add_new_card(card_name, foil, collection_id, card_filename, prices_filename):
    with open(card_filename, 'r', encoding='utf8') as cards_csv:
        cards_reader = csv.reader(cards_csv, delimiter=',')
        for row in cards_reader:
            if row[48].lower() == card_name.lower():
                if len(row[71]) > 1:
                    name = row[48] 
                    set_code= row[61]
                    uuid = row[71]
                else:
                    name = row[48] 
                    set_code= row[61]
                    uuid = row[70]
                break
    with open(prices_filename, 'r', encoding='utf8') as prices_csv:
        prices_reader = csv.reader(prices_csv, delimiter=',')
        for row in prices_reader:
            if row[5] == uuid and row[4] == foil:
                price = row[3]
                break
    return CollectionCard(name=name, set=set_code, foil=foil, price=price, collection_id=collection_id)


#######################################################
# Routes (Views)
#######################################################
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/collection')
def collections():
    return render_template('collection.html', collection=CollectionCard.query.filter_by(collection_id=1))

@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    card_form = CardForm()
    if card_form.validate_on_submit():
        new_card = add_new_card(card_form.search.data, card_form.is_foil.data, 1, 
                                'cards.csv', 'prices.csv')
        db.session.add(new_card)
        db.session.commit()
        return redirect(url_for('collections'))
    return render_template('add.html', card_form=card_form)

@app.route('/about')
def about():
    return render_template('about.html')