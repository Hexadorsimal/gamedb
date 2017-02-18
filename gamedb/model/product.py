from gamedb import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return "<Product {name}>".format(name=self.name)
