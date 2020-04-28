from mtgcollector import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)

    def __repr__(self):
       return f"Card('{self.name}', '{self.price}')"


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    cards = db.relationship('Card', backref='collection', lazy=True)

    def __repr__(self):
        return f"Collection('{self.title}', '{self.cards})')"