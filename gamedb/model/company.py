from gamedb import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    location = db.relationship("Location")

    def __repr__(self):
        return "<Company {name}>".format(name=self.name)
