#####################################################################################
# Name: Scott Ramroth
# Class: CS3080 Python Programming
# 
# Description: MTGCollector is a web-based card collection application that utlizes
# open source card pricing data to help collectors keep track of the value of their
# collection. The application is build in Flask and uses SQLAlchemy to manage a
# database.
#####################################################################################

from mtgcollector import db

#######################################################
# Models
#######################################################
class CollectionCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    set = db.Column(db.String(50), nullable=False)
    foil = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)

    def __repr__(self):
       return f"CollectionCard('{self.name}', '{self.set}', '{self.foil}')"


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    cards = db.relationship('CollectionCard', backref='collection', lazy=True)

    def __repr__(self):
        return f"Collection('{self.title}', '{self.cards})')"


