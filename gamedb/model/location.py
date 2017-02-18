from gamedb import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip = db.Column(db.String)
    country = db.Column(db.String)

    def __repr__(self):
        return "<Location {street} {city}, {state} {zip} {country}>".format(street=self.street, city=self.city, state=self.state, zip=self.zip, country=self.country)
