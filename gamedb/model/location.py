from gamedb import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return "<Location {name}>".format(name=self.name)
