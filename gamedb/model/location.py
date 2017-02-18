from gamedb import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)

    def __repr__(self):
        return "<Location {city}, {state}, {country}>".format(city=self.city, state=self.state, country=self.country)
